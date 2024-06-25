#!/usr/bin/python3
"""
"""
import sys
import MySQLdb

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    database_name = sys.argv[3]

    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=database_name
    )

    mycursor = db.cursor()
    query = "SELECT cities.id, cities.name, states.id\
        FROM cities JOIN states On cities.state_id = states.id\
            ORDER BY cities.id ASC"
    
    mycursor.execute(query)
    rows = mycursor.fetchall()
    for row in rows:
        print(row)