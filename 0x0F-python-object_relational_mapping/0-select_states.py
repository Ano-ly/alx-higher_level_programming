#!/usr/bin/python3
"""This module accesses a database"""
import MySQLdb
import sys


if __name__ == "__main__":
    """Does not execute when imported"""

    args = sys.argv

    db1 = MySQLdb.connect(host='localhost', port=3306,
                          user=args[1], passwd=args[2], db=args[3])
    mycur = db1.cursor()

    mycur.execute("SELECT * FROM states ORDER BY states.id ASC")
    intable = mycur.fetchall()
    for row in intable:
        print("({}, '{}')".format(row[0], row[1]))
