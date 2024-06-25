#!/usr/bin/python3
"""
A script that lists all states with a name starting with N (upper N)
from the database hbtn_0e_0_usa.

Arguments:
    mysql username (str) : argv[1]
    mysql password (str) : argv[2]
    database name (str) : argv[3]

"""
import sys
import MySQLdb

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    database_name = sys.argv[3]

    db = MySQLdb.connect(host="localhost",
                         port=3306,
                         user=username,
                         passwd=password,
                         db=database_name)

    cur = db.cursor()
    cur.execute("SELECT * FROM states WHERE name LIKE 'N%' ORDER BY id ASC")

    rows = cur.fetchall()
    for row in rows:
        print(row)

    cur.close()
    db.close()