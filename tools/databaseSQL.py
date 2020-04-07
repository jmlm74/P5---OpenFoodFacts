# Created by jmlm at 30/03/2020-22:53 - testP5
from setup import DBNAME,DBUSER,DBHOST,DBPW
import mysql.connector
from mysql.connector import Error
"""
class databaseSQL --> to use the database : connect close and orders
"""

class databaseConnect:
    """
    class databaseSQL --> to use the database : connect close and orders
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