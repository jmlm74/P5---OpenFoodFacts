# Created by jmlm at 08/04/2020-15:44 - P5
from __future__ import unicode_literals

from prompt_toolkit.shortcuts import print_tokens
from pygments.token import Token
import PyInquirer

from myapp.setup import *
from myapp.tools import jmlmtools
from myapp.controlers import userchoicetext
from myapp.models.category import Category



# The style sheet.
"""
style = style_from_dict({
    Token.vert: '#15ce47',
    Token.vertf: '#50FC00',
    Token.rouge: '#ff0000',
    Token.jaune: '#edfc00',
    Token.bleuc: '#00fce9',
    Token.bleu: '#00a8fc',
    Token.bleue: '#004cfc',
    Token.mauve: '#0400fc',
    Token.rose: '#fc00f8',
    Token.blanc: '#ffffff'
})
"""



class console_view:
    """

    """
    def __init__(self):
        jmlmtools.clear()
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
            jmlmtools.clear()
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
            jmlmtools.clear()
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
            jmlmtools.clear()
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
            jmlmtools.clear()
            print("")
            titre = [(Token.Blue, " P5 - Open Food Facts "),
                    (Token, '-'),
                    (Token.Yellow, " Menu4"),(Token, "\n")]
            print_tokens(titre, style=style)
            print_tokens(self.ligneSep1, style=style)
            choix = userchoicetext.UserChoiceText()
            prod = choix.product_substitut(idproduct)
            # print(prod)
            cat = Category()
            category = cat.get_category(prod[5])
            # print(category)
            ligne = [(Token.Turquoise,"Vous avez selectionné les produits suivant :"),
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
            
            "Select storeName from T_Products_stores as T  inner join T_Products as P " \
            " on P.idProduct=T.idProduct inner join T_Stores as S on T.idStore = S.idStore " \
            "where P.idProduct = 154;"

            input('toto')

            return 0