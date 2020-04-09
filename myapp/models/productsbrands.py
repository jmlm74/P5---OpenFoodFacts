# Created by jmlm at 02/04/2020-18:46 - testP5
from myapp.tools.jmlmtools import database_connect
from myapp.setup import *

"""
"""


class ProductsBrands:
    """
    """

    def __init__(self) -> object:
        """
        select B.idBrands,B.BrandName,TP.ProductName,P.idProduct from T_Brands as B inner join T_TempProducts as TP
        on Brand = brandName inner join T_Products as P on TP.productName = P.productName order by 1;

        :return:
        """
        self.tableName = TABLES["T_PRODUCTS_BRANDS"]
        # Data
        self.idProduct = 0
        self.idBrand = 0

    def create_table_products_brands(self):
        """
        Drop the table if exists and create it
        :return:
        """
        with database_connect() as cursor:
            sql = "drop table if exists %s " % self.tableName
            param = ""
            cursor.execute(sql, param)
            sql = "CREATE TABLE %s (idBrand INT UNSIGNED NOT NULL," \
                  "idProduct INT UNSIGNED NOT NULL," \
                  "INDEX IBrand (idBrand)," \
                  "INDEX IProduct (IdProduct)," \
                  "CONSTRAINT FK_Brands FOREIGN KEY (idBrand) REFERENCES T_Brands(idBrand)," \
                  "CONSTRAINT FK_Products FOREIGN KEY (idProduct) REFERENCES T_Products(idProduct)) " \
                  "ENGINE=InnoDB CHARSET latin1" % self.tableName
            cursor.execute(sql, param)

    def fill_table_products_brands(self):
        """
        get distinct Brand in temp_products table and insert in Brand table
        :return:
        """
        sql = 'insert into T_Brands (brandName) SELECT distinct(Brand) FROM test.T_TempProducts order by 1;'
        sql = "insert into %s (idBrand,idProduct) select B.idBrand,P.idProduct from T_Brands " \
              "as B inner join T_TempProducts as TP on Brand = brandName inner join T_Products as P on " \
              "TP.productName = P.productName order by 1;" % self.tableName
        dbconn = database_connect()
        with dbconn as cursor:
            cursor.execute(sql)
            dbconn.commit()

    def drop_table_products_brands(self):
        with database_connect() as cursor:
            sql = "drop table if exists %s " % self.tableName
            cursor.execute(sql)