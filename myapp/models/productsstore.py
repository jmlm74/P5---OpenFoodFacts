# Created by jmlm at 02/04/2020-18:46 - testP5
from myapp.tools.jmlmtools import database_connect
from myapp.setup import *

"""
"""


class ProductsStore:
    """
    """

    def __init__(self) -> object:
        """
        select B.idBrands,B.BrandName,TP.ProductName,P.idProduct from T_Brands as B inner join T_TempProducts as TP
        on Store = brandName inner join T_Products as P on TP.productName = P.productName order by 1;

        :return:
        """
        self.tableName = TABLES["T_PRODUCTS_STORES"]
        # Data
        self.idProduct = 0
        self.idStore = 0

    def create_table_products_stores(self):
        """
        Drop the table if exists and create it
        :return:
        """
        with database_connect() as cursor:
            sql = "drop table if exists %s " % self.tableName
            param = ""
            cursor.execute(sql, param)
            sql = "CREATE TABLE %s (idStore INT UNSIGNED NOT NULL," \
                  "idProduct INT UNSIGNED NOT NULL," \
                  "INDEX IStore (idStore)," \
                  "INDEX IProduct (IdProduct)," \
                  "CONSTRAINT FK_Stores FOREIGN KEY (idStore) REFERENCES T_Stores(idStore)," \
                  "CONSTRAINT FK_Products FOREIGN KEY (idProduct) REFERENCES T_Products(idProduct)) " \
                  "ENGINE=InnoDB CHARSET latin1" % self.tableName
            cursor.execute(sql, param)

    def fill_table_products_stores(self):
        """
        get distinct Store in temp_products table and insert in Store table
        :return:
        """
        sql = 'insert into T_Stores (storeName) SELECT distinct(Store) FROM test.T_TempProducts order by 1;'
        sql = "insert into %s (idStore,idProduct) select B.idStore,P.idProduct from T_Stores " \
              "as B inner join T_TempProducts as TP on Store = storeName inner join T_Products as P on " \
              "TP.productName = P.productName order by 1;" % self.tableName
        dbconn = database_connect()
        with dbconn as cursor:
            cursor.execute(sql)
            dbconn.commit()

    def drop_table_products_stores(self):
        with database_connect() as cursor:
            sql = "drop table if exists %s " % self.tableName
            cursor.execute(sql)