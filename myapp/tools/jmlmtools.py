# Created by jmlm at 31/03/2020-17:01
import platform, os
import argparse
import time
from myapp.setup import *
import mysql.connector
from mysql.connector import Error


"""
mes imports a moi que j'ai !
tools I use frecquently
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
    dont't forget the formatter
    """
    parser = argparse.ArgumentParser(formatter_class=SmartFormatter)
    parser.add_argument("-d", '--db', choices=['test','create'],help="R|'test' to test database \n"
                                    "'create' to fill the database. The tables will be automatically dropped and recreated ")
    return parser.parse_args()


def jmlm_now():
    """
    to have a sql now() timestamp
    :return: sql timestamp
    """
    now = time.strftime('%Y-%m-%d %H-%M-%S')
    return now

def get_env():
    """
    getenv --> help in debug
    :return:
    """
    import sys
    print("fichier : ",__file__)
    print("package : ",__package__)
    print("curdir : ",os.getcwd())
    print("syspath : ",sys.path)



"""
the color output in console
"""
COLOR_STYLES = {
    # styles
    'bold':         ['\033[1m',  '\033[0m'],
    'dim':          ['\033[2m',  '\033[22m'],
    'italic':       ['\033[3m',  '\033[23m'],
    'underline':    ['\033[4m',  '\033[24m'],
    'blink' :       ['\033[5m',  '\033[22m'],
    'inverse':      ['\033[7m',  '\033[27m'],
    'hidden':       ['\033[8m',  '\033[28m'],
    # colors
    'resetc':       ['\033[39m'],
    'black':        ['\033[30m', '\033[39m'],
    'red':          ['\033[31m', '\033[39m'],
    'green':        ['\033[32m', '\033[39m'],
    'yellow':       ['\033[33m', '\033[39m'],
    'blue':         ['\033[34m', '\033[39m'],
    'magenta':      ['\033[35m', '\033[39m'],
    'cyan':         ['\033[36m', '\033[39m'],
    'lightgrey':    ['\033[37m', '\033[39m'],
    'darkgrey':     ['\033[90m', '\033[39m'],
    'lightred':     ['\033[91m', '\033[39m'],
    'lightgreen':   ['\033[92m', '\033[39m'],
    'lightyellow':  ['\033[93m', '\033[39m'],
    'lightblue':    ['\033[94m', '\033[39m'],
    'lightmagenta': ['\033[95m', '\033[39m'],
    'lightcyan':    ['\033[96m', '\033[39m'],
    'white':        ['\033[97m', '\033[39m'],
    #backgrounds
    'bgreset':      ['\033[49m'],
    'bgblack':      ['\033[40m', '\033[49m'],
    'bgred':        ['\033[41m', '\033[49m'],
    'bggreen':      ['\033[42m', '\033[49m'],
    'bgyellow':     ['\033[43m', '\033[49m'],
    'bgblue':       ['\033[44m', '\033[49m'],
    'bgmagenta':    ['\033[45m', '\033[49m'],
    'bgcyan':       ['\033[46m', '\033[49m'],
    'bglightgrey':  ['\033[47m', '\033[49m'],
    'bgdarkgrey':   ['\033[100m', '\033[49m'],
    'bglightred':   ['\033[101m', '\033[49m'],
    'bglightgreen': ['\033[102m', '\033[49m'],
    'bglightyellow':['\033[103m', '\033[49m'],
    'bglightblue':  ['\033[104m', '\033[49m'],
    'bglightmagenta':['\033[105m', '\033[49m'],
    'bglightcyan':  ['\033[106m', '\033[49m'],
    'bgwhite':      ['\033[107m', '\033[49m'],

}

def colorify(text, colors):
    """Prefix and suffix text to render terminal color"""
    for color in colors:
        style = COLOR_STYLES[color]
        text = '{}{}{}'.format(style[0], text, style[1])
    return text


class MyError(Exception):
    """
    just used for the try/except !
    """
    pass


class database_connect:
    """
    class database_connect --> to use the database : connect close and orders
    """
    __db = None
    __host = None
    __user = None
    __pw = None
    __cursor = None
    __connex = None

    def __init__(self) -> object:
        """
        init the database connection
        """
        self.__db = DBNAME
        self.__user = DBUSER
        self.__pw = DBPW
        self.__host = DBHOST

    def __enter__(self):
        """
        called by with statement
        :return: cursor
        """
        return self.connect_db()

    def  __exit__(self, type, value, traceback):
        """
        called by the end of the with statement
        return: None
        """
        return self.disconnect_db()

    def commit(self):
        """
        commit transaction
        :return:
        """
        self.__connex.commit()

    def rollback(self):
        """
        Rollback transaction
        :return:
        """
        self.__connex.rollback()

    def connect_db(self):
        """
        connect to database an open cursor
        :return: cursor
        """
        try:
            cnx = mysql.connector.connect(host=self.__host,
                                          database = self.__db,
                                          user = self.__user,
                                          password = self.__pw)
            curs = cnx.cursor(buffered=True)
            self.__cursor = curs
            self.__connex = cnx
        except Error as e:
            print("Erreur de connexion : %s" % e.msg)
            return 0
        # print('OK')
        return self.__cursor

    def disconnect_db(self):
        """
        disconnect connection to database
        Close cursor and database connection
        :return:
        """
        self.__cursor.close()
        self.__connex.close()