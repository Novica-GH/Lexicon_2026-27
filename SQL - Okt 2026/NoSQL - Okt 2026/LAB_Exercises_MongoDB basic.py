# from pymongo import MongoClient
# client = MongoClient("mongodb://127.0.0.1:27017/", serverSelectionTimeoutMS=3000)
# print(client.list_database_names())


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


# Exercise 2
# Print the first and last name of every customer who lives in Göteborg.
# Expected: 2 customers


# Exercise 3
# Python: print the name and price of every product, one per line.
# Expected: 12 lines


# Exercise 4
# Python: how many customers live in Uppsala? Use count_documents.
# Expected: 3


# Exercise 5
# Python: find the product named Sandals with find_one and print how many are in stock.
# Expected: 22


# Exercise 6
# Python: print the first name of every customer who gets the newsletter (newsletter is True).
# Expected: 3 names


# Exercise 7
# Python: add yourself as a customer with insert_one, without an _id. Print the inserted_id. Then find
# yourself again with find_one and your email, and print yourself with pprint.
# Expected: an ObjectId, then your document


# Exercise 8
# Python: add two new products with insert_many (give them _id 13 and 14, and include tags). Then
# print how many products there are.
# Expected: 14


# Exercise 9
# Python: print every customer as 'First Last (City)'. Customers without a city should show
# (unknown). Hint: dict.get().
# Expected: 10 lines



# Exercise 10
# Challenge: print every order as 'Order 1: 2 items'. Hint: an order's items is a list, and len() works
# on lists.
# Expected: 15 lines



