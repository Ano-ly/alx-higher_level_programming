#!/usr/bin/python3
import MySQLdb
import sys

# This module accesses a database

args = sys.argv

db1 = MySQLdb.connect(host='localhost', port=3306, 
                      user=args[1], passwd=args[2], db=args[3])
mycur = db1.cursor()

mycur.execute("SELECT * FROM states ORDER BY states.id ASC")
intable = mycur.fetchall()
for row in intable:
    print("({}: '{}')".format(row[0], row[1]))

if __name__ == "main":
    main()
