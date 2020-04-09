# Created by jmlm at 30/03/2020-20:03 - testP5
from myapp.tools.jmlmtools import database_connect
from myapp.setup import *
""""
Category table --> 
"""


class Category:

    def __init__(self) -> object:
        """
        init --> just init the variables !
        """
        self.tableName = TABLES["T_CATEGORY"]
        # Data
        self.idCategory = ""
        self.categoryName = ""


    def create_table_category(self):
        """
        Drop the table if exists and create it
        :return:
        """
        dbconn = database_connect()
        with dbconn as cursor:
            sql = "drop table if exists %s " % self.tableName
            param = ""
            cursor.execute(sql,param)
            sql = "CREATE TABLE %s (idCategory INT UNSIGNED NOT NULL AUTO_INCREMENT," \
                  "categoryName VARCHAR(80) NULL,"\
                  " dateCreation TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,"\
                  "PRIMARY KEY (idCategory)) ENGINE=InnoDB CHARSET latin1" % self.tableName
            # print(sql)
            cursor.execute(sql,param)
            dbconn.commit()


    def fill_table_category(self):
        """
        Loop on CAT_LIST and insert items into table
        :return: None
        """
        sql1 = "insert into %s (categoryName) values " % self.tableName
        dbconn = database_connect()
        with dbconn as cursor:
            for cat in CAT_LIST:
                    sql = sql1 + """(%s)"""
                    print("Insertion : ",cat)
                    cursor.execute(sql,(cat,))
            dbconn.commit()
            dbconn.disconnect_db()

    def list_categories(self):
        sql = "select idCategory, categoryName from " + self.tableName + " order by 1"
        dbconn = database_connect()
        with dbconn as cursor:
            cursor.execute(sql)
            rows = cursor.fetchall()
        return rows

    def get_category(self,id):
        sql = "select idCategory, categoryName,dateCreation from %s where idCategory=" % self.tableName
        sql = sql + """%s"""
        with database_connect() as cursor:
            cursor.execute(sql,(id,))
            row = cursor.fetchone()
        return row