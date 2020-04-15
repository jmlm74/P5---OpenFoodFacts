# Created by jmlm at 30/03/2020-20:03 - testP5
from myapp.tools.jmlmtools import database_connect, jmlm_now
from myapp.setup import *

""""
T_Stores table
stores are from the temp_products table 
The relationship with products is a many to many relationship made through T_Products_Stores table 
"""


class Store:
    """
      The Store class
      Attributes :
          Table_name
      The table :
          2 columns : idStore and storeName
          Primary key : idStore
      methods
          Create/drop table
          fill table
          get records
      """
    def __init__(self) -> object:
        """
        init --> just init the variables !
        """
        self.tableName = TABLES["T_STORES"]


    def create_table_stores(self):
        """
        Drop the table if exists and create it
        :return:
        """
        with database_connect() as cursor:
            sql = "drop table if exists %s " % self.tableName
            param = ""
            cursor.execute(sql, param)
            sql = "CREATE TABLE %s (idStore INT UNSIGNED NOT NULL AUTO_INCREMENT, " \
                  "storeName VARCHAR(80) NULL," \
                  "dateCreation TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP," \
                  "PRIMARY KEY (idStore)) ENGINE=InnoDB CHARSET latin1" % self.tableName
            cursor.execute(sql, param)

    def fill_table_stores(self):
        """
        get distinct Store in temp_products table and insert in Store table
        :return:
        """
        sql = 'insert into T_Stores (storeName) SELECT distinct(Store) FROM test.T_TempProducts order by 1;'
        dbconn = database_connect()
        with dbconn as cursor:
            cursor.execute(sql)
            dbconn.commit()

    def get_store_byproduct(self,idproduct):
        """
        get storeName by idproduct
        :param idproduct:
        :return: row(s) Stores [(storename),...]
        """
        sql = """Select storeName from T_Products_stores as T  inner join T_Products as P  \
             on P.idProduct=T.idProduct inner join T_Stores as S on T.idStore = S.idStore  \
             where P.idProduct = %s"""
        with database_connect() as cursor:
            cursor.execute(sql,(idproduct,))
            rows = cursor.fetchall()
        return rows
