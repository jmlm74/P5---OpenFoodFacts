# Created by jmlm at 30/03/2020-20:03 - testP5
from myapp.tools.jmlmtools import database_connect, jmlm_now
from myapp.setup import *

import requests

""""
Products table --> 
A product is getting from the openfoodfacts API
To minimize the API calls a temp table with everything we need is created.
Then the datas are extracted from this temp table and the others tables (products, stores) are
    created
At the end of the database creation, the temp table is dropped.   
"""


class Product:
    """
      The Product class
      Attributes :
          Table_name
          temp_table_name
          url1 is the beginning of the API url of openfoodfact API
          url2 is the end
          between the 2 urls the category is inserted before request it
      The tables :
      2 tables : temporary one and production one
      the temporary is used to get the datas from openfoodfacts API
      Store, product tables are from this temp table
      6 columns : idProduct, productName, url, nutriscore_score, nutriscore_grade, idCategory
          Primary key : idproduct
          1 constraint (foreign key) with T_Category Table on idcategory
      methods
          Create/drop tables
          fill tables
          get/insert records
      """

    def __init__(self) -> object:
        """
        init --> just init the variables !
        """
        self.table_name = TABLES["T_PRODUCTS"]
        self.temp_table_name = TABLES["T_TEMPPRODUCTS"]
        self.url1 = URL_PRODUCTS1
        self.url2 = URL_PRODUCTS2

    def create_table_products(self):
        """
        Drop the table if exists and create it
        :return:
        """
        with database_connect() as cursor:
            sql = "drop table if exists %s " % self.table_name
            cursor.execute(sql)
            sql = "CREATE TABLE %s (idProduct INT UNSIGNED NOT NULL AUTO_INCREMENT, " \
                  "productName VARCHAR(80) NOT NULL," \
                  "url TEXT NULL, " \
                  "nutriscore_score SMALLINT DEFAULT 100," \
                  "nutriscore_grade CHAR(1) DEFAULT 'z', " \
                  "idCategory INT UNSIGNED," \
                  "dateCreation TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP," \
                  "CONSTRAINT FK_Category FOREIGN KEY (idCategory) REFERENCES T_Categories(idCategory) ," \
                  "PRIMARY KEY (idProduct)) ENGINE=InnoDB CHARSET latin1" % self.table_name
            cursor.execute(sql)

    def create_temptable_products(self):
        """
        Drop the temp table if exists and create it
        :return:
        """
        with database_connect() as cursor:
            sql = "drop table if exists %s " % self.temp_table_name
            cursor.execute(sql)
            sql = "CREATE TABLE %s (idProduct INT UNSIGNED NOT NULL AUTO_INCREMENT, " \
                  "productName VARCHAR(80) NOT NULL," \
                  "url TEXT NULL, " \
                  "nutriscore_score SMALLINT DEFAULT 100," \
                  "nutriscore_grade CHAR(1) DEFAULT 'z', " \
                  "Store VARCHAR(100), " \
                  "idCategory INT UNSIGNED," \
                  "PRIMARY KEY (idProduct)) ENGINE=InnoDB CHARACTER SET latin1" % self.temp_table_name
            #  "CONSTRAINT fk_tempcategory FOREIGN KEY (idCategory) REFERENCES T_Categories(idCategory) ," \
            cursor.execute(sql)

    def drop_temptable_products(self):
        """
        drop the temptable
        :return:
        """
        with database_connect() as cursor:
            sql = "drop table if exists %s " % self.temp_table_name
            cursor.execute(sql)

    def drop_table_products(self):
        """
        drop the table
        :return:
        """
        with database_connect() as cursor:
            sql = "drop table if exists %s " % self.table_name
            cursor.execute(sql)

    def fill_temptable_products(self):
        """
        fill the temp table
        get the categories from the T_Category table.
        For each category -->
            Construct the url
            request the url
            get the result in json and parse it
            insert datas in the temp table
        :return:
        """
        dbconn = database_connect()
        with dbconn as cursor:
            # get the categories
            sql = "select idCategory,categoryName from T_Categories"
            cursor.execute(sql)
            categories = cursor.fetchall()
            # for each category
            for category in categories:
                print("Récupère données : {} - {}".format(category[0], category[1]))
                # prepare the sql
                sql1 = "insert into %s (productName,url,nutriscore_score,nutriscore_grade,Store,idCategory)" \
                       " values" % self.temp_table_name
                # 3 pages (page 2-4-6) of 20 products
                for i in range(2, 7, 2):
                    # build the url
                    url = self.url1 + category[1] + self.url2 + str(i)
                    # get the response - parse the json file and then insert the product
                    response = requests.get(url)
                    if (response.status_code) == 200:
                        # text = json.loads(response.content.decode('latin1'))
                        text = response.json()
                        for t in text['products']:
                            if 'product_name' in t and len(t['product_name']) > 0:
                                t['product_name'] = t['product_name'][:79]
                                t['product_name'] = t['product_name'].replace("'", " ")
                                if 'url' not in t:
                                    t['url'] = ''
                                if 'nutriscore_score' not in t:
                                    t['nutriscore_score'] = "100"
                                if 'nutriscore_grade' not in t:
                                    t['nutriscore_grade'] = "Z"
                                if 'brands' not in t:
                                    t['brands'] = "Inconnu"
                                t['brands'] = t['brands'][:49]
                                if len(t['brands']) == 0:
                                    t['brands'] = "Inconnu"
                                t['brands'] = t['brands'].replace("'", " ")
                                sql2 = "('%s','%s',%s,'%s','%s',%s)" % (t['product_name'],
                                                                        t['url'],
                                                                        t['nutriscore_score'],
                                                                        t['nutriscore_grade'],
                                                                        t['brands'],
                                                                        category[0])
                                sql = sql1 + sql2
                                cursor.execute((sql))
                dbconn.commit()

    def fill_table_products(self):
        """
        fill the table T_Product from the temp table
        :param self:
        :return:
        """
        sql = "insert into T_Products (productName,url,nutriscore_score,nutriscore_grade,idCategory) select " \
              "productName,url, nutriscore_score,nutriscore_grade,idCategory from T_TempProducts group by productName;"
        dbconn = database_connect()
        with dbconn as cursor:
            cursor.execute(sql)
            dbconn.commit()

    def list_products_bycat(self, idcategory):
        """
        get all products for an idcategory
        :param idcategory:
        :return: row(s) of product [(idProduct, productName,url, nutriscore_score,
                                    nutriscore_grade,idCategory,dateCreation),...]
        """
        sql = "select idProduct, productName,url, nutriscore_score, nutriscore_grade,idCategory, " \
              "dateCreation from %s where idCategory=" % self.table_name
        sql = sql + """%s  order by idProduct"""
        with database_connect() as cursor:
            cursor.execute(sql, (idcategory,))
            rows = cursor.fetchall()
        return rows

    def get_product_byid(self, idproduct):
        """
        Get a product by id
        :param idproduct:
        :return: row of 1 product [(idProduct, productName,url, nutriscore_score,
                                    nutriscore_grade,idCategory,dateCreation)]
        """
        sql = "select idProduct, productName,url,nutriscore_score,nutriscore_grade,idCategory, " \
              "dateCreation from %s where idProduct=" % self.table_name
        sql = sql + """%s"""
        with database_connect() as cursor:
            cursor.execute(sql, (idproduct,))
            row = cursor.fetchone()
        return row

    def get_product_bookmarks(self, idproduct, ):
        """
        Get the products which have been bookmarked for a product - get the substitutes for
            a product
        the url is cut as 53 char to fit in the chart but it keeps good (you can click on it)
        :param idproduct:
        :return: row(s) of products [(idProduct, productName,substr(url,1,53),nutriscore_score,
                    nutriscore_grade,idCategory)...]
        """
        sql = "select  idProduct, productName,substr(url,1,53),nutriscore_score,nutriscore_grade,idCategory " \
              "from %s where idcategory = (select idcategory from T_Products where " \
              "idProduct = %d) and nutriscore_score <= (select nutriscore_score from T_Products " \
              "where idProduct = %d order by nutriscore_score desc)" % (self.table_name, idproduct, idproduct)
        with database_connect() as cursor:
            cursor.execute(sql)
            rows = cursor.fetchall()
        return rows
