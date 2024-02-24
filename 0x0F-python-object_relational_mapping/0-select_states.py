#!/usr/bin/python3
""" Script that lists all states from the database hbtn_0e_0_usa """
import MySQLdb
from sys import argv

if __name__ == "__main__":
    db = MySQL.connect(host = "localhost", port = 3306, user = argv[1], passwd = argv[2], db = argv[3])
    c = db.cursor()
    c.execute("SELECT * FROM states ORDER BY is ACS")
    r = c.fetchall()
    for row in r:
        print(row)
    c.close()
    db.close()
