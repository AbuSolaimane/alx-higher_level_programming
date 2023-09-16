from MySQLdb import _mysql as driver
from sys import argv

if __name__ == '__main__':
    db = driver.(host="localhost", user=argv[1], password=argv[2],
            database=argv[3], port=3306);
    # cursor object created to interact with the database
    cursor = db.cursor();

    # Execute a simple SELECT query
    query = "SELECT * FROM states ORDER BY id ASC";
    cursor.execute(query)
    
    # Fetch and print the results
    states = cursor.fetchall()
    for row in states:
        print(row)

    # Close the cursor and the database connection
    cursor.close()
    connection.close()
