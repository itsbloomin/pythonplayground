# SQLite
# https://www.sqlite.org/lang.html
# https://docs.python.org/3/library/sqlite3.html
# https://www.sqlitetutorial.net/sqlite-python/
# https://www.tutorialspoint.com/sqlite/sqlite_python.htm
# YouTube Tutorial: https://www.youtube.com/watch?v=byHcYRpMgI4
import sqlite3

# connect to database
conn = sqlite3.connect('customer.db')

# create cursor
c = conn.cursor()

# query


# commit changes
conn.commit()

# close connection
conn.close()
