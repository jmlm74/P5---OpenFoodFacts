# Created by jmlm at 30/03/2020-20:03 - testP5
from tools.databaseSQL import databaseConnect
from tools import jmlmtools
from setup import *
import json
import requests
import unicodedata
""""
brands table --> 
"""


class brandsTable:

    def __init__(self) -> object:
        """
        init --> just init the variables !
        """
        self.tableName = TABLES["T_BRANDS"]
        self.url = URL_BRANDS


    def create_table_brands(self):
        """
        Drop the table if exists and create it
        :return:
        """
        with databaseConnect() as cursor:
            sql = "drop table if exists %s " % self.tableName
            param = ""
            cursor.execute(sql,param)
            sql = "CREATE TABLE %s (idBrand INT UNSIGNED NOT NULL AUTO_INCREMENT, "\
                  "brandName VARCHAR(80) NULL," \
                  "dateCreation TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP," \
                  "PRIMARY KEY (idBrand)) ENGINE=InnoDB CHARSET latin1" % self.tableName
            cursor.execute(sql,param)


    def fill_table_brands(self):
        """
        get distinct brands in temp_products table and insert in brands table
        :return:
        """
        sql = 'insert into T_Brands (brandName) SELECT distinct(brands) FROM test.T_TempProducts order by 1;'
        dbconn = databaseConnect()
        with dbconn as cursor:
            cursor.execute(sql)
            dbconn.commit()


