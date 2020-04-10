# Created by jmlm at 30/03/2020-20:03 - testP5
from myapp.tools.jmlmtools import database_connect
from myapp.setup import *
from myapp.tools.jmlmtools import jmlm_now

""""
Store table --> 
"""


class Store:

    def __init__(self) -> object:
        """
        init --> just init the variables !
        """
        self.tableName = TABLES["T_STORES"]
        self.url = URL_STORES
        # Data
        self.idStore = 0
        self.StoreName = ""
        self.dateCreation = jmlm_now()

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
