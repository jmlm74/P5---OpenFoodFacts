# Created by jmlm at 30/03/2020-20:03 - testP5
from myapp.tools.jmlmtools import database_connect
from myapp.setup import *

""""
Category table --> 
a row only contains the id and the category full name
"""


class Category:
    """
     The Categories class
     Attributes :
         Table_name
     The table :
         2 columns : idCategory, categoryName
         Primary key : idCategory
     methods
         Create/drop table
         Fill the table
         get/insert records
     """

    def __init__(self) -> object:
        """
        init --> just init the variables !
        """
        self.table_name = TABLES['T_CATEGORY']

    def create_table_category(self):
        """
        Drop the table if exists and create it
        :return:
        """
        dbconn = database_connect()
        with dbconn as cursor:
            sql = "drop table if exists %s " % self.table_name
            param = ""
            cursor.execute(sql, param)
            sql = 'CREATE TABLE %s (idCategory INT UNSIGNED NOT NULL AUTO_INCREMENT,' \
                  'categoryName VARCHAR(80) NULL,' \
                  ' dateCreation TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,' \
                  'PRIMARY KEY (idCategory)) ENGINE=InnoDB CHARSET latin1' % self.table_name
            cursor.execute(sql, param)
            dbconn.commit()

    def drop_table_bookmarks(self):
        """
        drop the table
        :return:
        """
        with database_connect() as cursor:
            sql = 'drop table if exists %s ' % self.table_name
            cursor.execute(sql)

    def fill_table_category(self):
        """
        Loop on CAT_LIST and insert items into table
        :return: None
        """
        sql1 = 'insert into %s (categoryName) values ' % self.table_name
        dbconn = database_connect()
        with dbconn as cursor:
            for cat in CAT_LIST:
                sql = sql1 + """(%s)"""
                print('Insertion : ', cat)
                cursor.execute(sql, (cat,))
            dbconn.commit()
            dbconn.disconnect_db()

    def list_categories(self):
        """
        get all the categories
        :return: row(s) - categories list [(idcategory, categoryName),...]
        """
        sql = 'select idCategory, categoryName from ' + self.table_name + " order by 1"
        with database_connect() as cursor:
            cursor.execute(sql)
            rows = cursor.fetchall()
        return rows

    def get_category_byid(self, id):
        """
        get a category by id (1 row)
        :param id:
        :return: 1 row [(idcategory, categoryName)]
        """
        sql = 'select idCategory, categoryName,dateCreation from %s where idCategory=' % self.table_name
        sql = sql + """%s"""
        with database_connect() as cursor:
            cursor.execute(sql, (id,))
            row = cursor.fetchone()
        return row
