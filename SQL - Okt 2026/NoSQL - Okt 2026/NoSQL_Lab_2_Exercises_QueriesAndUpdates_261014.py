#-------------------------------------------------------


# Exercises: Queries and updates
# Use Python with the header from the code-along. Start by running python seed_webshop.py.
# Exercises 8 to 10 change data: run the seed script again when you are done.

# The header (at the top of every Python file):
# from pymongo import MongoClient
# client = MongoClient("mongodb://localhost:27017/")
# db = client["webshop"]

# Exercise 1
# Show the name and price of all products that cost more than 1000 kr.
# Expected: 3 products


# from pymongo import MongoClient
# client = MongoClient("mongodb://localhost:27017/")
# db = client["webshop"]


# for product in db.products.find({"price": {"$gt": 1000}}):
#     print(f"{product['name']}: {product['price']} kr")


# Exercise 2
# Show all orders that are not delivered. Use $ne. Print the _id and status.
# Expected: 8 orders

# from pymongo import MongoClient
# client = MongoClient("mongodb://localhost:27017/")
# db = client["webshop"]

# for order in db.orders.find({"status": {"$ne": "delivered"}}):
#     print(f"Order {order['_id']}: {order['status']}")


# Exercise 3
# Show customers who live in Stockholm or Malmö, using $in.
# Expected: 3 customers

# from pymongo import MongoClient
# client = MongoClient("mongodb://localhost:27017/")
# db = client["webshop"]

# for customer in db.customers.find({"city": {"$in": ["Stockholm", "Malmö"]}}):
#     print(f"{customer['first_name']} {customer['last_name']} ({customer['city']})")



# Exercise 4
# Which products are white? Use dot notation.
# Expected: 3 products

from pymongo import MongoClient
client = MongoClient("mongodb://localhost:27017/")
db = client["webshop"]

for product in db.products.find({"specs.color": "White"}):
    print(f"{product['name']} - {product['specs']['color']}")




# Exercise 5
# Which products have the tag sport? Show only name and tags, without _id.
# Expected: 3 products

# Exercise 6
# Show the 5 cheapest products, cheapest first. Only name and price.
# Expected: 5 products


# Exercise 7
# Which orders contain product 2 (T-shirt White)? Hint: dot notation works on arrays of objects too:
# "items.product_id".
# Expected: 4 orders


# Exercise 8
# Raise the price of all Accessories by 20 kr with $inc. Then print the Accessories with their new
# prices.
# Expected: 4 products, each 20 kr more

# Exercise 9
# Add the tag "new" to the Rain Jacket without creating duplicates, and give it a field restock_date
# with today's date (use datetime.now()).
# Expected: 1 product with the new tag and field (the time will be yours)


# Exercise 10
# Challenge: delete all orders with status new placed before 2026-03-20. Count them first. Hint:
# dates in filters are datetime objects, like datetime(2026, 3, 20).
# Expected: 2, then 2 deleted