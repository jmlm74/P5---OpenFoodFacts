# Created by jmlm at 07/04/2020-15:08 - P5
from models.category import categoryTable
from models.brands import brandsTable
from models.products import productsTable
from models.products_brands import products_brandsTable
from tools.databaseSQL import databaseConnect
from tools import jmlmtools
from setup import *



def fill_database():
    """
    drop table T_Products_Brands (products <-> brands)
    """
    tableProductsBrands = products_brandsTable()
    tableProductsBrands.drop_table_products_brands()

    """
    drop table T_products
    """
    tableproducts = productsTable()
    tableproducts.drop_table_products()


    """
    create & fill table T_Category
    """
    tableCat = categoryTable()
    tableCat.create_table_category()
    tableCat.fill_table_category()

    """
    create and fill tables T_tempProducts and Products
    """
    tableproducts.create_temptable_products()
    tableproducts.create_table_products()
    tableproducts.fill_temptable_products()
    tableproducts.fill_table_products()

    """
    create and fill table T_brands (need tempProducts)
    """
    tableBrands = brandsTable()
    tableBrands.create_table_brands()
    tableBrands.fill_table_brands()

    """
    create and fill table T_Brands_Products 
    """
    tableProductsBrands.create_table_products_brands()
    tableProductsBrands.fill_table_products_brands()

    """
    drop temp table
    """
    tableproducts.drop_temptable_products()


def test_database():
    """
    Test la base :
    - Connexion

    :return:
    """
    connex = databaseConnect()
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
        sql = 'SELECT idCategory from T_Categories where TIMESTAMPDIFF(DAY,now(),dateCreation)<7 limit 1'
        cursor.execute(sql)
        result = cursor.fetchone()
        if result:
            print("ATTENTION : Les données ont plus de 7 jours. Il est vivement conseillé de récupérer les nouvelles "
                  "données. Pour cela réexecuter le programme avec le parametre '-d create'")
        else:
            print("La date des données est inférieure à 7 jours.")

        connex.disconnect_db()