# coding:utf-8

import MySQLdb
from config.database import *


class DbHelper:
    def __init__(self):
        self.host = HOST
        self.port = PORT
        self.user = USER
        self.passwd = PASSWORD
        self.db = DATABASE
        self.charset = CHARSET
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
