#!/usr/bin/python3
""" script that takes in arguments and displays all values in the
states table of hbtn_0e_0_usa where name matches the argument.
SQL Injection"""
import MySQLdb
import sys

if __name__ == "__main__":
    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    c = db.cursor()
    q = "SELECT * FROM states WHERE name = %s"
    v = sys.argv[4]
    c.execute(q, (v,))
    [print(i) for i in c if i[1] == sys.argv[4]]
