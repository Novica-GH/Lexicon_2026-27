##********************************************************************************************
#  Novica Ivkovic                                                                           *
#  Cours: System Developer Python and AI                                                    *
#  Oktober 16 2026 -  Day10. SQL second week - NoSQL- LAB 3
#
#                    --- Exercises: Design, aggregation and safe code ---
#********************************************************************************************


# Exercises 1 and 2 are written answers, and so is the last one. The rest are done in Python. 
# Put the header below at the top of every file. Start by running python seed_webshop.py 
# so everyone has the same data. Look back at the slides when you need the syntax.

# 1. Done reset of db - seed_webshop.py  executed!

#The header (at the top of every Python file):

# from pymongo import MongoClient
# client = MongoClient("mongodb://localhost:27017/")
# db = client["webshop"]
#-------------------------------------------------------


# Exercise 1
# Design: a library app shows a book page with the book's title, author and all its reviews. Many
# members borrow the same book. Would you embed or reference the reviews? The members?
# Explain in two sentences.
# Expected: written answer


# Reviews: I would embed the reviews inside the book document because they are always displayed together
# on the book's page, have a bounded size, and belong exclusively to that specific book.

# Members: I would reference the members using unique IDs in a separate collection because members 
# borrow multiple books over time 
# and their profile data needs to be updated independently in one central place.
#------------------------------------------------------------------------------


# Exercise 2
# Our orders copy the product name into each item. Give one advantage and one disadvantage of
# that copy.
# Expected: written answer


# Advantage: It improves read performance (denormalization) by allowing to generate an order receipt 
# instantly without needing extra queries or joins to look up the product name. 
# 
# Disadvantage: It introduces data duplication across documents, which increases storage requirements 
# and can lead to data inconsistency.
#---------------------------------------------------------------------------------------------


# Exercise 3
# 2.  Create a collection newsletter_signups with (1.) validation:
#  email is required and must be a string, 
# and # source can only be "web" or "store" (look up enum). 
# 3. Insert one valid and 
# 4. one invalid document.
# Expected: the second insert fails


# from pymongo import MongoClient
# from pymongo.errors import OperationFailure
# client = MongoClient("mongodb://localhost:27017/")
# db = client["webshop"]


# if "newsletter_signups" in db.list_collection_names():
#     db.newsletter_signups.drop()

# # 1. Define JSON Schema Validation Rules
# validator = {
#     "$jsonSchema": {
#         "bsonType": "object",
#         "required": ["email"],
#         "properties": {
#             "email": {
#                 "bsonType": "string",
#                 "description": "Email must be a string and is required"
#             },
#             "source": {
#                 "enum": ["web", "store"],
#                 "description": "Source can only be 'web' or 'store'"
#             }
#         }
#     }
# }

# # 2. Create collection with validator
# db.create_collection("newsletter_signups", validator=validator)
# print("Collection 'newsletter_signups' created with validation rules.")

# # 3. Insert ONE VALID document
# valid_doc = {
#     "email": "user@example.com",
#     "source": "web"
# }
# try:
#     res = db.newsletter_signups.insert_one(valid_doc)
#     print(f"Valid insert succeeded with _id: {res.inserted_id}")
# except OperationFailure as e:
#     print(f"Valid insert failed: {e}")

# #  Collection 'newsletter_signups' created with validation rules.
# #  Valid insert succeeded with _id: 6ad233babacf0dc5d9168bc5

# # 4. Insert ONE INVALID document (invalid source 'app' not in enum)
# invalid_doc = {
#     "email": "baduser@example.com",
#     "source": "app"  # 'app' is not allowed by enum
# }
# try:
#     db.newsletter_signups.insert_one(invalid_doc)
#     print("Invalid insert unexpectedly succeeded!")
# except OperationFailure as e:
#     print("\nExpected error caught for invalid document:")
#     print(e.details["errmsg"])

# Expected error caught for invalid document:
# Document failed validation
#--------------------------------------------------------------



# Exercise 4
# How many customers live in each city? Use $group. Biggest city first.
# Expected: 6 rows (one with _id None)


# from pymongo import MongoClient
# client = MongoClient("mongodb://localhost:27017/")
# db = client["webshop"]


# # Aggregation pipeline: GROUP BY city and count customers, then SORT DESC
# pipeline = [
#     {
#         "$group": {
#             "_id": "$city",
#             "count": {"$sum": 1}
#         }
#     },
#     {
#         "$sort": {
#             "count": -1
#         }
#     }
# ]

# results = list(db.customers.aggregate(pipeline))

# for row in results:
#     city = row["_id"] if row["_id"] is not None else "None"
#     print(f"City: {city:<10} -> Customers: {row['count']}")


# # City: Uppsala    -> Customers: 3
# # City: Göteborg   -> Customers: 2
# # City: Stockholm  -> Customers: 2
# # City: Malmö      -> Customers: 1
# # City: None       -> Customers: 1
# # City: Västerås   -> Customers: 1
#------------------------------------------------------------



# Exercise 5
# What is the cheapest and the most expensive product in each category? 
# Use $min and $max.
# Expected: 3 rows


# from pymongo import MongoClient
# client = MongoClient("mongodb://localhost:27017/")
# db = client["webshop"]


# pipeline = [
#     {
#         "$group": {
#             "_id": "$category",
#             "min_price": {"$min": "$price"},
#             "max_price": {"$max": "$price"}
#         }
#     },
#     {
#         "$sort": {
#             "_id": 1
#         }
#     }
# ]

# results = list(db.products.aggregate(pipeline))

# for row in results:
#     print(f"Category: {row['_id']} | Min Price: {row['min_price']} kr | Max Price: {row['max_price']} kr")

# # City: Uppsala    -> Customers: 3
# # City: Göteborg   -> Customers: 2
# # City: Stockholm  -> Customers: 2
#-----------------------------------------------------------------------



# Exercise 6
# How many orders does each customer have (all statuses)? 
# Show only customers with 2 or more orders. 
# Hint: $match after $group works like HAVING.
# Expected: 5 rows


# from pymongo import MongoClient
# client = MongoClient("mongodb://localhost:27017/")
# db = client["webshop"]


# pipeline = [
#     {
#         "$group": {
#             "_id": "$customer_id",
#             "order_count": {"$sum": 1}
#         }
#     },
#     {
#         "$match": {
#             "order_count": {"$gte": 2}
#         }
#     },
#     {
#         "$sort": {
#             "order_count": -1
#         }
#     }
# ]

# results = list(db.orders.aggregate(pipeline))

# for row in results:
#     print(f"Customer ID: {row['_id']} -> Orders: {row['order_count']}")

# # Customer ID: 2 -> Orders: 3
# # Customer ID: 1 -> Orders: 3
# # Customer ID: 4 -> Orders: 2
# # Customer ID: 3 -> Orders: 2
# # Customer ID: 6 -> Orders: 2
#-----------------------------------------------------------



# Exercise 7
# For each order, show the _id and the number of items in it. 
# Use $project with $size.
# Expected: 15 rows


# from pymongo import MongoClient
# client = MongoClient("mongodb://localhost:27017/")
# db = client["webshop"]


# pipeline = [
#     {
#         "$project": {
#             "_id": 1,
#             "num_items": {"$size": "$items"}
#         }
#     }
# ]

# results = list(db.orders.aggregate(pipeline))

# for row in results:
#     print(f"Order ID: {row['_id']:<5} | Number of items: {row['num_items']}")


# # Order ID: 1     | Number of items: 2
# # Order ID: 2     | Number of items: 1
# # Order ID: 3     | Number of items: 1
# # Order ID: 4     | Number of items: 2
# # Order ID: 5     | Number of items: 1
# # Order ID: 6     | Number of items: 2
# # Order ID: 7     | Number of items: 1
# # Order ID: 8     | Number of items: 2
# # Order ID: 9     | Number of items: 1
# # Order ID: 10    | Number of items: 2
# # Order ID: 11    | Number of items: 1
# # Order ID: 12    | Number of items: 2
# # Order ID: 13    | Number of items: 1
# # Order ID: 14    | Number of items: 2
# # Order ID: 15    | Number of items: 2
#------------------------------------------


# Exercise 8
# How many units of each category have been sold? 
# Products' categories are not in the orders, so you need: $unwind and  $lookup to products. 
# Skip cancelled orders.
# Expected: 3 rows


from pymongo import MongoClient
client = MongoClient("mongodb://localhost:27017/")
db = client["webshop"]


pipeline = [
    #  Skip cancelled orders
    {
        "$match": {
            "status": {"$ne": "cancelled"}
        }
    },
    #   Deconstruct the items array so each item becomes a separate document
    {
        "$unwind": "$items"
    },
    #   Join with products collection on product_id to get product category
    {
        "$lookup": {
            "from": "products",
            "localField": "items.product_id",
            "foreignField": "_id",
            "as": "product_info"
        }
    },
    #   Deconstruct product_info array resulting from $lookup
    {
        "$unwind": "$product_info"
    },
    #   Group by category and sum up quantities sold
    {
        "$group": {
            "_id": "$product_info.category",
            "total_units_sold": {"$sum": "$items.quantity"}
        }
    },
    #   Sort results by total_units_sold in descending order
    {
        "$sort": {
            "total_units_sold": -1
        }
    }
]

results = list(db.orders.aggregate(pipeline))

for row in results:
    print(f"Category: {row['_id']} -> Total Units Sold: {row['total_units_sold']}")


# Category: Clothing -> Total Units Sold: 21
# Category: Accessories -> Total Units Sold: 7
# Category: Shoes -> Total Units Sold: 4
# #--------------------------------------------------


# Exercise 9
# Revenue per status: for each status, the total of quantity times unit_price.
# Expected: 4 rows




# Exercise 10
# Challenge: which tags are the most common? Show each tag and how many products have it,
# most common first.
# Expected: 7 tags




# Exercise 11
# Webshop: this function is unsafe. Explain why, and fix it.
# def find_orders(request_text):
# data = json.loads(request_text)
# return list(db.orders.find({"status": data["status"]}))
# Test with '{"status": "new"}' and with '{"status": {"$ne": "x"}}'.
# Expected: 4, then 0 (the unsafe version gives 15)





# Exercise 12
# Webshop: write a function products_under(text) for a search box. The text comes from the user,
# so convert it with float(). If the conversion fails, catch the ValueError, print 'Please enter a
# number.' and return an empty list. Otherwise return the name and price of all products cheaper
# than that price.
# Test it with "300", "abc" and '{"$gt": 0}'.
# Expected: 5 products for "300". For the other two: Please enter a number.




# Exercise 13
# What happens when the database is down? Make a second client that points to the wrong port:
# MongoClient("mongodb://localhost:27018/", serverSelectionTimeoutMS=2000). Count the
# products with it inside try/except, catch ServerSelectionTimeoutError (from pymongo.errors) and
# print a friendly message instead of a crash. Then do the same count with the normal client.
# Expected: After about 2 seconds your friendly message. Then 12 with the normal client.




# Exercise 14
# Written answer: personal data in the webshop. Which fields in customers are personal data?
# Orders only store customer_id, not the customer's name or email. Why is that good when a
# customer asks to be deleted? A classmate wants to copy the customer's email and city into every
# order to make reading faster. What do you answer? Write 4-6 sentences.
# Expected: A written answer. Compare with a classmate.

