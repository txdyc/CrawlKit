# coding:utf-8

import MySQLdb
from config import database


class DbHelper:
    def __init__(self):
        self.host = database.HOST
        self.port = database.PORT
        self.user = database.USER
        self.passwd = database.PASSWORD
        self.db = database.DATABASE
        self.charset = database.CHARSET
        self.connection = None

    def conn(self):
        if not self.connection:
            self.connection = MySQLdb.connect(host=self.host,
                                              port=self.port,
                                              user=self.user,
                                              passwd=self.passwd,
                                              db=self.db,
                                              charset=self.charset)
        return self.connection
