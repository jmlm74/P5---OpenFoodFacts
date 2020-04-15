# Created by jmlm at 08/04/2020-19:15 - P5
"""
User prompts and choices
"""
from __future__ import print_function, unicode_literals

from PyInquirer import prompt, Separator
from examples import custom_style_1

from myapp.models.category import Category
from myapp.models.product import Product
from myapp.tools.jmlmtools import colorify


class UserChoiceText:
    """
    User prompts and choices : numeric, text or list (via PyInquirer)
    """
    def __init__(self):
        pass

    def choice_prompt_numeric(self,message="Entrez votre choix : ",color='lightblue'):
        """
        prompt for user entry --> numeric answer
        :param message:
        :param color:
        :return: the category id or 0 if error
        """
        try:
            msg = colorify(message, [color])
            choix = int(input(msg))
            return choix
        except ValueError:
            return 999

    def choice_prompt_text(self, message="Entrez votre choix : ",color='lightblue'):
        """
        prompt for user entry --> string answer
        :param message:
        :param color:
        :return:
        """
        try:
            msg = colorify(message, [color])
            choix = str(input(msg))
            return choix
        except ValueError:
            return "999"

    def category_choice(self):
        """
        choose a category using PyInquirer list prompt
         - get all categories in database
         - put them into the list
         - prompt the user and catch the exception
        :return: the category id or 0 if error (no 0 category in database)
        """
        # get all categories
        category = Category()
        list_cat = category.list_categories()
        list_choices = []
        # building the display list
        for cat in list_cat:
            choice = "%02d - %s" % (cat[0], cat[1])
            list_choices.append(choice)
        list_choices.append(Separator())
        list_choices.append("00 - retour")
        question = [{'type': 'list',
                     'name': 'menu2',
                     'message': "Choisissez la catégorie du produit",
                     'choices': list_choices,
                     'carousel': True}, ]
        # prompt and return id or catch the error and return 0
        try:
            response = prompt(question, style=custom_style_1)
            ind = response['menu2'].split()
            rc = int(ind[0])
        except KeyError:
            rc = 0
        return rc

    def product_choice_bycat(self, idcategory):
        """
        choose a product using PyInquirer list choice
        get the fullname of the category
        get all products from the category in parameter
        put them into a list
        prompt the user to choose a product
        :param idcategory:
        :return:idproduct
        """
        #get category full name
        cat = Category()
        category = cat.get_category_byid(idcategory)
        msg = "Choisissez un produit de la catégorie %s " % category[1]
        # get all the products by the category
        product = Product()
        products = product.list_products_bycat(idcategory)
        # building the display list
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
        # prompt and return id or catch the error and return 0
        try:
            response = prompt(question, style=custom_style_1)
            ind = response['menu3'].split()
            rc = int(ind[0])
        except KeyError:
            rc = 0
        return rc
