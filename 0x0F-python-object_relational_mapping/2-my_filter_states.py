#!/usr/bin/python3
"""
this is a module
"""

import MySQLdb as driver
from sys import argv

if __name__ == '__main__':
    """
    the main
    """
    db_ = driver.connect(
        host="localhost", user=argv[1], passwd=argv[2],
        db=argv[3], port=3306)
    # cursor object created to interact with the database
    cursor = db_.cursor()
    # Execute a simple SELECT query
    query = "SELECT * FROM states WHERE name LIKE BINARY '{}' \
            ORDER BY id ASC".format(argv[4])
    cursor.execute(query)
    # Fetch and print the results
    states = cursor.fetchall()
    for row in states:
        print(row)

    # Close the cursor and the database connection
    cursor.close()
    db_.close()
