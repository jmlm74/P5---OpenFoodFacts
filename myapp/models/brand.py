# Created by jmlm at 30/03/2020-20:03 - testP5
from myapp.tools.jmlmtools import database_connect
from myapp.setup import *
from myapp.tools.jmlmtools import jmlm_now

""""
Brand table --> 
"""


class Brand:

    def __init__(self) -> object:
        """
        init --> just init the variables !
        """
        self.tableName = TABLES["T_BRANDS"]
        self.url = URL_BRANDS
        # Data
        self.idBrand = 0
        self.brandName = ""
        self.dateCreation = jmlm_now()

    def create_table_brands(self):
        """
        Drop the table if exists and create it
        :return:
        """
        with database_connect() as cursor:
            sql = "drop table if exists %s " % self.tableName
            param = ""
            cursor.execute(sql, param)
            sql = "CREATE TABLE %s (idBrand INT UNSIGNED NOT NULL AUTO_INCREMENT, " \
                  "brandName VARCHAR(80) NULL," \
                  "dateCreation TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP," \
                  "PRIMARY KEY (idBrand)) ENGINE=InnoDB CHARSET latin1" % self.tableName
            cursor.execute(sql, param)

    def fill_table_brands(self):
        """
        get distinct Brand in temp_products table and insert in Brand table
        :return:
        """
        sql = 'insert into T_Brands (brandName) SELECT distinct(Brand) FROM test.T_TempProducts order by 1;'
        dbconn = database_connect()
        with dbconn as cursor:
            cursor.execute(sql)
            dbconn.commit()
