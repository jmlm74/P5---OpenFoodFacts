# Created by jmlm at 08/04/2020-19:15 - P5
from prompt_toolkit.validation import Validator, ValidationError
from prompt_toolkit import prompt
from prompt_toolkit.styles import Style

from myapp.models.category import Category
from myapp.models.product import Product

import inquirer

# The style sheet.
style = Style.from_dict({
    'vert': '#15ce47',
    'vertf': '#50FC00',
    'rouge': '#ff0000',
    'jaune': '#edfc00',
    'bleuc': '#00fce9',
    'bleu': '#00a8fc',
    'bleue': '#004cfc',
    'mauve': '#0400fc',
    'rose': '#fc00f8',
    'blanc': '#ffffff'
})


class UserChoiceText:

    def __init__(self):
        self.__choixN = 0
        self.__choixT = ""

    def choice_prompt_numeric(self):
        try:
            # self.choixN = int(prompt("Entrez votre choix : ",validator = self.NumberValidation()))
            message = [('class:bleuc italic',"Entrez votre choix : ")]
            self.__choixN = int(prompt((message),style=style))
            return self.__choixN
        except ValueError:
            return 999

    def category_choice(self):
        category = Category()
        listCat = category.list_categories()
        list_choices = []
        for cat in listCat:
            choice = "%02d - %s" % (cat[0], cat[1])
            list_choices.append(choice)
        list_choices.append("   -----------")
        list_choices.append("00 - retour")
        question = [inquirer.List('menu2',
                                  message="Choisissez la catégorie du produit",
                                  choices=list_choices,
                                  carousel=True)]
        response = inquirer.prompt(question)
        if not response['menu2'][:2].isdigit():
            rc = 99
        else:
            rc = int(response['menu2'][:2])
        return rc

    def product_choice_bycat(self,idcategory):
        cat = Category()
        category = cat.get_category(idcategory)
        msg = "Choisissez un produit de la catégorie %s " % category[1]
        product = Product()
        products = product.list_products_bycat(idcategory)
        list_products=[]
        for prod in products:
            choice = "%02d - %s" % (prod[0],prod[1])
            list_products.append(choice)
        list_products.append("   -----------")
        list_products.append("00 - retour")
        question = [inquirer.List('menu3',
                                  message=msg,
                                  choices=list_products,
                                  carousel=True)]
        response = inquirer.prompt(question)