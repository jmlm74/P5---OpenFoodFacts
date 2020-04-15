# Created by jmlm at 12/04/2020-17:03 - P5
"""
Bookmarks table (substitutes)
a bookmark is like a tuple with the product and one of his substitution products
A many to many relationship table between T_Products and T_Products
  - 1 product may have many substitutes
  - 1 product may be a substitute of many products
"""
from myapp.tools.jmlmtools import database_connect
from myapp.setup import *

from mysql.connector import Error


class Bookmark:
    """
    The bookmarks class
    Attributes :
        Table_name
    The table :
        2 columns : idproduct and idproduct1  --> many many to many relationship table
            between T_Products and T_Products
        Primary key : idproduct,idproduct1
        2 constraints (foreign keys) with T_Product Table on idproduct
    methods
        Create/drop table
        get/insert records
    """
    def __init__(self):
        self.table_name = TABLES["T_BOOKMARKS"]

    def create_table_bookmarks(self):
        """
        drop if exist then create the table
        :return:
        """
        with database_connect() as cursor:
            sql = "drop table if exists %s " % self.table_name
            cursor.execute(sql)
            sql = "CREATE TABLE IF NOT EXISTS `test`.`T_Bookmarks` (" \
                  "`idproduct` INT(10) UNSIGNED NOT NULL," \
                  "`idproduct1` INT(10) UNSIGNED NOT NULL," \
                  "CONSTRAINT `I_Bookmarks` PRIMARY KEY (`idproduct`, `idproduct1`)," \
                  "CONSTRAINT `fk_T_Products_idproduct`" \
                  "FOREIGN KEY (`idproduct`) " \
                  "REFERENCES `T_Products` (`idproduct`) " \
                  "ON DELETE NO ACTION ON UPDATE NO ACTION, " \
                  "CONSTRAINT `fk_T_Products_Idproduct1` " \
                  "FOREIGN KEY (`idproduct1`) " \
                  "REFERENCES `T_Products` (`idproduct`) " \
                  "ON DELETE NO ACTION " \
                  "ON UPDATE NO ACTION) ENGINE = InnoDB DEFAULT CHARACTER SET = latin1"
            cursor.execute(sql)

    def drop_table_bookmarks(self):
        """
        drop the table
        :return:
        """
        with database_connect() as cursor:
            sql = "drop table if exists %s " % self.table_name
            cursor.execute(sql)

    def get_bookmark_byproduct(self,idproduct):
        """
        Get bookmark(s) - substitute(s) - by product id
        :param idproduct:
        :return: row(s) [(idproduct,idproduct1],...]
        """
        sql = "select idproduct,idproduct1 from %s where idproduct=" % self.table_name
        sql = sql + """%s"""
        with database_connect() as cursor:
            cursor.execute(sql,(idproduct, ))
            rows = cursor.fetchall()
        return rows

    def add_bookmark(self,idproduct,idproduct1):
        """
        add a bookmark then commit work
        catch an error and rollback work if necessary
        :param idproduct:
        :param idproduct1:
        :return: 0, 'OK' if OK or 1 and error message if sql insert error
        """
        sql = f"insert into {self.table_name} (idproduct,idproduct1) values "
        sql += """(%s,%s)"""
        cnx = database_connect()
        with cnx as cursor:
            try:
                cursor.execute(sql,(idproduct,idproduct1))
                cnx.commit()
                return 0, "OK"
            except Error as e:
                cnx.rollback()
                return 1, e

    def get_all_bookmarks(self):
        """
        get all the bookmarks
        :return: the bookmarks list [(idproduct,idproduct1],...]
        """
        sql = "select idproduct,idproduct1 from %s order by 1" % self.table_name
        with database_connect() as cursor:
            cursor.execute(sql)
            rows=cursor.fetchall()
        return rows