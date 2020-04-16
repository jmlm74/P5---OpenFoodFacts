# Created by jmlm at 02/04/2020-18:46 - testP5
from myapp.tools.jmlmtools import database_connect
from myapp.setup import *

"""
The many to many relationship table for products and stores
The table is filled from the temp_products and the store tables
Rows are like a tuple (idStore,idProduct)
A many to many relationship table between T_Products and T_Store
  - 1 product may have many Stores
  - 1 Store may be a Store for many products
"""


class ProductsStore:
    """
    the class ProductsStore
        Attributes :
        Table_name
    The table :
        2 columns : idStore and idProduct  --> many many to many relationship table
            between T_Store and T_Products
        Primary key : idStore
        2 constraints (foreign keys) with T_Store on idStore and T_products on id_Products
    methods
        Create/drop table
        fill the records
    """

    def __init__(self) -> object:
        """
        just init the variables
         :return:
        """
        self.table_name = TABLES["T_PRODUCTS_STORES"]

    def create_table_products_stores(self):
        """
        Drop the table if exists and create it
        :return:
        """
        with  database_connect() as cursor:
            sql = "drop table if exists %s " % self.table_name
            param = ""
            cursor.execute(sql, param)
            sql = "CREATE TABLE %s (idStore INT UNSIGNED NOT NULL," \
                  "idProduct INT UNSIGNED NOT NULL," \
                  "CONSTRAINT `I_Products_Stores` PRIMARY KEY (`idStore`, `idProduct`)," \
                  "CONSTRAINT FK_Stores FOREIGN KEY (idStore) REFERENCES T_Stores(idStore)," \
                  "CONSTRAINT FK_Products FOREIGN KEY (idProduct) REFERENCES T_Products(idProduct)) " \
                  "ENGINE=InnoDB CHARSET latin1" % self.table_name
            cursor.execute(sql, param)

    def fill_table_products_stores(self):
        """
        get distinct Store in temp_products table and insert the ids from the T_Store and the
        T_Pproducts tables (to get the ids)
        :return:
        """
        sql = "insert ignore into %s (idStore,idProduct) select B.idStore,P.idProduct from T_Stores " \
              "as B inner join T_TempProducts as TP on Store = storeName inner join T_Products as P on " \
              "TP.productName = P.productName order by 1;" % self.table_name
        dbconn = database_connect()
        with dbconn as cursor:
            cursor.execute(sql)
            dbconn.commit()

    def drop_table_products_stores(self):
        """
        drop the table
        :return:
        """
        with database_connect() as cursor:
            sql = "drop table if exists %s " % self.table_name
            cursor.execute(sql)