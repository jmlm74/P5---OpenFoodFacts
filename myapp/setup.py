# Created by jmlm at 30/03/2020-22:29 - testP5
from pathlib import Path

from prompt_toolkit.styles import style_from_dict
from pygments.token import Token

# the curent path
BASEDIR = Path(__file__).resolve().parent


# DATABASE
DBHOST = '192.168.1.99'  # Database host (may be localhost)
DBUSER = 'jmlm'
DBPW = 'jmlmpw'
DBNAME = 'P5_DB'
TABLES = {
    "T_CATEGORY": 'T_Categories',
    "T_STORES": 'T_Stores',
    "T_PRODUCTS_STORES": "T_Products_stores",
    "T_TEMPPRODUCTS": 'T_TempProducts',
    "T_PRODUCTS": 'T_Products',
    "T_BOOKMARKS": 'T_Bookmarks',
    }

#URLs
URL_STORES = 'https://fr.openfoodfacts.org/brands.json'
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

