#********************************************************************************************
#  Novica Ivkovic                                                                           *
#  Cours: SQL                                                  *
#  Oktober 12 2026 - LAB: Python meets SQL                                                                *
#             *
#********************************************************************************************


# from datetime import datetime
# from pymongo import MongoClient
# client = MongoClient("mongodb://localhost:27017/")
# db = client["webshop"]
# customers = [
#     {"_id": 1, "first_name": "Anna", "last_name": "Lindqvist", "email": "anna.lindqvist@example.com", "city": "Uppsala", "joined": datetime(2024, 3, 14), "newsletter": True},
#     {"_id": 2, "first_name": "Erik", "last_name": "Johansson", "email": "erik.j@example.com", "city": "Stockholm", "joined": datetime(2023, 11, 2), "phone": "070-1234567"},
#     {"_id": 3, "first_name": "Sara", "last_name": "Ahmed", "email": "sara.ahmed@example.com", "city": "Göteborg", "joined": datetime(2025, 1, 20), "newsletter": True},
#     {"_id": 4, "first_name": "Johan", "last_name": "Berg", "email": "johan.berg@example.com", "city": "Uppsala", "joined": datetime(2022, 6, 30)},
#     {"_id": 5, "first_name": "Maria", "last_name": "Nilsson", "email": "maria.n@example.com", "city": "Malmö", "joined": datetime(2025, 8, 11), "phone": "073-7654321"},
#     {"_id": 6, "first_name": "Ali", "last_name": "Hassan", "email": "ali.hassan@example.com", "city": "Stockholm", "joined": datetime(2024, 9, 5), "newsletter": False},
#     {"_id": 7, "first_name": "Emma", "last_name": "Karlsson", "email": "emma.k@example.com", "city": "Västerås", "joined": datetime(2023, 2, 17)},
#     {"_id": 8, "first_name": "Oskar", "last_name": "Persson", "email": "oskar.p@example.com", "city": "Uppsala", "joined": datetime(2025, 5, 28), "newsletter": True},
#     {"_id": 9, "first_name": "Fatima", "last_name": "Yilmaz", "email": "fatima.y@example.com", "city": "Göteborg", "joined": datetime(2024, 12, 1), "phone": "076-1112233"},
#     {"_id": 10, "first_name": "Lukas", "last_name": "Ek", "email": "lukas.ek@example.com", "joined": datetime(2026, 1, 9)}
# ]
# products = [
#     {"_id": 1, "name": "Hoodie Black", "category": "Clothing", "price": 599, "stock": 25, "tags": ["winter", "cotton", "bestseller"], "details": {"color": "black", "material": "cotton"}},
#     {"_id": 2, "name": "T-shirt White", "category": "Clothing", "price": 249, "stock": 60, "tags": ["summer", "cotton"], "details": {"color": "white", "material": "cotton"}},
#     {"_id": 3, "name": "Cap Logo", "category": "Accessories", "price": 199, "stock": 40, "tags": ["summer"], "details": {"color": "black"}},
#     {"_id": 4, "name": "Sneakers Classic", "category": "Shoes", "price": 1199, "stock": 12, "tags": ["bestseller"], "details": {"color": "white", "material": "leather"}, "sizes": [39, 40, 41, 42, 43, 44]},
#     {"_id": 5, "name": "Water Bottle", "category": "Accessories", "price": 149, "stock": 0, "tags": ["sport"], "details": {"color": "green", "material": "steel"}},
#     {"_id": 6, "name": "Joggers Grey", "category": "Clothing", "price": 499, "stock": 18, "tags": ["sport", "cotton"], "details": {"color": "grey", "material": "cotton"}},
#     {"_id": 7, "name": "Backpack Urban", "category": "Accessories", "price": 749, "stock": 8, "tags": ["travel"], "details": {"color": "black", "material": "nylon"}},
#     {"_id": 8, "name": "Running Shoes", "category": "Shoes", "price": 1399, "stock": 5, "tags": ["sport", "bestseller"], "details": {"color": "blue"}, "sizes": [40, 41, 42, 43, 44, 45]},
#     {"_id": 9, "name": "Socks 3-pack", "category": "Clothing", "price": 129, "stock": 100, "tags": ["cotton"], "details": {"color": "white", "material": "cotton"}},
#     {"_id": 10, "name": "Beanie", "category": "Accessories", "price": 179, "stock": 30, "tags": ["winter"], "details": {"color": "black", "material": "wool"}},
#     {"_id": 11, "name": "Rain Jacket", "category": "Clothing", "price": 1299, "stock": 0, "tags": ["winter", "waterproof"], "details": {"color": "yellow", "material": "polyester"}},
#     {"_id": 12, "name": "Sandals", "category": "Shoes", "price": 399, "stock": 22, "tags": ["summer"], "details": {"color": "brown", "material": "leather"}, "sizes": [37, 38, 39, 40, 41]}
# ]
# orders = [
#     {"_id": 1, "customer_id": 1, "order_date": datetime(2026, 1, 5), "status": "delivered", "items": [{"product_id": 1, "name": "Hoodie Black", "quantity": 1, "unit_price": 599}, {"product_id": 3, "name": "Cap Logo", "quantity": 2, "unit_price": 199}]},
#     {"_id": 2, "customer_id": 2, "order_date": datetime(2026, 1, 12), "status": "delivered", "items": [{"product_id": 4, "name": "Sneakers Classic", "quantity": 1, "unit_price": 1199}]},
#     {"_id": 3, "customer_id": 1, "order_date": datetime(2026, 1, 20), "status": "delivered", "items": [{"product_id": 9, "name": "Socks 3-pack", "quantity": 3, "unit_price": 129}]},
#     {"_id": 4, "customer_id": 3, "order_date": datetime(2026, 1, 28), "status": "delivered", "items": [{"product_id": 2, "name": "T-shirt White", "quantity": 2, "unit_price": 249}, {"product_id": 6, "name": "Joggers Grey", "quantity": 1, "unit_price": 499}]},
#     {"_id": 5, "customer_id": 4, "order_date": datetime(2026, 2, 3), "status": "delivered", "items": [{"product_id": 8, "name": "Running Shoes", "quantity": 1, "unit_price": 1399}]},
#     {"_id": 6, "customer_id": 5, "order_date": datetime(2026, 2, 10), "status": "delivered", "items": [{"product_id": 1, "name": "Hoodie Black", "quantity": 1, "unit_price": 599}, {"product_id": 10, "name": "Beanie", "quantity": 1, "unit_price": 179}]},
#     {"_id": 7, "customer_id": 6, "order_date": datetime(2026, 2, 14), "status": "cancelled", "items": [{"product_id": 7, "name": "Backpack Urban", "quantity": 1, "unit_price": 749}]},
#     {"_id": 8, "customer_id": 2, "order_date": datetime(2026, 2, 21), "status": "delivered", "items": [{"product_id": 2, "name": "T-shirt White", "quantity": 1, "unit_price": 249}, {"product_id": 9, "name": "Socks 3-pack", "quantity": 2, "unit_price": 129}]},
#     {"_id": 9, "customer_id": 8, "order_date": datetime(2026, 2, 27), "status": "shipped", "items": [{"product_id": 11, "name": "Rain Jacket", "quantity": 1, "unit_price": 1299}]},
#     {"_id": 10, "customer_id": 9, "order_date": datetime(2026, 3, 4), "status": "shipped", "items": [{"product_id": 3, "name": "Cap Logo", "quantity": 1, "unit_price": 199}, {"product_id": 2, "name": "T-shirt White", "quantity": 3, "unit_price": 249}]},
#     {"_id": 11, "customer_id": 1, "order_date": datetime(2026, 3, 9), "status": "shipped", "items": [{"product_id": 6, "name": "Joggers Grey", "quantity": 2, "unit_price": 499}]},
#     {"_id": 12, "customer_id": 3, "order_date": datetime(2026, 3, 15), "status": "new", "items": [{"product_id": 4, "name": "Sneakers Classic", "quantity": 1, "unit_price": 1199}, {"product_id": 9, "name": "Socks 3-pack", "quantity": 1, "unit_price": 129}]},
#     {"_id": 13, "customer_id": 6, "order_date": datetime(2026, 3, 18), "status": "new", "items": [{"product_id": 1, "name": "Hoodie Black", "quantity": 2, "unit_price": 599}]},
#     {"_id": 14, "customer_id": 4, "order_date": datetime(2026, 3, 22), "status": "new", "items": [{"product_id": 10, "name": "Beanie", "quantity": 2, "unit_price": 179}, {"product_id": 3, "name": "Cap Logo", "quantity": 1, "unit_price": 199}]},
#     {"_id": 15, "customer_id": 2, "order_date": datetime(2026, 3, 28), "status": "new", "items": [{"product_id": 8, "name": "Running Shoes", "quantity": 1, "unit_price": 1399}, {"product_id": 2, "name": "T-shirt White", "quantity": 1, "unit_price": 249}]}
# ]
# for name in ["customers", "products", "orders"]:
#     db[name].drop()
# db.customers.insert_many(customers)
# db.products.insert_many(products)
# db.orders.insert_many(orders)
# print("webshop is ready:",
#       db.customers.count_documents({}), "customers,",
#       db.products.count_documents({}), "products,",
#       db.orders.count_documents({}), "orders")
 
# has context menu
# Send to: thread only






#********************************************************************************************
#   Python and the database

# Work in VS Code, in your folder with a copy of webshop.db. Close the database in DB Browser
# first (Close Database), otherwise Python can get the error 'database is locked'. Exercises 5 to 8
# build on shop.py from the code-along.
#********************************************************************************************


#***********************************************************************************************
#  Exercise 1
#  Write a script that prints all customers as 'First Last (City)'.
#  Expected: 10 lines
#***********************************************************************************************

# import sqlite3

# conn = sqlite3.connect("webshop.db")
# conn.execute("PRAGMA foreign_keys = ON")
# cursor = conn.cursor()


# cursor.execute("SELECT first_name, last_name, COALESCE(city, 'unknown') FROM customers")

# for first_name, last_name, city in cursor.fetchall():
#     print(f"{first_name} {last_name} ({city})")

# conn.close()


#****************************************************************************************************
#  Exercise 2
#  Ask the user for a max price and show all products cheaper than that. Use a ? placeholder.
#****************************************************************************************************

# import sqlite3

# conn = sqlite3.connect("webshop.db")
# cursor = conn.cursor()

# max_price = float(input("Input maximal price (kr): "))


# query = "SELECT name, price FROM products WHERE price < ? ORDER BY price ASC"
# cursor.execute(query, (max_price,))

# products = cursor.fetchall()

# if products:
#     print(f"\nProducts cheaper then {max_price} kr:")
#     for name, price in products:
#         print(f"  - {name:<20}- {price:>7.2f} kr")
# else:
#     print(f"\nThere is no products cheaper than {max_price} kr.")

# conn.close()





#************************************************************************************************
#   Exercise 3
#   Ask the user for a category and print how many products it has. Use COUNT and fetchone().                                  *
#************************************************************************************************

# import sqlite3

# conn = sqlite3.connect("webshop.db")
# cursor = conn.cursor()


# category = input("Input a category (for example: Clothing, Shoes, Accessories): ")


# query = "SELECT COUNT(*) FROM products WHERE category = ?"
# cursor.execute(query, (category,))


# result = cursor.fetchone()
# count = result[0]

# print(f"Category '{category}' has total {count} product(s).")

# conn.close()



#******************************************************************************************************
#  Exercise 4
#   Explain in your own words: why is building SQL with an f-string dangerous, and why is a ?
#   placeholder safe?
#   Expected: a few sentences
#******************************************************************************************************

# - It is possible and very danger that via f-strins user can directly insert unchecked input
#    that can change SQL sintax and logic of a query, and even to go around autentification 
#     and delete or take some data from the data base.
#
#   - ? placeholder is a safe way - Input is standariserad and parametriserad as a value - not SQL command.
#        In that case eaven if import looks like SQL command it is not going to execute and harm the data base,
#        because this for example SQL command is goint to be interpreted like a text or number... not command!



#*******************************************************************************************************
#   Exercise 5
#   Add a menu option 4 to shop.py: change the stock of a product. Ask for the product id and the new
#   stock.
#*******************************************************************************************************

# import sqlite3

# def show_menu():
#     print("\n   --- WEBSHOP MENU ---\n")
#     print(" 1. Show all procucts")
#     print(" 2. Search by price")
#     print(" 3. Count by category")
#     print(" 4. Change stock levels of products")
#     print(" 9. Exit\n")

# def update_stock():
#     try:
#         product_id = int(input("Input ID of procuct: "))
#         new_stock = int(input("Input a new stock level: "))

#         conn = sqlite3.connect("webshop.db")
#         cursor = conn.cursor()

#         cursor.execute(
#             "UPDATE products SET stock = ? WHERE product_id = ?",
#             (new_stock, product_id)
#         )
        
#         conn.commit()   # We need too confirm uppdate in db.
#         if cursor.rowcount > 0:
#             print(f"The  stock status for product ID {product_id} has been successfully updated to {new_stock}.")
#         else:
#             print(f"Product with ID {product_id} not found.")

#         conn.close()
#     except ValueError:
#         print("Error: ID and stock level must be integers!")


# while True:
#     show_menu()
#     choice = input("Select an option: ")

#     if choice == "4":
#         update_stock()
#     elif choice == "9":
#         print("Bye, bye!\n")
#         break



#***********************************************************************************************
#   Exercise 6
#   Add a menu option 5 to shop.py: show an order's receipt. Ask for the order_id and use a JOIN to
#   show product names.
#***********************************************************************************************

# import sqlite3

# def show_menu():
#     print("\n   --- WEBSHOP MENU ---\n")
#     print(" 1. Show all procucts")
#     print(" 2. Search by price")
#     print(" 3. Count by category")
#     print(" 4. Change stock levels of products")
#     print(" 5. Show an order's receipt" )
#     print(" 9. Exit\n")

# def update_stock():
#     try:
#         product_id = int(input("Input ID of procuct: "))
#         new_stock = int(input("Input a new stock level: "))

#         conn = sqlite3.connect("webshop.db")
#         cursor = conn.cursor()

#         cursor.execute(
#             "UPDATE products SET stock = ? WHERE product_id = ?",
#             (new_stock, product_id)
#         )
        
#         conn.commit()   # We need too confirm uppdate in db.
#         if cursor.rowcount > 0:
#             print(f"The  stock status for product ID {product_id} has been successfully updated to {new_stock}.")
#         else:
#             print(f"Product with ID {product_id} not found.")

#         conn.close()
#     except ValueError:
#         print("Error: ID and stock level must be integers!")

# # A part - uppdate from exercise 6

# def show_order_receipt():
#     try:
#         order_id = int(input("Input order_id: "))

#         conn = sqlite3.connect("webshop.db")
#         cursor = conn.cursor()

#         query = """
#             SELECT p.name, oi.quantity, oi.unit_price, (oi.quantity * oi.unit_price) AS line_total
#             FROM order_items oi
#             JOIN products p ON oi.product_id = p.product_id
#             WHERE oi.order_id = ?
#         """
#         cursor.execute(query, (order_id,))
#         items = cursor.fetchall()

#         if items:
#             print(f"\n  --- RECEIPT FOR ORDER #{order_id} ---")
#             total_amount = 0
#             for name, quantity, unit_price, line_total in items:
#                 print(f"  - {name} | {quantity} * {unit_price} kr = {line_total} kr")
#                 total_amount += line_total
            
#             print("-" * 35)
#             print(f"TOTAL: {total_amount} kr")
#         else:
#             print(f"Order #{order_id} was not found or has no items.")

#         conn.close()
#     except ValueError:
#         print("Please enter a valid numeric order ID.")

# # now we continue with "old" part from ex.5


# while True:
#     show_menu()
#     choice = input("Select an option: ")

#     if choice == "4":
#         update_stock()
#     elif choice == "5":
#         show_order_receipt()    
#     elif choice == "9":
#         print("Bye, bye!\n")
#         break



#****************************************************************************************************
#   Exercise 7
#   What happens in add_product if the user types abc as the price? Fix it with try/except.
#****************************************************************************************************

# I fixed it in ex.6 - with try/except:

    # conn.close()
    # except ValueError:
    #     print("Please enter a valid numeric order ID.")

#************************************************************************************************
#   Exercise 8
#   Challenge: add a menu option 6, 'top 3 best-selling products'. Use GROUP BY, ORDER BY and
#   LIMIT.
#   Expected: 3 lines
#************************************************************************************************


import sqlite3

def show_menu():
    print("\n   --- WEBSHOP MENU ---\n")
    print(" 1. Show all procucts")
    print(" 2. Search by price")
    print(" 3. Count by category")
    print(" 4. Change stock levels of products")
    print(" 5. Show an order's receipt" )
    print(" 6. Top 3 best-selling products" )
    print(" 9. Exit\n")

def update_stock():
    try:
        product_id = int(input("Input ID of procuct: "))
        new_stock = int(input("Input a new stock level: "))

        conn = sqlite3.connect("webshop.db")
        cursor = conn.cursor()

        cursor.execute(
            "UPDATE products SET stock = ? WHERE product_id = ?",
            (new_stock, product_id)
        )
        
        conn.commit()   # We need too confirm uppdate in db.
        if cursor.rowcount > 0:
            print(f"The  stock status for product ID {product_id} has been successfully updated to {new_stock}.")
        else:
            print(f"Product with ID {product_id} not found.")

        conn.close()
    except ValueError:
        print("Error: ID and stock level must be integers!")

# A part - uppdate from exercise 6

def show_order_receipt():
    try:
        order_id = int(input("Input order_id: "))

        conn = sqlite3.connect("webshop.db")
        cursor = conn.cursor()

        query = """
            SELECT p.name, oi.quantity, oi.unit_price, (oi.quantity * oi.unit_price) AS line_total
            FROM order_items oi
            JOIN products p ON oi.product_id = p.product_id
            WHERE oi.order_id = ?
        """
        cursor.execute(query, (order_id,))
        items = cursor.fetchall()

        if items:
            print(f"\n  --- RECEIPT FOR ORDER #{order_id} ---")
            total_amount = 0
            for name, quantity, unit_price, line_total in items:
                print(f"  - {name} | {quantity} * {unit_price} kr = {line_total} kr")
                total_amount += line_total
            
            print("-" * 35)
            print(f"TOTAL: {total_amount} kr")
        else:
            print(f"Order #{order_id} was not found or has no items.")

        conn.close()
    except ValueError:
        print("Please enter a valid numeric order ID.")


# A part - uppdate from exercise 8

def show_top_selling_products():
    conn = sqlite3.connect("webshop.db")
    cursor = conn.cursor()

    
    query = """
        SELECT p.name, SUM(oi.quantity) AS total_sold
        FROM order_items oi
        JOIN products p ON oi.product_id = p.product_id
        GROUP BY oi.product_id, p.name
        ORDER BY total_sold DESC
        LIMIT 3
    """
    cursor.execute(query)
    top_products = cursor.fetchall()

    if top_products:
        print("\n  --- TOP 3 BEST-SELLING PRODUCTS ---\n")
        for name, total_sold in top_products:
            print(f"  - {name:<15}: {total_sold} units sold")
    else:
        print("No order items found.")

    conn.close()

# now we continue with "old" part from ex.5


while True:
    show_menu()
    choice = input("Select an option: ")

    if choice == "4":
        update_stock()
    elif choice == "5":
        show_order_receipt()  
    elif choice == "6":
        show_top_selling_products()        
    elif choice == "9":
        print("Bye, bye!  Tack för idag! Ha en trevlig kväll! :)\n")
        break





#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
#******************************************************************************************************
#   Personal data       - GDPR - 
#   Use webshop.db in
#******************************************************************************************************
#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++


#*******************************************************************************************************
#  Exercise 9
#   Anna (customer 1) asks: 'Which products have I bought?' Write the query that answers her. Show
#   product names only, each once.
#   Expected: 4 rows
#*******************************************************************************************************

#***********************************************************************************************
#   Exercise 10
#   Erik says his email is wrong. Correct it to erik.johansson@example.com.
#   Expected: 1 row changed
#***********************************************************************************************

    
#****************************************************************************************************
#   Exercise 11
#   Create a view customer_overview that a support person can use: customer_id, first name, city and
#   number of orders, but no email. Customers with no orders must also be shown.
#   Expected: 10 rows when you SELECT from the view                                          *
#****************************************************************************************************



#************************************************************************************************
#  Exercise 12
#   Discuss in pairs: the webshop wants to add a birth_date column 'just in case'. What would you
#   say? Write two sentences.
#   Expected: two sentences
#************************************************************************************************


#---------------------------------------------------------------------------------------------
# **********************************  END of LAB - 2026-10-12  ********************************************************