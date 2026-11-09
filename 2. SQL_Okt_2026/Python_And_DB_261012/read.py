# import sqlite3

# conn = sqlite3.connect("webshop.db")
# cursor = conn.cursor()

# cursor.execute("SELECT name, price FROM products")
# rows = cursor.fetchall()

# print(rows)

# conn.close()
#--------------------------------2

# import sqlite3

# conn = sqlite3.connect("webshop.db")
# cursor = conn.cursor()

# cursor.execute("SELECT name, price FROM products ORDER BY price DESC")
# for name, price in cursor. fetchall():
#     print(f"{name:<20} {price:>8.2f} kr")

# conn.close()
#--------------------------------------------3

# import sqlite3

# conn = sqlite3.connect("webshop.db")
# cursor = conn.cursor()

# cursor.execute("SELECT COUNT(*) FROM customers")
# count = cursor.fetchone()[0]
# print("Customers:", count)
# conn.close()
#------------------------------------------4

# import sqlite3

# conn = sqlite3.connect("webshop.db")
# cursor = conn.cursor()

# city ='Uppsala'
# cursor.execute(
#     "SELECT first_name, last_name FROM customers WHERE city = ?",
#     (city,)
# )
# print(cursor.fetchone())

# conn.close()
#-----------------------------------5"
# The bad example

import sqlite3

conn = sqlite3.connect("webshop.db")
cursor = conn.cursor()

city = "x' OR '1'="1'

sql = f"SELECT first_name FROM customers WHERE city = {city}"

print(cursor.fetchone())

conn.close()
