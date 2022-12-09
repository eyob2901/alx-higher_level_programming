#!/usr/bin/python3
"""a SCRIPT THAT LIST ALL STATES FROM THE DATABASE hbtn_0e_0_usa."""

import MySQLdb
import sys


if __name__ == "__main__":
    """MAIN FUNCTION"""
    db = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3])
    cur = db.cursor()
    cur.execute("SELECT * FROM states ORDER BY id ASC")
    query_rows = cur.fetchall()
    for row in query_rows:
        print(row)
    cur.close()
    db.close()
