# Created by jmlm at 08/04/2020-15:44 - P5
from __future__ import unicode_literals

from prompt_toolkit.formatted_text import FormattedText
from prompt_toolkit import print_formatted_text
from prompt_toolkit.styles import Style

from myapp.tools import jmlmtools
from myapp.controlers import userchoicetext
from myapp.models.category import Category

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


class console_view:
    """

    """
    def __init__(self):
        jmlmtools.clear()
        self.ligneSep2 = FormattedText([('class:vertf', '------------')])
        self.ligneSep1 = FormattedText([('class:bleu bold', '   ------------------------')])
        self.ligneQuitter = FormattedText([('class:vertf', '0 - '),
                                ('class:bleue', 'Quitter')])

    def appli(self):
        loop = True
        while loop:
            choix_menu1 = 0
            choix_menu2  = 0
            choix_menu3 = 0
            choix_menu1 = self.display_menu1()
            if choix_menu1 == 0:
                loop = False
                continue
            if choix_menu1 == 1:
                choix_menu2 = self.display_menu2()
                if choix_menu2 == 0 :
                   continue
                else:
                    print("On va choisir un produit de la categorie %d " % choix_menu2)
                    input("titi")
                    choix_menu3 = self.display_menu3(choix_menu2)
                    print("retour menu3 %d " % choix_menu3)
                    input("toto")

    def display_menu1(self):
        loop = True
        choixMenu = 0
        while loop:
            jmlmtools.clear()
            print("")
            # The text.
            titre = FormattedText([('class:bleu bold'," P5 - Open Food Facts "),
                                   ('','-'),
                                   ('class:jaune'," Menu1")
                                    ])
            ligne1 = FormattedText([('class:vertf','1 - '),
                                    ('class:bleue', 'Retrouver un aliment dans une catégorie')])
            ligne2 = FormattedText([('class:vertf', '2 - '),
                                    ('class:bleue', 'Retouver les aliments substitués')])
            if choixMenu == 999:
                ligneErreur = FormattedText([('class:rouge bold blink',"Erreur - vous devez entrer un choix valide !")])
                print_formatted_text(ligneErreur)
            else:
                print("")
            print_formatted_text(titre, style=style)
            print_formatted_text(self.ligneSep1,style=style)
            print_formatted_text(ligne1, style=style)
            print_formatted_text(ligne2, style=style)
            print_formatted_text(self.ligneSep2, style=style)
            print_formatted_text(self.ligneQuitter, style=style)
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
            titre = FormattedText([('class:bleu bold'," P5 - Open Food Facts "),
                                   ('','-'),
                                   ('class:jaune'," Menu2")
                                    ])
            print_formatted_text(titre, style=style)
            print_formatted_text(self.ligneSep1,style=style)
            choix = userchoicetext.UserChoiceText()
            cat = choix.category_choice()
            if cat == 99:
                loop = True
            else:
                loop = False
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
            titre = FormattedText([('class:bleu bold', " P5 - Open Food Facts "),
                                   ('', '-'),
                                   ('class:jaune', " Menu3")
                                   ])
            print_formatted_text(titre, style=style)
            print_formatted_text(self.ligneSep1, style=style)
            choix=userchoicetext.UserChoiceText()
            prod = choix.product_choice_bycat(idcategory)

            return 0


