import sqlite3

# connect to database
conn = sqlite3.connect('customer.db')

# create cursor
c = conn.cursor()

# commands

# insert
c.execute("INSERT INTO customers VALUES ('Mary', 'Brown', 'mary@gmail.com')")

# insert many
many_customers = [
    ('Jane', 'Doe', 'jane@gmail.com'),
    ('Amy', 'Smith', 'amy@gmail.com'),
    ('Tony', 'DiMarco', 'tony@gmail.com')
]
c.executemany("INSERT INTO customers VALUES (?, ?, ?)", many_customers)

# commit changes
conn.commit()

# close connection
conn.close()
