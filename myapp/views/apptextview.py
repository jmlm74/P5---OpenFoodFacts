# Created by jmlm at 08/04/2020-15:44 - P5
from __future__ import unicode_literals

from prompt_toolkit.shortcuts import print_tokens

from prettytable import PrettyTable

from myapp.setup import *
from myapp.tools.jmlmtools import clear, colorify
from myapp.controlers import userchoicetext
from myapp.models.category import Category
from myapp.models.store import Store
from myapp.models.product import Product
from myapp.models.bookmark import Bookmark




# The style sheet.
#Color



class console_view:
    """

    """
    def __init__(self):
        clear()
        self.ligneSep2 =[(Token.Green, '------------'),(Token, "\n")]
        self.ligneSep1 = [(Token.Teal, '   ------------------------'),(Token, "\n")]
        self.ligneQuitter = [(Token.Green, '0 - '),
                            (Token.Blue, 'Quitter'),(Token, "\n")]

    def appli(self):
        loop = True
        while loop:
            choix_menu1 = 0
            choix_menu2  = 0
            choix_menu3 = 0
            choix_menu4 = 0
            choix_menu1 = self.display_menu1()
            if choix_menu1 == 0:
                loop = False
                continue
            if choix_menu1 == 1:
                choix_menu2 = self.display_menu2()
                if choix_menu2 == 0 :
                   continue
                choix_menu3 = self.display_menu3(choix_menu2)
                if choix_menu3 == 0:
                    continue
                choix_menu4 = self.display_menu4(choix_menu3)

    def display_menu1(self):
        loop = True
        choixMenu = 0
        while loop:
            clear()
            print("")
            # The text.
            titre = [(Token.Blue," P5 - Open Food Facts "),
                    (Token,'-'),
                    (Token.Yellow," Menu1"),(Token, "\n")]
            ligne1 = [(Token.Green,'1 - '),
                    (Token.Blue, 'Retrouver un aliment dans une catégorie'),(Token, "\n")]
            ligne2 = [(Token.Green, '2 - '),
                    (Token.Blue, 'Retouver les aliments substitués'),(Token, "\n")]
            if choixMenu == 999:
                ligneErreur = [(Token.Red,"Erreur - vous devez entrer un choix valide !"),
                               (Token, "\n")]
                print_tokens(ligneErreur,style=style)
            else:
                print("")
            print_tokens(titre, style=style)
            print_tokens(self.ligneSep1,style=style)
            print_tokens(ligne1, style=style)
            print_tokens(ligne2, style=style)
            print_tokens(self.ligneSep2, style=style)
            print_tokens(self.ligneQuitter, style=style)
            choix=userchoicetext.UserChoiceText()
            choixMenu = choix.choice_prompt_numeric()
            if choixMenu in [0,1]:
                loop = False
                return choixMenu
            elif choixMenu not in [0,1,2]:
                choixMenu = 999


    def display_menu2(self):
        """

        :param self:
        :return:
        """
        loop = True
        choixMenu = 0
        while loop:
            clear()
            print("")
            titre = [(Token.Blue," P5 - Open Food Facts "),
                    (Token,'-'),
                    (Token.Yellow," Menu2"),(Token, "\n")]
            print_tokens(titre, style=style)
            print_tokens(self.ligneSep1,style=style)
            choix = userchoicetext.UserChoiceText()
            cat = choix.category_choice()
            return cat

    def display_menu3(self,idcategory):
        """

        :param category:
        :return:
        """
        loop = True
        while loop:
            clear()
            print("")
            titre = [(Token.Blue, " P5 - Open Food Facts "),
                    (Token, '-'),
                    (Token.Yellow, " Menu3"),(Token, "\n")]
            print_tokens(titre, style=style)
            print_tokens(self.ligneSep1, style=style)
            choix=userchoicetext.UserChoiceText()
            prod = choix.product_choice_bycat(idcategory)
            return prod


    def display_menu4(self,idproduct):
        """
        :param product:
        :return:
        """
        loop = True
        while loop:
            clear()
            print("")
            titre = [(Token.Blue, " P5 - Open Food Facts "),
                    (Token, '-'),
                    (Token.Yellow, " Menu4"),(Token, "\n")]
            print_tokens(titre, style=style)
            print_tokens(self.ligneSep1, style=style)
            product = Product()
            prod = product.get_product_byid(idproduct)
            cat = Category()
            category = cat.get_category_byid(prod[5])
            ligne = [(Token.Turquoise,"Vous avez selectionné le produit suivant :"),
                     (Token, "\n")]
            print_tokens(ligne,style=style)
            print("")
            ligne = [(Token.Turquoise,"Produit : "),
                     (Token.White,prod[1]),
                     (Token, '-'),
                     (Token.Turquoise, "  Catégorie : "),
                     (Token.White, category[1]),
                     (Token, "\n")]
            print_tokens(ligne, style=style)
            ligne = [(Token.Turquoise,"Score Nutriscore : "),
                     (Token.White,str(prod[3])),
                     (Token, '-'),
                     (Token.Turquoise,"  Score Grade : "),
                     (Token.White,prod[4]),
                     (Token, "\n")]
            print_tokens(ligne, style=style)
            ligne = [(Token.Turquoise, "URL : "),
                     (Token.White, prod[2]),
                     (Token, "\n")]
            print_tokens(ligne, style=style)
            store = Store()
            stores = store.get_store_byproduct(idproduct)
            if len(stores) > 1:
                mag = "Magasins : "
                sup1 = True
            else:
                mag = "Magasin : "
                sup1 = False
            ligne = [(Token.Turquoise,mag)]
            for stor in stores:
                ligne.append((Token.White,stor[0]))
                ligne.append((Token," - "))
            ligne.append((Token,"\n"))
            print_tokens(ligne, style=style)
            subsitutes = product.get_product_bookmarks(idproduct)
            bookmark= Bookmark()
            #bookmarks = bookmark.get_bookmark_byproduct(idproduct)
            bookmarks = [element[1] for element in bookmark.get_bookmark_byproduct(idproduct)]
            # print(bookmarkss)
            if len(subsitutes):
                x = PrettyTable()
                x.field_names = ['Substitut','id','Libelle','URL','Score','Grade','categorie']
                x.align['Libelle'] = "l"
                x.align["Score"] = "r"
                list_products = []
                for subsitute in subsitutes:
                    lignetab = []
                    if subsitute[0] == idproduct:
                        continue
                    list_products.append(subsitute[0])
                    if subsitute[0] in bookmarks:
                        lignetab.append('O')
                        lignetab.extend(subsitute)
                        lignetab = [colorify(element,['red']) for element in lignetab]
                    else:
                        lignetab.append("N")
                        lignetab.extend(subsitute)
                    x.add_row(lignetab)
                ligne = [(Token,"\n"),
                         (Token.Turquoise,"Ci-dessous les produits de substitution possibles "
                                          "- nutriscore inférieur ou égal - "),
                         (Token.DarkRed,"(en rouge les produits déjà mis en substitués/favoris) "),
                         (Token,"\n")]
                print_tokens(ligne,style=style)
                print(x.get_string(fields=['Substitut','id','Libelle','URL','Score','Grade'],reversort=True))
            message = "Entrez les id des produits qui peuvent remplacer le produit choisi séparés par une " \
                      "virgule ','. Ils seront alors enregistrés dans la base (0 pour retour au menu) : "
            choice = userchoicetext.UserChoiceText()
            choix = choice.choice_prompt_text(message)
            if choix == '0':
                return 0
            listechoix=choix.split(',')
            for choix in listechoix:
                if not choix.isdigit():
                    ligne = colorify("Erreur : Vous devez entrer des id de produits - Abandon "
                                     "du traitement - Appuyer sur entrée pour continuer",['red','bold'])
                    print(ligne)
                    input()
                    loop = False
                else:
                    input('toto')
                    return 0