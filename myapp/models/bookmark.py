# Created by jmlm at 12/04/2020-17:03 - P5
from myapp.tools.jmlmtools import database_connect

from myapp.setup import *



class Bookmark:

    def __init__(self):
        self.tableName = TABLES["T_BOOKMARKS"]

    def create_table_bookmarks(self):
        with database_connect() as cursor:
            sql = "drop table if exists %s " % self.tableName
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
        with database_connect() as cursor:
            sql = "drop table if exists %s " % self.tableName
            cursor.execute(sql)

    def get_bookmark_byproduct(self,idproduct):
        sql = "select idproduct,idproduct1 from %s where idproduct=" % self.tableName
        sql = sql + """%s"""
        with database_connect() as cursor:
            cursor.execute(sql,(idproduct, ))
            rows = cursor.fetchall()
        return rows