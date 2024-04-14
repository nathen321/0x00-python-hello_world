#!/usr/bin/python3
"""
Write a script that takes in an argument and displays all values
"""
import MySQLdb
from sys import argv

# The code should not be executed when imported
if __name__ == '__main__':
    # make a connection to the database
    db = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                         passwd=argv[2], db=argv[3])

    # It gives us the ability to have multiple seperate working environments
    # through the same connection to the database.
    cur = db.cursor()

    cur.execute(
            "SELECT cities.id, cities.name FROM cities\
                INNER JOIN states ON cities.state_id = states.id\
                WHERE states.name = %s", [argv[4]])

    rows = cur.fetchall()
    liste = [cti[1] for cti in rows]
    print(", ".join(liste))
    # Clean up process
    cur.close()
    db.close()
