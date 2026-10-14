#--------------------------------------

# Exercises: MongoDB basics
# Do all exercises in Python, with the header from the code-along at the top of your file. Start by
# running python seed_webshop.py. Exercises 7 and 8 add data: when you are done, run python
# seed_webshop.py to reset the webshop.

#The header (at the top of every Python file):

# from pymongo import MongoClient
# client = MongoClient("mongodb://localhost:27017/")
# db = client["webshop"]

# Exercise 1
# Print the name of every product in the Accessories category.
# Expected: 4 names


# from pymongo import MongoClient
# client = MongoClient("mongodb://localhost:27017/")
# db = client["webshop"]

# for product in db.products.find({"category": "Accessories"}):
#     print(product["name"])
#     #print(product)

# for product in db.products.find({"category":" "}):
#     print(product)



# Exercise 2
# Print the first and last name of every customer who lives in Göteborg.
# Expected: 2 customers

# from pymongo import MongoClient
# client = MongoClient("mongodb://localhost:27017/")
# db = client["webshop"]


# for customer in db.customers.find({"city": "Göteborg"}):
#     print(f"{customer['first_name']} {customer['last_name']}")




# Exercise 3
# Python: print the name and price of every product, one per line.
# Expected: 12 lines

# from pymongo import MongoClient
# client = MongoClient("mongodb://localhost:27017/")
# db = client["webshop"]

# for product in db.products.find():
#     print(f"{product['name']}: {product['price']} kr")



# Exercise 4
# Python: how many customers live in Uppsala? Use count_documents.
# Expected: 3

# from pymongo import MongoClient
# client = MongoClient("mongodb://localhost:27017/")
# db = client["webshop"]


# count = db.customers.count_documents({"city": "Uppsala"})

# print(f"Number of customers in Uppsala: {count}")



# Exercise 5
# Python: find the product named Sandals with find_one and print how many are in stock.
# Expected: 22

# from pymongo import MongoClient
# client = MongoClient("mongodb://localhost:27017/")
# db = client["webshop"]


# product = db.products.find_one({"name": "Sandals"})

# if product:
#     print(f"Stock for Sandals: {product['stock']}")



# Exercise 6
# Python: print the first name of every customer who gets the newsletter (newsletter is True).
# Expected: 3 names

# from pymongo import MongoClient
# client = MongoClient("mongodb://localhost:27017/")
# db = client["webshop"]

# for customer in db.customers.find({"newsletter": True}):
#     print(customer["first_name"])



# Exercise 7
# Python: add yourself as a customer with insert_one, without an _id. Print the inserted_id. Then find
# yourself again with find_one and your email, and print yourself with pprint.
# Expected: an ObjectId, then your document


# from pymongo import MongoClient
# from pprint import pprint
# client = MongoClient("mongodb://localhost:27017/")
# db = client["webshop"]

# new_customer = {                # New customer insert
#     "first_name": "Novica",
#     "last_name": "Ivković",
#     "email": "novica@ivkovic.com",
#     "city": "Stockholm",
#     "newsletter": True
# }

# result = db.customers.insert_one(new_customer)

# # print test
# print(f"Inserted ID: {result.inserted_id}")

# # finding customer via email
# me = db.customers.find_one({"email": "novica@example.com"})
# pprint(me)

#python seed_webshop.py





# Exercise 8
# Python: add two new products with insert_many (give them _id 13 and 14, and include tags). Then
# print how many products there are.
# Expected: 14

# from pymongo import MongoClient
# client = MongoClient("mongodb://localhost:27017/")
# db = client["webshop"]

# new_products = [
#     {
#         "_id": 13,
#         "name": "Running Shoes",
#         "category": "Footwear",
#         "price": 899,
#         "stock": 15,
#         "tags": ["sports", "footwear", "running"]
#     },
#     {
#         "_id": 14,
#         "name": "Leather Belt",
#         "category": "Accessories",
#         "price": 349,
#         "stock": 20,
#         "tags": ["leather", "accessories", "style"]
#     }
# ]


# db.products.insert_many(new_products)


# total_products = db.products.count_documents({})
# print(f"Total products: {total_products}")



# Exercise 9
# Python: print every customer as 'First Last (City)'. Customers without a city should show
# (unknown). Hint: dict.get().
# Expected: 10 lines

# from pymongo import MongoClient
# client = MongoClient("mongodb://localhost:27017/")
# db = client["webshop"]


# for customer in db.customers.find():
#     first = customer.get("first_name", "")
#     last = customer.get("last_name", "")
#     city = customer.get("city", "unknown")
    
#     print(f"{first} {last} ({city})")




# Exercise 10
# Challenge: print every order as 'Order 1: 2 items'. Hint: an order's items is a list, and len() works
# on lists.
# Expected: 15 lines


# from pymongo import MongoClient
# client = MongoClient("mongodb://localhost:27017/")
# db = client["webshop"]


# for order in db.orders.find():
#     order_id = order.get("_id")
#     items_count = len(order.get("items", []))
    
#     print(f"Order {order_id}: {items_count} items")
