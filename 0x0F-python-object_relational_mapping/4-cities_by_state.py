#!/usr/bin/python3
"""
This module accesses a database
and prints values of columns from two different
tables using join
"""
import MySQLdb
import sys


if __name__ == "__main__":
    """Does not execute when imported"""

    args = sys.argv

    db1 = MySQLdb.connect(host='localhost', port=3306,
                          user=args[1], passwd=args[2], db=args[3])
    mycur = db1.cursor()

    mycur.execute("SELECT cities.id, cities.name, states.name FROM cities\
                  INNER JOIN states ON cities.state_id =\
                  states.id ORDER BY cities.id ASC")
    intable = mycur.fetchall()
    for row in intable:
        print("({}, \'{}\', \'{}\')".format(row[0], row[1], row[2]))
