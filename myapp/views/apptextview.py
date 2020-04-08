# Created by jmlm at 08/04/2020-15:44 - P5
from __future__ import unicode_literals
from myapp.tools import jmlmtools
from prompt_toolkit import prompt
from prompt_toolkit.formatted_text import FormattedText
from prompt_toolkit import print_formatted_text
from prompt_toolkit.styles import Style
from myapp.controlers import choicetext

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


class consoleview:
    """

    """
    def __init__(self):
        self.choixMenu1 = 0
        pass


    def displayMenu1(self):
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
            ligne = FormattedText([('class:bleu bold','   ------------------------')])
            ligne1 = FormattedText([('class:vertf','1 - '),
                                    ('class:bleue', 'Remplacer un aliment')])
            ligne2 = FormattedText([('class:vertf', '2 - '),
                                    ('class:bleue', 'Retouver les aliments substitués')])
            lignesep = FormattedText([('class:vertf', '------------')])
            ligne3 = FormattedText([('class:vertf', '0 - '),
                                    ('class:bleue', 'Quitter')])
            if choixMenu == 999:
                ligneErreur = FormattedText([('class:rouge bold blink',"Erreur - vous devez entrer un choix valide !")])
                print_formatted_text(ligneErreur)
            else:
                print("")
            print_formatted_text(titre, style=style)
            print_formatted_text(ligne,style=style)
            print_formatted_text(ligne1, style=style)
            print_formatted_text(ligne2, style=style)
            print_formatted_text(lignesep, style=style)
            print_formatted_text(ligne3, style=style)
            choix=choicetext.choicetext()
            choixMenu = choix.choice_promptN()
            if choixMenu == 0:
                loop = False
            elif choixMenu not in [0,1,2]:
                choixMenu = 999

