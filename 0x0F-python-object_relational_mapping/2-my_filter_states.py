#!/usr/bin/python3
"""
Script to display all rows of states table
where name matches argument
"""

import MySQLdb
from sys import argv

if __name__ == '__main__':

    db = MySQLdb.connect(
        host="localhost", user=argv[1], port=3306, passwd=argv[2], db=argv[3])

    cur = db.cursor()

    cur.execute("SELECT * FROM states \
        WHERE name LIKE BINARY '{}' ORDER BY states.id ASC".format(argv[4]))

    rows = cur.fetchall()

    for row in rows:
        print(row)
