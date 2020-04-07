# Created by jmlm at 02/04/2020-18:46 - testP5
from tools.databaseSQL import databaseConnect
from setup import *

"""

"""


class products_brandsTable:
    """
    """

    def __init__(self) -> object:
        """
        select B.idBrands,B.BrandName,TP.ProductName,P.idProduct from T_Brands as B inner join T_TempProducts as TP
        on brands = brandName inner join T_Products as P on TP.productName = P.productName order by 1;

        :return:
        """
        self.tableName = TABLES["T_PRODUCTS_BRANDS"]

    def create_table_products_brands(self):
        """
        Drop the table if exists and create it
        :return:
        """
        with databaseConnect() as cursor:
            sql = "drop table if exists %s " % self.tableName
            param = ""
            cursor.execute(sql, param)
            sql = "CREATE TABLE %s (idBrand INT UNSIGNED NOT NULL," \
                  "idProduct INT UNSIGNED NOT NULL," \
                  "INDEX IBrand (idBrand)," \
                  "INDEX IProduct (IdProduct)," \
                  "dateCreation TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP," \
                  "CONSTRAINT FK_Brands FOREIGN KEY (idBrand) REFERENCES T_Brands(idBrand)," \
                  "CONSTRAINT FK_Products FOREIGN KEY (idProduct) REFERENCES T_Products(idProduct)) " \
                  "ENGINE=InnoDB CHARSET latin1" % self.tableName
            cursor.execute(sql, param)

    def fill_table_products_brands(self):
        """
        get distinct brands in temp_products table and insert in brands table
        :return:
        """
        sql = 'insert into T_Brands (brandName) SELECT distinct(brands) FROM test.T_TempProducts order by 1;'
        sql = "insert into %s (idBrand,idProduct) select B.idBrand,P.idProduct from T_Brands " \
              "as B inner join T_TempProducts as TP on brands = brandName inner join T_Products as P on " \
              "TP.productName = P.productName order by 1;" % self.tableName
        dbconn = databaseConnect()
        with dbconn as cursor:
            cursor.execute(sql)
            dbconn.commit()

    def drop_table_products_brands(self):
        with databaseConnect() as cursor:
            sql = "drop table if exists %s " % self.tableName
            cursor.execute(sql)