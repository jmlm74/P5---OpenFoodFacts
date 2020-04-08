# Created by jmlm at 30/03/2020-22:29 - testP5
from pathlib import Path

# the curent path
BASEDIR = Path(__file__).resolve().parent


# DATABASE
DBHOST = '192.168.1.99'  # Database host (may be localhost)
DBUSER = 'jmlm'
DBPW = 'jmlmpw'
DBNAME = 'test'
TABLES = {
    "T_CATEGORY": 'T_Categories',
    "T_BRANDS": 'T_Brands',
    "T_PRODUCTS_BRANDS": "T_Products_Brands",
    "T_TEMPPRODUCTS": 'T_TempProducts',
    "T_PRODUCTS": 'T_Products'
    }

#URLs
URL_BRANDS = 'https://fr.openfoodfacts.org/brands.json'
URL_PRODUCTS1 = 'https://world.openfoodfacts.org/cgi/search.pl?action=process&tagtype_0=categories&tag_contains_0=' \
                'contains&tag_0='
URL_PRODUCTS2 = '&sort_by=product_name&page_size=20&action=process&json=true,&page='

# Categories
CAT_LIST = ['Poissons',
            'pate-a-tartiner',
            'fruits secs',
            'gateaux',
            'Volailles',
            'Desserts',
            'sandwichs',
            'Plats préparés à la viande']
