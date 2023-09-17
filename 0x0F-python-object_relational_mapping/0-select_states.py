#!/usr/bin/python3
"""
This script lists all states from the
database `hbtn_0e_0_usa`.
"""

import MySQLdb
from sys import argv

if __name__ == '__main__':
    # Check if correct number of arguments is provided
    if len(argv) != 4:
        print("Usage: {} <username> <password> <database>".format(argv[0]))
        exit(1)

    username, password, database = argv[1], argv[2], argv[3]

    try:
        # Connect to the MySQL server
        db = MySQLdb.connect(
                host="localhost",
                user=username,
                port=3306,
                passwd=password,
                db=database
                )

        # Create a cursor object
        cur = db.cursor()

        # Execute the query to select all states and order by states.id
        cur.execute("SELECT * FROM states ORDER BY states.id")

        # Fetch all rows
        rows = cur.fetchall()

        # Print the rows
        for row in rows:
            print(row)

        # Close cursor and database connection
        cur.close()
        db.close()

    except MySQLdb.Error as e:
        print("MySQL Error: {}".format(e))
