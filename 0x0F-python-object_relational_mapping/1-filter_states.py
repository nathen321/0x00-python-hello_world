#!/usr/bin/python3

from sys import argv
import MySQLdb

if __name__ == "__main__":
    db = MySQLdb.connect(user=argv[1], passwd=argv[2], db=argv[3])
    cur = db.cursor()
    cur.execute("SELECT * FROM `states` ORDER BY `id`")
    rows = cur.fetchall()
    [print(state) for state in rows if state[1][0] == 'N']
