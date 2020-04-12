# Created by jmlm at 08/04/2020-19:15 - P5
from __future__ import print_function, unicode_literals
from PyInquirer import prompt, Separator, style_from_dict, Token
from examples import custom_style_3, custom_style_2, custom_style_1


from myapp.setup import *
from myapp.models.category import Category
from myapp.models.product import Product


class UserChoiceText:

    def __init__(self):
        self.__choixN = 0
        self.__choixT = ""
        self.__choixL = []
        self.couleur_prompt = ""
        self.msg_prompt = ""

    def message(self, cli):
        return [
            (self.couleur_prompt, self.msg_prompt),
        ]

    def choice_prompt_numeric(self):
        from prompt_toolkit.shortcuts import Token, prompt

        try:
            self.msg_prompt = "Entrez votre choix : "
            self.couleur_prompt = Token.Blue
            self.__choixN = int(prompt(get_prompt_tokens=self.message, style=style))
            return self.__choixN
        except ValueError:
            return 999

    def choice_prompt_text(self,message):
        from prompt_toolkit.shortcuts import Token, prompt

        try:
            self.msg_prompt = message
            self.couleur_prompt = Token.Blue
            self.__choixT = str(prompt(get_prompt_tokens=self.message, style=style))
            return self.__choixT
        except ValueError:
            return "999"


    def category_choice(self):
        category = Category()
        listCat = category.list_categories()
        list_choices = []
        for cat in listCat:
            choice = "%02d - %s" % (cat[0], cat[1])
            list_choices.append(choice)
        list_choices.append(Separator())
        list_choices.append("00 - retour")
        question = [{'type': 'list',
                     'name': 'menu2',
                     'message': "Choisissez la catégorie du produit",
                     'choices': list_choices,
                     'carousel': True}, ]
        response = prompt(question, style=custom_style_1)
        ind = response['menu2'].split()
        rc = int(ind[0])
        return rc

    def product_choice_bycat(self, idcategory):
        cat = Category()
        category = cat.get_category_byid(idcategory)
        msg = "Choisissez un produit de la catégorie %s " % category[1]
        product = Product()
        products = product.list_products_bycat(idcategory)
        list_products = []
        for prod in products:
            choice = "%02d - %s" % (prod[0], prod[1])
            list_products.append(choice)
        list_products.append(Separator())
        list_products.append("00 - retour")
        question = [{'type': 'list',
                     'name': 'menu3',
                     'message': msg,
                     'choices': list_products,
                     'carousel': True}]
        response = prompt(question, style=custom_style_1)
        ind = response['menu3'].split()
        rc = int(ind[0])
        return rc
"""
    def product_substitut(self, idproduct):
        prod = Product()
        product = prod.get_product_byid(idproduct)
        return product
"""

