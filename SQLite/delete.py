import sqlite3

# connect to database
conn = sqlite3.connect('customer.db')

# create cursor
c = conn.cursor()

# query
c.execute("DELETE from customers WHERE rowid = 6")

# query
c.execute("SELECT rowid, * FROM customers")
items = c.fetchall()
for item in items:
    print(item[0], item[1], item[2], item[3])

# commit changes
conn.commit()

# close connection
conn.close()