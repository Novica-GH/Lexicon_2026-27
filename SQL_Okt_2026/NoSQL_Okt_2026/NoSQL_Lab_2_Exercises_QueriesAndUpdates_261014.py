##********************************************************************************************
#  Novica Ivkovic                                                                           *
#  Cours: System Developer Python and AI                                                    *
#  Oktober 14 2026 -  7. SQL second week - NoSQL- LAB 2
#
#                   Exercises: Queries and updates            
#********************************************************************************************

# Exercises: Queries and updates

# Use Python with the header from the code-along. Start by running python seed_webshop.py.
# Exercises 8 to 10 change data: run the seed script again when you are done.

# The header (at the top of every Python file):

#-----------------------------------------
# from pymongo import MongoClient
# client = MongoClient("mongodb://localhost:27017/")
# db = client["webshop"]
#---------------------------------------


# Exercise 1
# Show the name and price of all products that cost more than 1000 kr.
# Expected: 3 products

# from pymongo import MongoClient
# client = MongoClient("mongodb://localhost:27017/")
# db = client["webshop"]

# for product in db.products.find({"price": {"$gt": 1000}}):
#     print(f"{product['name']}: {product['price']} kr")

# Sneakers Classic: 1199 kr
# Running Shoes: 1399 kr
# Rain Jacket: 1299 kr
#------------------------------------


# Exercise 2
# Show all orders that are not delivered. Use $ne. Print the _id and status.
# Expected: 8 orders

# from pymongo import MongoClient
# client = MongoClient("mongodb://localhost:27017/")
# db = client["webshop"]

# for order in db.orders.find({"status": {"$ne": "delivered"}}):
#     print(f"Order {order['_id']}: {order['status']}")

# Order 7: cancelled
# Order 9: shipped
# Order 10: shipped
# Order 11: shipped
# Order 12: new
# Order 13: new
# Order 14: new
# Order 15: new
#--------------------------------


# Exercise 3
# Show customers who live in Stockholm or Malmö, using $in.
# Expected: 3 customers

# from pymongo import MongoClient
# client = MongoClient("mongodb://localhost:27017/")
# db = client["webshop"]

# for customer in db.customers.find({"city": {"$in": ["Stockholm", "Malmö"]}}):
#     print(f"{customer['first_name']} {customer['last_name']} ({customer['city']})")

# Erik Johansson (Stockholm)
# Maria Nilsson (Malmö)
# Ali Hassan (Stockholm)
# Novica Ivković (Stockholm)    -  I am ++ here  - Lab1.7 from yesterday
# Novica Ivković (Stockholm)    - And here,      - Lab1.8 from yesterday      
# Novica Ivković (Stockholm)    - and here.      - Lab1.8 from yesterday
#---------------------------------------------


# Exercise 4
# Which products are white? Use dot notation.
# Expected: 3 products

# from pymongo import MongoClient
# client = MongoClient("mongodb://localhost:27017/")
# db = client["webshop"]

# for product in db.products.find({"details.color": "white"}):
#     print(f"{product['name']} - {product['details']['color']}")

# # T-shirt White - white
# # Sneakers Classic - white
# # Socks 3-pack - white
#-----------------------------



# Exercise 5
# Which products have the tag sport? Show only name and tags, without _id.
# Expected: 3 products

# from pymongo import MongoClient
# client = MongoClient("mongodb://localhost:27017/")
# db = client["webshop"]

# for product in db.products.find({"tags": "sport"}, {"name": 1, "tags": 1, "_id": 0}):
#     print(product)

# # {'name': 'Water Bottle', 'tags': ['sport']}
# # {'name': 'Joggers Grey', 'tags': ['sport', 'cotton']}
# # {'name': 'Running Shoes', 'tags': ['sport', 'bestseller']}
#--------------------------------------------------------------


# Exercise 6
# Show the 5 cheapest products, cheapest first. Only name and price.
# Expected: 5 products

# from pymongo import MongoClient
# client = MongoClient("mongodb://localhost:27017/")
# db = client["webshop"]

# cursor = db.products.find({}, {"name": 1, "price": 1, "_id": 0}).sort("price", 1).limit(5)

# for product in cursor:
#     print(f"{product['name']}: {product['price']} kr")

# # Socks 3-pack: 129 kr
# # Water Bottle: 149 kr
# # Beanie: 179 kr
# # Cap Logo: 199 kr
# # T-shirt White: 249 kr
#------------------------


# Exercise 7
# Which orders contain product 2 (T-shirt White)? Hint: dot notation works on arrays of objects too:
# "items.product_id".
# Expected: 4 orders

# from pymongo import MongoClient
# client = MongoClient("mongodb://localhost:27017/")
# db = client["webshop"]


# for order in db.orders.find({"items.product_id": 2}):
#     print(f"Order ID: {order['_id']}, Status: {order['status']}")

# # Order ID: 4, Status: delivered
# # Order ID: 8, Status: delivered
# # Order ID: 10, Status: shipped
# # Order ID: 15, Status: new
#--------------------------------



# Exercise 8
# Raise the price of all Accessories by 20 kr with $inc. Then print the Accessories with their new
# prices.
# Expected: 4 products, each 20 kr more

# from pymongo import MongoClient
# client = MongoClient("mongodb://localhost:27017/")
# db = client["webshop"]

# db.products.update_many(
#     {"category": "Accessories"},
#     {"$inc": {"price": 20}}
# )

# for product in db.products.find({"category": "Accessories"}):
#     print(f"{product['name']}: {product['price']} kr")

# # Cap Logo: 219 kr
# # Water Bottle: 169 kr
# # Backpack Urban: 769 kr
# # Beanie: 199 kr
# # Leather Belt: 369 kr  - comming from Lab1.8 from yesterday
#---------------------------



# Exercise 9
# Add the tag "new" to the Rain Jacket without creating duplicates, and give it a field restock_date
# with today's date (use datetime.now()).
# Expected: 1 product with the new tag and field (the time will be yours)

# from datetime import datetime
# from pymongo import MongoClient
# client = MongoClient("mongodb://localhost:27017/")
# db = client["webshop"]


# db.products.update_one(
#     {"name": "Rain Jacket"},
#     {
#         "$addToSet": {"tags": "new"},
#         "$set": {"restock_date": datetime.now()}
#     }
# )

# rain_jacket = db.products.find_one({"name": "Rain Jacket"})
# print(f"Name: {rain_jacket['name']}")
# print(f"Tags: {rain_jacket['tags']}")
# print(f"Restock Date: {rain_jacket['restock_date']}")

# # Name: Rain Jacket
# # Tags: ['winter', 'waterproof', 'new']
# # Restock Date: 2026-10-14 15:40:09.023000
# #--------------------------------------------



# Exercise 10
# Challenge: delete all orders with status new placed before 2026-03-20. Count them first. Hint:
# dates in filters are datetime objects, like datetime(2026, 3, 20).
# Expected: 2, then 2 deleted

# from datetime import datetime
# from pymongo import MongoClient
# client = MongoClient("mongodb://localhost:27017/")
# db = client["webshop"]

# filter_query = {
#     "status": "new",
#     "order_date": {"$lt": datetime(2026, 3, 20)}
# }

# count_before = db.orders.count_documents(filter_query)
# print(f"Orders found: {count_before}")

# delete_result = db.orders.delete_many(filter_query)
# print(f"Deleted: {delete_result.deleted_count}")

# Orders found: 2
# Deleted: 2
#------------------------------------------------------