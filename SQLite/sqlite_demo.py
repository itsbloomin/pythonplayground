# SQLite
# https://www.sqlite.org/lang.html
# https://docs.python.org/3/library/sqlite3.html
# https://www.sqlitetutorial.net/sqlite-python/
# https://www.tutorialspoint.com/sqlite/sqlite_python.htm
# YouTube Tutorial: https://www.youtube.com/watch?v=byHcYRpMgI4
import sqlite3

# Query and Display all
def show_all():
    conn = sqlite3.connect('customer.db')  # connect to database
    c = conn.cursor()  # create cursor
    c.execute("SELECT rowid, * FROM customers")
    items = c.fetchall()
    for item in items:
        print(item[0], item[1], item[2], item[3])
    conn.commit()  # commit changes
    conn.close()  # close connection

# Add many records to table
def add_record(first, last, email):
    conn = sqlite3.connect('customer.db')  # connect to database
    c = conn.cursor()  # create cursor
    c.execute("INSERT INTO customers VALUES (?, ?, ?)", (first, last, email))
    conn.commit()  # commit changes
    conn.close()  # close connection

# Add new record to table
def add_many_records(list):
    conn = sqlite3.connect('customer.db')  # connect to database
    c = conn.cursor()  # create cursor
    c.executemany("INSERT INTO customers VALUES (?, ?, ?)", (list))
    conn.commit()  # commit changes
    conn.close()  # close connection

# Delete record, use rowid as string
def remove_record(rowid):
    conn = sqlite3.connect('customer.db')  # connect to database
    c = conn.cursor()  # create cursor
    c.execute("DELETE FROM customers WHERE rowid = (?)", rowid)
    conn.commit()  # commit changes
    conn.close()  # close connection

# query with email
def email_lookup(email):
    conn = sqlite3.connect('customer.db')  # connect to database
    c = conn.cursor()  # create cursor
    c.execute("SELECT * FROM customers WHERE email = (?)", (email,))
    items = c.fetchall()
    for item in items:
        print(item[0], item[1], item[2])
    conn.commit()  # commit changes
    conn.close()  # close connection

# add_record("Jonathan", "Jones", "jonjones@hotmail.com")
# show_all()

# remove_record('7')
# show_all()

# customer_list = [("Mike","Smith","mike@smith.com"), ("Megan","Brown","megan@brown.com")]
# add_many_records(customer_list)

# email_lookup("jonjones@hotmail.com")

show_all()
