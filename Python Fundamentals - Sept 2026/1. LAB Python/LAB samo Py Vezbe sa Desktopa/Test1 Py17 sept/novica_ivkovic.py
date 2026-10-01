# ==================================================
# TASK 1
# ==================================================

# products = [
#     {"name": "Laptop", "price": 12000, "stock": 4},
#     {"name": "Mouse", "price": 350, "stock": 0},
#     {"name": "Keyboard", "price": 800, "stock": 6},
#     {"name": "Monitor", "price": 3200, "stock": 3},
#     {"name": "Headset", "price": 950, "stock": 0},
#     {"name": "Webcam", "price": 1100, "stock": 5}
# ]

# # 1. Loop through the products.
# # 2. Print the name of every product that is in stock.
# # 3. Calculate the total value of all products in stock.
# #    The value of a product is price * stock.
# # 4. Print the total value.
# # 5. Keep track of which in-stock product has the highest price
# #    without using max(), and print its name.


# # Write your solution below:

# # 1. Loop through the products.
# # 2. Print the name of every product that is in stock.

# for product in products:
#     if product["stock"] > 0:
#         print(f"The list of available products: ", {product["name"]})

# # 3. Calculate the total value of all products in stock.
# #    The value of a product is price * stock.
# # 4. Print the total value.

# total = 0

# for product in products:
#       total += product["price"]

# print(f"Total value of all products in stock: ", total)


# # 5. Keep track of which in-stock product has the highest price
# #    without using max(), and print its name.

# highest_price = 0

# for product in products:
#      if product["price"] > highest_price:
#           highest_price = product["price"]

# print(f"The product with the highest price in the stock is: ", {highest_price})


# ==================================================
# TASK 2
# ==================================================

# scores = [78, 92, 55, 81, 67, 95, 73]

# # Create a function called calculate_average that:
# # - receives a list of scores
# # - calculates and returns the average score
# #
# # Create another function called create_result that:
# # - receives a list of scores
# # - uses calculate_average()
# # - returns "PASS" if the average is 70 or higher
# # - otherwise returns "FAIL"
# #
# # Call create_result() using the scores above.
# # Print both the average score and the final result.


# # Write your solution below:

# def calculate_average (list_of_scores):
#     if not list_of_scores:
#         return 0      # we want to ensure: - receives a list of scores
#     return sum(list_of_scores)/len(list_of_scores)

# # print (calculate_average(scores)) # test if function works

# def create_result (list_of_scores):
#     if not list_of_scores:
#             return 0      # we want to ensure: - receives a list of scores
#     else:
#          average = calculate_average(list_of_scores)
#          #  print(average) - test average
#     return ("PASS" if average >= 70 else "FAIL")

# average = round(calculate_average(scores),2)

# print (f"Average score is: {average} and final result is: {create_result(scores)}")




# ==================================================
# TASK 3
# ==================================================

# product_prices = [250, 400, 150, 700]

# order_settings = {
#     "discount": 10,
#     "shipping": 49,
#     "priority": True
# }

# # Create a function called calculate_order that:
# # - receives a customer name as a normal parameter
# # - receives any number of product prices using *args
# # - receives optional settings using **kwargs
# # - calculates the subtotal of all product prices
# # - applies the discount percentage if "discount" exists
# # - adds shipping if "shipping" exists
# # - returns a dictionary containing:
# #       customer
# #       subtotal
# #       final_total
# #       settings
# #
# # Call the function using:
# # - customer name "Anna"
# # - the values from product_prices using unpacking
# # - the values from order_settings using dictionary unpacking
# #
# # Print the returned dictionary.


# # Write your solution below:

# def calculate_order(customer, *prices,**settings):

#     subtotal = 0

#     for price in prices:
#         subtotal += price
#     # or subtotal = sum(prices)
    
#     final_total = 0.0

#     if "discount" in settings:
#         discount_percent = settings["discount"]
#         final_total = subtotal - final_total * (discount_percent / 100)

#     if "shipping" in settings:
#         final_total += settings["shipping"]

#     return {
#         "customer": customer,
#         "subtotal": subtotal,
#         "final_total": final_total,
#         "settings" : settings
#     }

# result = calculate_order("Anna", *product_prices, **order_settings)

# print(result)



# ==================================================
# TASK 4
# ==================================================

players = [
    {"name": "  anna", "score": 85, "active": True},
    {"name": "DAVID ", "score": 72, "active": False},
    {"name": " sara ", "score": 94, "active": True},
    {"name": "LEO", "score": 67, "active": True},
    {"name": " emma", "score": 88, "active": True},
    {"name": "OSCAR ", "score": 76, "active": False}
]

# 1. Create a new list containing normalized player names.
#    Remove unnecessary whitespace and use consistent capitalization.
#    Use a list comprehension.
#
# 2. Create a new list containing only the active players
#    with a score of 80 or higher.
#    Use a list comprehension.
#
# 3. Sort the original players by score from highest to lowest.
#    Use sorted() with a lambda.
#
# 4. Print the ranking in the following format:
#
#    1. Sara - 94
#    2. Emma - 88
#    ...
#
#    Generate the ranking numbers using enumerate().
#
# 5. Create a separate list containing the player names and
#    another list containing their scores.
#    Combine them using zip() and print each name together
#    with its score.


# Write your solution below:

# 1.
normalized_player_names = [player["name"].strip().capitalize() for player in players]

print(normalized_player_names)

# 2.
active_players = [
    player["name"].strip().capitalize()
    for player in players
    if player["active"] and player["score"] >= 80
]

print(active_players)

# 3. 
sorted_players = sorted(players, key=lambda player: player["score"], reverse=True)

for player in sorted_players:
    print(f"{player['name'].strip().capitalize()}: {player['score']}")

# 4. 
for rank, player in enumerate(sorted_players, start=1):
    tidy_name = player["name"].strip().capitalize()
    score = player["score"]
    print(f"{rank}. {tidy_name} - {score}")

# 5. 
player_names = [player["name"].strip().capitalize() for player in players] # list
player_scores = [player["score"] for player in players]  # list

for name, score in zip(player_names, player_scores):
    print(f"Player: {name} - Score: {score}")
