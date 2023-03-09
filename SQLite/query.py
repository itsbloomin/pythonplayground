import sqlite3

# connect to database
conn = sqlite3.connect('customer.db')

# create cursor
c = conn.cursor()

# query
c.execute("SELECT * FROM customers")
print(c.fetchall())

# commit changes
conn.commit()

# close connection
conn.close()
