#!/usr/bin/python3
""" ists all states with a name starting with N
(upper N) from the database hbtn_0e_0_usa: """

import MySQLdb
import sys

if __name__ == "__main__":
    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    c = db.cursor()
    q = "SELECT * FROM states WHERE name = '{}'".format(sys.argv[4])
    c.execute(q)
    [print(i) for i in c if i[1] == sys.argv[4]]
