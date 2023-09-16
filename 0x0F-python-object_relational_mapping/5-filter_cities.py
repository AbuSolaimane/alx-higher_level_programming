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
    query = "SELECT c.name FROM \
            cities c JOIN states s ON \
            c.state_id = s.id WHERE s.name \
            LIKE BINARY %(name_s)s ORDER BY c.id ASC"
    cursor.execute(query, {'name_s': argv[4]})
    # Fetch and print the results
    states = cursor.fetchall()
    print(", ".join([row[0] for row in states]))

    # Close the cursor and the database connection
    cursor.close()
    db_.close()
