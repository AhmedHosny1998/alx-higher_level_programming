#!/usr/bin/python3
"""list all states from the database hbtn_0e_0_usa"""

import MySQLdb
from sys import argv

if __name__ == "__main__":
    db = MySQLdb.connect(host='localhost', user=argv[1], passwd=argv[2], db=argv[3], port=3306)
    cur = db.cursor()

    q = """SELECT * FROM states WHERE BINARY name
    LIKE 'N%' ORDER BY ID ASC"""
    cur.execute(q)
    res = cur.fetchall()
    for row in res:
        print(row)
    cur.close()
    db.close()
    

