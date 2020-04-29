# Created by jmlm at 08/04/2020-15:44 - P5
from __future__ import unicode_literals

from prettytable import PrettyTable

from myapp.tools.jmlmtools import clear, colorify, MyError
from myapp.controlers import userchoicetext
from myapp.models.category import Category
from myapp.models.store import Store
from myapp.models.product import Product
from myapp.models.bookmark import Bookmark

"""
All the display 
"""

class ConsoleView:
    """
    The consoleView class
    Attributes :
    lines for the differents menus
    Methods:
    Appli --> the main loop
    display_menuXX --> display each menu
    display_product_detail --> display a product detail
    all the method are loop which can be leaved by user only

    """
    def __init__(self):
        clear()
        self.ligne_sep2=colorify("------------", ['lightgreen'])
        self.ligne_sep1 = colorify("   ------------------------", ['cyan'])
        self.ligne_quitter= colorify("0 - ", ['lightgreen']) + colorify("Quitter", ['lightblue'])
        self.titre = colorify("P5 - Open Food Facts" ,['lightblue']) + " - "

    def appli(self):
        """
        the main loop
        to leave : 0 in the first menu
        :return:
        """
        loop = True
        while loop:
            choix_menu0 = 0
            choix_menu11  = 0
            choix_menu12 = 0
            choix_menu13 = 0
            choix_menu21 = 0
            choix_menu0 = self.display_menu0()
            if choix_menu0 == 0:
                loop = False
                continue
            elif choix_menu0 == 1:
                choix_menu11 = self.display_menu11()
                if choix_menu11 == 0 :
                   continue
                choix_menu12 = self.display_menu12(choix_menu11)
                if choix_menu12 == 0:
                    continue
                choix_menu13 = self.display_menu13(choix_menu12)
            else:
                choix_menu21 = self.display_menu21()

    def display_menu0(self):
        """
        display the 1st menu
        the input is treated by the specific class UserChoiceText()
        :return: choice 1 or 2 or 0 to leave the program
        """
        loop = True
        choix_menu = 0
        while loop:
            clear()
            print("")
            # The text.
            titre = self.titre + colorify("Menu",['lightyellow'])
            ligne1 = colorify("1 - ",['lightgreen']) + \
                     colorify("Retrouver un aliment dans une catégorie",['lightblue'])
            ligne2 = colorify("2 - ", ['lightgreen']) + \
                     colorify("Retouver les aliments substitués", ['lightblue'])
            if choix_menu == 999:
                ligneErreur = colorify('Erreur - vous devez entrer un choix valide !',['red'])
                print(ligneErreur)
            else:
                print("")
            print(titre)
            print(self.ligne_sep1)
            print(ligne1)
            print(ligne2)
            print(self.ligne_sep2)
            print(self.ligne_quitter)
            choix=userchoicetext.UserChoiceText()
            choix_menu = choix.choice_prompt_numeric("Entrez votre choix : ")
            if choix_menu in [0,1,2]:
                loop = False
                return choix_menu
            else:
                choix_menu = 999


    def display_menu11(self):
        """
        choose the category --> PyInquirer
        display and choice are treated by UserChoiceText() class
        :param self:
        :return: Category or 0 to go back
        """
        loop = True
        while loop:
            clear()
            print("")
            titre = self.titre + colorify(" Menu1.1",['lightyellow'])
            print(titre)
            print(self.ligne_sep1)
            choix = userchoicetext.UserChoiceText()
            cat = choix.category_choice()
            return cat


    def display_menu21(self):
        """
        choose the bookmark
        the chart is displayed by Prettytable
        user can choose a product to display details of the product itself and the bookmarks
            products
        :param self:
        :return:
        """
        loop = True
        while loop:
            clear()
            print("")
            titre = self.titre + colorify(" Menu2.1",['lightyellow'])
            print(titre)
            print(self.ligne_sep1)
            # build the chart
            print(colorify("\nCi-dessous les produits substitués avec le produit de "
                           "substition choisi : ",['lightblue']))
            bookmarkk = Bookmark()
            bookmarks = bookmarkk.get_all_bookmarks()
            x = PrettyTable()
            x.field_names = ['  Id  ', 'Libelle','---->' , 'Id subst', 'Libelle substitution' ]
            x.align['  Id  '] = 'r'
            x.align['Id subst'] = 'r'
            x.align['Libelle'] = "l"
            x.align['Libelle substitution'] = "l"
            list_products = []
            list_products2 = []
            for bookmark in bookmarks:
                ligne_tab=[]
                product = Product()
                prod = product.get_product_byid(bookmark[0])
                prod_subst = product.get_product_byid(bookmark[1])
                list_products.append(prod[0])
                list_products2.append((prod[0],prod_subst[0]))
                ligne_tab.append(prod[0])
                ligne_tab.append(prod[1])
                ligne_tab.append("---->")
                ligne_tab.append(prod_subst[0])
                ligne_tab.append(prod_subst[1])
                x.add_row(ligne_tab)
            print(x.get_string())
            # choose a product to display the details or 0 to go back
            print(colorify("Entrez l'id d'un produit pour obtenir son détail et le sdétails des produits "
                       "qui lui sont substituables (0 pour retour au menu)", ['lightblue']))
            choix = userchoicetext.UserChoiceText()
            id = choix.choice_prompt_numeric("Entrez votre choix : ")
            if id == 999:
                input(colorify("Erreur : Vous devez entrer un nombre (id) ou 0 pour retour"
                               " au menu - Appuyer sur Entrée pour continuer !", ["red"]))
                continue
            elif id == 0:
                loop = False
                continue
            if id not in list_products:
                input(colorify("Erreur : Vous devez entrer un nombre (id) présent dans la listes ci-dessus"
                               " - Appuyer sur Entrée pour continuer !", ["red"]))
                continue
            print(colorify("\nDetail du produit: ", ["lightyellow"]))
            # display details
            self.display_product_detail(prod)
            for list_subst in list_products2:
                if list_subst[0] == id:
                    ligne = colorify("\nDétail du bookmark :", ['lightmagenta'])
                    print(ligne)
                    product = Product()
                    prod = product.get_product_byid(list_subst[1])
                    self.display_product_detail(prod)
            input(colorify("\n\nAppuyer sur entrée pour continuer : ", ["lightcyan"]))



    def display_menu12(self, idcategory):
        """
        choose the product in category in parameter --> PyInquirer
        display and choice are treated by UserChoiceText() class
        :param idcategory:
        :return: product
        """
        loop = True
        while loop:
            clear()
            print("")
            titre = self.titre + colorify(" Menu1.2", ['lightyellow'])
            print(titre)
            print(self.ligne_sep1)
            choix=userchoicetext.UserChoiceText()
            prod = choix.product_choice_bycat(idcategory)
            return prod


    def display_menu13(self, idproduct):
        """
        display the detail of the product in parameter
        display a chart of products which have nutrisocre = or < to select them to be
        substitutes --> recorded as bookmarks
        :param idproduct:
        :return:
        """
        loop = True
        while loop:
            clear()
            print("")
            titre = self.titre + colorify(" Menu1.3", ['lightyellow'])
            print(titre)
            print(self.ligne_sep1)
            # get the product and its category and its stores
            product = Product()
            prod = product.get_product_byid(idproduct)
            cat = Category()
            category = cat.get_category_byid(prod[5])
            store = Store()
            stores = store.get_store_byproduct(idproduct)
            # display detail
            ligne = colorify("Vous avez selectionné le produit suivant :", ['lightcyan'])
            print(ligne)
            self.display_product_detail(prod,category,stores)
            # get substitutes
            subsitutes = product.get_product_bookmarks(idproduct)
            # get already defined bookmarks
            bookmark= Bookmark()
            bookmarks = [element[1] for element in bookmark.get_bookmark_byproduct(idproduct)]
            # building the display table of substitutes with prettytable
            if len(subsitutes):
                x = PrettyTable()
                x.field_names = ['Substitut','id','Libelle','URL','Score','Grade','categorie']
                x.align['Libelle'] = "l"
                x.align["Score"] = "r"
                list_products = []
                for subsitute in subsitutes:
                    subsitute=list(subsitute)
                    if subsitute[0] == idproduct:
                        continue
                    list_products.append(subsitute[0])
                    if subsitute[0] in bookmarks:
                        subsitute.insert(0, "0")
                        subsitute = [colorify(element,['green']) for element in subsitute]
                    else:
                        subsitute.insert(0,"N")
                    x.add_row(subsitute)
                # display chart
                ligne = colorify("\nCi-dessous les produits de substitution possibles "
                                 "- nutriscore inférieur ou égal - ",['lightcyan']) + \
                        colorify("(en vert les produits déjà mis en substitués/ookmarks) ",['green'])
                print(ligne)
                print(x.get_string(fields=['Substitut','id','Libelle','URL','Score','Grade'],reversort=True))
            # input the subsitutes id to be in bookmarks
            # choice are treated by UserChoiceText() class
            message = "Entrez les id des produits qui peuvent remplacer le produit choisi séparés par une " \
                      "virgule ','. Ils seront alors enregistrés dans la base (0 pour retour au menu) : "
            choice = userchoicetext.UserChoiceText()
            choix = choice.choice_prompt_text(message)
            if choix == '0':
                return 0
            liste_choix=choix.split(',')
            # treat the user input and the errors
            try:
                for choix in liste_choix:
                    if not choix.isdigit():
                        ligne = colorify("Erreur : Vous devez entrer des id de produits - Abandon "
                                         "du traitement",['red','bold'])
                        print(ligne)
                        raise MyError
                    else:
                        if int(choix) in list_products:
                            bookmark = Bookmark()
                            rc = bookmark.add_bookmark(idproduct,choix)
                            if rc[0] > 0:
                                print("%s" % rc[1])
                                ligne = colorify(f"Erreur : Echec création bookmark "
                                                 f"{idproduct} {choix}", ['red'])
                                print(ligne)
                                raise MyError
                            else:
                                ligne = colorify(f"Création bookmark {idproduct}-{choix} OK !"
                                                 , ['lightgreen'])
                                print(ligne)
                        else:
                            ligne = colorify(f"Erreur le produit {choix} n'est pas dans la liste"
                                             f"des produits de substitution --> Abandon de ce choix !\n"
                                             f"Appuyer sur entrée pour continuer !",['red'])
                            print(ligne)
                            input("")

            except MyError:
                input (colorify("Abandon du traitement - Appuyer sure entrée pour continuer",['red']))
                continue
            input(colorify("Appuyer sur entrée pour continuer",['lightgreen']))
            # return 0


    def display_product_detail(self,prod,category=None,stores=None):
        """
        Display the detail of the product with its category and stores
        :param prod:
        :param category:
        :param stores:
        :return:
        """
        # to get the category id and the stres id if not specified
        if category is None:
            cat = Category()
            category = cat.get_category_byid(prod[5])
        if stores is None:
            store = Store()
            stores = store.get_store_byproduct(prod[0])
    # display
        ligne = colorify("Produit : ", ['lightcyan']) + \
                colorify(prod[1], ['white']) + " - " + \
                colorify("  Catégorie : ", ['lightcyan']) + \
                colorify(category[1], ['white'])
        print(ligne)
        ligne = colorify("Score Nutriscore : ", ['lightcyan']) + \
                colorify(str(prod[3]), ['white']) + " - " + \
                colorify("  Score Grade : ", ['lightcyan']) + \
                colorify(prod[4], ['white'])
        print(ligne)
        ligne = colorify("URL : ", ["lightcyan"]) + colorify(prod[2], ['white'])
        print(ligne)
        if len(stores) > 1:
            mag = "Magasins : "
        else:
            mag = "Magasin : "
        ligne = colorify(mag, ['lightcyan'])
        for stor in stores:
            ligne += colorify(stor[0], ['white'])
            ligne += " - "
        print(ligne)