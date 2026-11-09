import sqlite3

#1.
# conn = sqlite3.connect("webshop.db")
# cursor = conn.cursor()

# cursor.execute("SELECT name, price FROM products")
# rows = cursor.fetchall()

# print(rows)

# conn.close()


#2.
# conn = sqlite3.connect("webshop.db")
# cursor = conn.cursor()

# cursor.execute("SELECT name, price FROM products ORDER BY price DESC")
# for name, price in cursor.fetchall():

#     print(f"{name:<20} {price:>8.2f} kr")

# conn.close()


#3.
conn = sqlite3.connect("webshop.db")
cursor = conn.cursor()

#cursor.execute("SELECT COUNT(*) FROM customers")
#count = cursor.fetchone()[0]

# city = 'Uppsala'
# cursor.execute(
#     "SELECT first_name, last_name FROM customers WHERE city = ?",
#     (city,)
# )

# print(cursor.fetchall())

# conn.close()


#4. Bad example:
city = "x' OR '1'="1'
sql = f"SELECT first_name FROM customers WHERE city = {city}"

print(cursor.fetchall())

conn.close()





 
 
# def connect():
#     conn = sqlite3.connect("webshop.db")
#     conn.execute("PRAGMA foreign_keys = ON")
#     return conn

#     cursor.execute("SELECT name, price FROM products")
 
 
# def list_products(conn):
#     cursor = conn.execute("SELECT product_id, name, price, stock FROM products")
#     for pid, name, price, stock in cursor.fetchall():
#         print(f"{pid:>3}  {name:<20} {price:>8.2f} kr  ({stock} in stock)")
 
 
# def search_customers(conn):
#     city = input("City: ")
#     cursor = conn.execute(
#         "SELECT first_name, last_name FROM customers WHERE city = ?", (city,))
#     rows = cursor.fetchall()
#     if not rows:
#         print("No customers found.")
#     for first, last in rows:
#         print(first, last)
 
 
# def add_product(conn):
#     name = input("Name: ")
#     category = input("Category: ")
#     price = float(input("Price: "))
#     stock = int(input("Stock: "))
#     conn.execute(
#         "INSERT INTO products (name, category, price, stock) VALUES (?, ?, ?, ?)",
#         (name, category, price, stock))
#     conn.commit()
#     print("Saved!")
 
 
# def main():
#     conn = connect()
#     while True:
#         print("\n1) List products  2) Search customers  3) Add product  0) Quit")
#         choice = input("> ")
#         if choice == "1":
#             list_products(conn)
#         elif choice == "2":
#             search_customers(conn)
#         elif choice == "3":
#             add_product(conn)
#         elif choice == "0":
#             break
#     conn.close()
 
 
# main()