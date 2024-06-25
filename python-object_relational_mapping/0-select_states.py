#!/usr/bin/python3
"""
"""
import MySQLdb
import sys

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    database_name = sys.argv[3]

db = MySQLdb.connect(host="localhost", port=3306, user=username, passwd=password, db=database_name)
cur = db.cursor()
cur.execute("SELECT id, name FROM states ORDER BY id ASC")

rows = cur.fetchall()
for row in rows:
    print(row)

cur.close()
db.close

