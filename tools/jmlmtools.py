# Created by jmlm at 31/03/2020-17:01
import platform, os
import argparse


"""
mes imports a moi que j'ai
"""

def clear():
    """
    It does his name : clearscreen (can't test on Mac) --> StackoverFlow
    """
    if platform.system() == "Windows":
        os.system("cls")
    else:
        print("\033c", end="")


class SmartFormatter(argparse.HelpFormatter):
    """
    \n in help text for argparse = newline
    just start your help text with R|
    """
    def _split_lines(self, text, width):
        if text.startswith('R|'):
            return text[2:].splitlines()
        # this is the RawTextHelpFormatter._split_lines
        return argparse.HelpFormatter._split_lines(self, text, width)


def parse_arguments():
    """
    return parsed agrs --> treated by the caller
    """
    parser = argparse.ArgumentParser(formatter_class=SmartFormatter)
    parser.add_argument("-d", '--db', choices=['test','create'],help="R|'test' to test database \n"
                                    "'create' to fill the database. The tables will be automatically dropped and recreated ")
    return parser.parse_args()