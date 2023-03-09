import sqlite3

# connect to database
conn = sqlite3.connect('customer.db')

# create cursor
c = conn.cursor()

# create a table (w/DocString)
# remove / comment out once created -- maybe check if exists?
c.execute("""CREATE TABLE customers (
                first_name text,
                last_name text,
                email text
         )""")

# commit changes
conn.commit()

# close connection
conn.close()