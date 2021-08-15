import sqlite3
from sqlite3 import Error
from sqlite3.dbapi2 import connect

def ConnectDBSQLite():
    return connect('SysFinanCtrl.db')