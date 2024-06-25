#!/usr/bin/python3
"""
This script lists all cities from the database hbtn_0e_4_usa.
"""
import sys
import MySQLdb

if __name__ == "__main__":
    # Get MySQL username, password, and database name from command line
    # arguments
    username = sys.argv[1]
    password = sys.argv[2]
    database_name = sys.argv[3]

    # Connect to the MySQL database
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=database_name
    )

    mycursor = db.cursor()
    query = """
    SELECT cities.id, cities.name, states.name
    FROM cities
    JOIN states ON cities.state_id = states.id
    ORDER BY cities.id ASC
    """
    mycursor.execute(query)
    rows = mycursor.fetchall()
    for row in rows:
        print(row)

    mycursor.close()
    db.close()
