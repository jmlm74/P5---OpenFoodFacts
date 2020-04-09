# Created by jmlm at 31/03/2020-17:01
import platform, os
import argparse
import time
from myapp.setup import *
import mysql.connector
from mysql.connector import Error


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


def jmlm_now():
    now = time.strftime('%Y-%m-%d %H-%M-%S')
    return now

def get_env():
    import sys
    print("fichier : ",__file__)
    print("package : ",__package__)
    print("curdir : ",os.getcwd())
    print("syspath : ",sys.path)



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