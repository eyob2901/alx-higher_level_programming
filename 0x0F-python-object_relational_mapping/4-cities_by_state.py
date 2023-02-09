#!/usr/bin/python3
""" script that lists all cities from the database hbtn_0e_4_usa """

import sys
import MySQLdb

if __name__ == '__main__':
    con = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    cur = con.cursor()
    q = """select cities.id, cities.name, states.name
    from cities join states on state_id = states.id Order by cities.id"""
    cur.execute(q)
    for i in cur.fetchall():
        print(i)
