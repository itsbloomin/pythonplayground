import sqlite3

# connect to database
conn = sqlite3.connect('customer.db')

# create cursor
c = conn.cursor()

# query
c.execute("SELECT * FROM customers")
items = c.fetchall()
for item in items:
    print(item[0], item[1], item[2])

# commit changes
conn.commit()

# close connection
conn.close()
