# Created by jmlm at 07/04/2020-15:08 - P5
from myapp.models.category import Category
from myapp.models.store import Store
from myapp.models.product import Product
from myapp.models.productsstores import ProductsStores
from myapp.tools.jmlmtools import database_connect
from myapp.setup import *


def fill_database():
    """
    drop table T_Products_Brands (Product <-> Store)
    """
    table_products_stores = ProductsStores()
    table_products_stores.drop_table_products_stores()

    """
    drop table T_products
    """
    table_products = Product()
    table_products.drop_table_products()


    """
    create & fill table T_Category
    """
    tableCat = Category()
    tableCat.create_table_category()
    tableCat.fill_table_category()

    """
    create and fill tables T_tempProducts and Products
    """
    table_products.create_temptable_products()
    table_products.create_table_products()
    table_products.fill_temptable_products()
    table_products.fill_table_products()

    """
    create and fill table T_brands (need tempProducts)
    """
    table_stores = Store()
    table_stores.create_table_stores()
    table_stores.fill_table_stores()

    """
    create and fill table T_Brands_Products 
    """
    table_products_stores.create_table_products_stores()
    table_products_stores.fill_table_products_stores()

    """
    drop temp table
    """
    table_products.drop_temptable_products()


def test_database():
    """
    Test la base :
    - Connexion

    :return:
    """
    connex = database_connect()
    test = connex.connect_db()
    if not test :
        print("Erreur de connexion")
        return False
    print("Test connexion : OK")
    sql1 = "show tables like '"
    with connex as cursor:
        print("Test tables")
        for key, value in TABLES.items():
            # don't test temp tables
            if (key[:6]) == 'T_TEMP':
                continue
            print("Testing %s as %s" % (key,value))
            sql = sql1 + value + "'"
            cursor.execute(sql)
            result = cursor.fetchone()
            if result:
                print("Test OK")
            else:
                print("ERREUR tests existence table")
#ToDo mettre > au lieu de < --> tests et demo
        sql = 'SELECT idCategory from T_Categories where TIMESTAMPDIFF(DAY,now(),dateCreation)<30 limit 1'
        try:
            cursor.execute(sql)
            result = cursor.fetchone()
            if result:
                print("ATTENTION : Les données ont plus de 30 jours. Il est vivement conseillé de récupérer les nouvelles "
                      "données. Pour cela réexecuter le programme avec le parametre '-d create'")
            else:
                print("La date des données est inférieure à 7 jours.")
        except:
            pass

        connex.disconnect_db()