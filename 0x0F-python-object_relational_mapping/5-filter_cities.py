#!/usr/bin/python3
"""
This module accesses a database and prints
all the cities of a state passed to the
script as argument (safe)
"""
import MySQLdb
import sys


if __name__ == "__main__":
    """Does not execute when imported"""

    args = sys.argv

    db1 = MySQLdb.connect(host='localhost', port=3306,
                          user=args[1], passwd=args[2], db=args[3])
    mycur = db1.cursor()
    string = "SELECT cities.name FROM cities JOIN states ON states.id =\
            cities.state_id WHERE BINARY states.name = '{}'".format(args[4])
    mycur.execute(string)
    intable = mycur.fetchall()
    mylist = []
    for row in intable:
        mylist.append(row[0])
    print(", ".join(mylist))
