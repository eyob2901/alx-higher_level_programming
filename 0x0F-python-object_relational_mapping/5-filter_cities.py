#!/usr/bin/python3
"""  script that takes in the name of a state as an argument and
lists all cities of that state,"""
import MySQLdb
import sys

if __name__ == "__main__":
    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    c = db.cursor()
    q = """SELECT cities.name FROM cities join states
    on state_id = states.id where states.name = %s"""
    v = sys.argv[4]
    c.execute(q, (v,))
    v = [','.join(i) for i in c]
    print(', '.join(v))
