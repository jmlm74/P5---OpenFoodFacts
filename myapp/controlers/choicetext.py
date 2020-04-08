# Created by jmlm at 08/04/2020-19:15 - P5
from prompt_toolkit.validation import Validator, ValidationError
from prompt_toolkit import prompt
from prompt_toolkit.styles import Style

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


class choicetext:

    def __init__(self):
        self.choixN = 0
        self.choixT = ""

    def choice_promptN(self):
        try:
            # self.choixN = int(prompt("Entrez votre choix : ",validator = self.NumberValidation()))
            message = [('class:bleuc italic',"Entrez votre choix : ")]
            self.choixN = int(prompt((message),style=style))
            return self.choixN
        except ValueError:
            return 999