#********************************************************************************************
#  Novica Ivkovic                                                                           *
#  Cours: System Developer Python and AI                                                    *
#  September 16 2026 - LAB 6                                                                *
#             Today's study goal is: REPETIION - COMPREHENSION                              *
#********************************************************************************************


#********************************************************************************************
#  LAB 6                     Part A - List comprehension                                    *
#********************************************************************************************

# Part A.1. Create squares for numbers 1-20 using a normal loop, then a list comprehension.
#------------------------------------------------------------------------------------------

# squares_loop = []

# for number in range (1, 21):
#     squares_loop.append(number **2)

# print("We are going through normal loop:", squares_loop)

# squares_comprehension = [number **2 for number in range(1, 21)]

# print("We are going through list comprehension:", squares_comprehension)


# # Part A.2. Create a list containing only even numbers from 1-100
# #----------------------------------------------------------------
     
# ## 1st way - classic

# even_numbers =[]

# for number in range (1,101):
#     if number % 2 == 0 :  
#         even_numbers.append(number)

# print(even_numbers)

# # 2nd way - by a list comprehension

# even_numbers =[number for number in range(2,101,2)] # takes, begining from 2 with step 2, and goes to 100.
# print(even_numbers)

# # 3rd way - by a list comprehension with if condition (mix of 1 and 2)

# even_numbers =[number for number in range(1,101) if number % 2 == 0] # takes, begining from 2 with step 2, and goes to 100.
# print(even_numbers)



# # Part A.3 Convert a list of names to stripped, title-cased names.
# #-----------------------------------------------------------------

# # 1st way - classic by for-loop

# start_list = ["Ada", "  bob", "  GvidO  ", " luCIA  ", "SteFAN  ", " Petar", "   EMIL"]

# tidied_list =[]

# for name in start_list:
#     tidy = name.strip().title()
#     tidied_list.append(tidy)

# print(tidied_list)

# # # 2nd way - by a list comprehension

# start_list = ["Ada", "  bob", "  GvidO  ", " luCIA  ", "SteFAN  ", " Petar", "   EMIL"]

# stripped_list = [name.strip().title() for name in start_list]

# print(stripped_list)



# Part A.4 Given scores, create a list containing only passing scores.
#---------------------------------------------------------------------

##via - list comprehension

# scores = [1, 3, 4, 5, 7, 9, 6, 3, 10, 4, 8, 9]

# passing_scores = [score for score in scores if score > 5]

# print(scores)
# print(passing_scores)


# Part A.5 Create labels such as 'PASS'/'FAIL' for every score using a conditional expression in a comprehension.
#----------------------------------------------------------------------------------------------------------------

# scores = [1, 3, 4, 5, 7, 9, 6, 3, 10, 4, 8, 9]


# labels = ["PASS" if score > 5 else "FAIL" for score in scores]

# print(labels)
  
        
# Part A.6. Rewrite three earlier loop-based transformations from Lessons 2-4 as comprehensions.
#-----------------------------------------------------------------------------------------------

# study_sessions = [
#     {"subject": "Python Programming", "minutes": 45},
#     {"subject": "Mathematics", "minutes": 60},
#     {"subject": "Database Systems", "minutes": 30},
#     {"subject": "Python Programming", "minutes": 90},
#     {"subject": "Web Development", "minutes": 50}
# ]

# # Earlier loop with if session["minutes"] > 45
# long_sessions = [s for s in study_sessions if s["minutes"] > 45]

# # Earlier loop appending s["subject"].upper() to a new list
# subject_names = [s["subject"].upper() for s in study_sessions]

# # Earlier: loop calculating hours and updating a dictionary
# session_hours = {s["subject"]: s["minutes"] / 60 for s in study_sessions}


# print("1. Long Sessions (>45 mins):")
# print(long_sessions)

# print("\n2. Upper Case Subjects:")
# print(subject_names)

# print("\n3. Subject Duration in Hours (Dict):")
# print(session_hours)





#***********************************************************************************************
#  LAB 6                Part B - Dictionary and set comprehensions                             *
#***********************************************************************************************


# Part B.1 Create a dictionary mapping numbers 1-10 to their squares.
#--------------------------------------------------------------------

# squares_dict = {number: number**2 for number in range (1, 11)}

# print(squares_dict)



# Part B.2 Given a list of words, create a dictionary mapping each word to its length.
#-------------------------------------------------------------------------------------

# start_list = ["Ada", "bob", "Gvido", "Lucia", "Stefan", "Petar", "EMIL"]

# word_by_length = {word: len(word) for word in start_list}

# print(word_by_length)




# Part B.3 Given a list with duplicates, create a set comprehension containing lowercase normalized values.
#----------------------------------------------------------------------------------------------------------


# start_list = ["Ada", "bob", "Gvido", "Lucia   ", "   Stefan", "Petar ", "EMIL"]

# normalized_set = {item.strip().lower() for item in start_list}

# print(normalized_set)


# Part B.4 Create a dictionary of only product whose price is below a chosen threshold.
#--------------------------------------------------------------------------------------


# prices = {
#     "apple" : 10,
#     "banana" : 5,
#     "orange" : 8,
#     "mango" : 14,
#     "avokado" : 12,
#     "strawberry": 15,
#     "pears" : 7,
#     "watermelon": 9
# }

# cheaper_product = {product : price for product, price in prices.items() if (price < 10)}

# print(cheaper_product)



# Part B.5 Create a dictinary mapping student names to PASS/FAIL from a list of student dictionaries.
#----------------------------------------------------------------------------------------------------


# students  = [
#     {"name": "Anna", "score": 85},
#     {"name": "Bob", "score": 50},
#     {"name": "Charlie", "score": 65},
#     {"name": "Diana", "score": 75}
# ]

# students_status = {student["name"] : ("PASS" if student["score"] >= 70 else "FAIL") for student in students}

# print(students_status)
                  

    
#****************************************************************************************************
#  LAB 6                           PART C - enumerate                                               *
#****************************************************************************************************


# C.1. Print a playlist with numbering starting at 1 using enumerate.
#--------------------------------------------------------------------


# playlist = [
#     "Waterloo - ABBA",
#     "Like a Virgin - Madonna",
#     "Beat it - Michael Jackson",
#     "I will always love you - Whitney Houston"
# ]


# for number, track in enumerate(playlist, start=1):
#     print(f"{number}. {track}")



# C.2 Given a list of tasks, print 'Task 1:', 'Task 2:' etc.
#-----------------------------------------


# tasks = [
#     "Insert new element in a list.",
#     "Replace the first element in the list with: 'PrimeTime'.",
#     "Invert the first and last elements of the list.",
#     "Delete the last element in the list"
# ]

# for number, task in enumerate(tasks, start=1):
#      print(f"Task {number}: {task}")




# C.3 Find and print indexes of all values above a threshold.
#------------------------------------------------------------


# values = [10, 20, 25, 40, 70, 55, 99, 30, 17, 87, 5]
# threshold = 40

# clasic with for-loop:

# print(f"Print the values above {threshold}:")
# for index, value in enumerate(values):
#     if value > threshold:
#         print(f"Index {index}: {value}")

# with comprehension:

# print(f"Print the values above {threshold}:")

# print("\n".join([f"Index {index}: {value}" for index, value in enumerate(values) if value > threshold]))


# C.4 Rewrite a range (len(...)) loop using enumerate and explain why the new version is clearer.
#------------------------------------------------------------------------------------------------

# names = ["Ada", "bob", "Gvido", "Lucia", "Stefan", "Petar", "EMIL", "Mikelandjelo"]

# # via range(len(...))

# for i in range(len(names)):
#     name = names[i]
#     print(f"Name {i + 1}: {name}")

# # via enumerate

# for i, name in enumerate(names, start=1):
#     print(f"Name {i}: {name}")



#************************************************************************************************
#  LAB 6                         PART D - zip and unpacking                                     *
#************************************************************************************************

# D.1 Combine separate name and score lists using zip and print each pair.
#-------------------------------------------------------------------------

# names = ["Anna", "Bob", "Diana", "Leo", "Emil", "Stefan"]
# scores = [85, 75, 94, 65, 57, 72]

# for name, score in zip(names, scores):
#     print(f"Player: {name} - Score: {score}")


# D.2 Create a dictionary using dict(zip(keys, values)).
#-------------------------------------------------------

keys = ["Anna", "Bob", "Diana", "Leo", "Emil", "Stefan"]
values = [85, 75, 94, 65, 57, 72]

key_values = dict(zip(keys, values))
print(key_values)


# D.3 Combine three lists: product name, price and stock.
#--------------------------------------------------------

# names = ["Laptop", "Printer", "Mouse", "Keyboard", "UPS"]
# prices = [7000, 1550, 200, 300, 3000]  # kr
# stock = [4, 5, 16, 20, 3]

# combined_products = list(zip(names, prices, stock))
# print(combined_products)

# /// Result - printed output: ///
# [('Laptop', 7000, 4), ('Printer', 1550, 5), ('Mouse', 200, 16), ('Keyboard', 300, 20), ('UPS', 3000, 3)]


# D.4 Investigate what happens when zipped lists have different lengths.
#-----------------------------------------------------------------------

# names = ["Laptop", "Printer", "Mouse", "Keyboard", "UPS"]
# prices = [7000, 1550, 200, 300]  # kr
# stock = [4, 5, 16, ]

# combined_products = list(zip(names, prices, stock))
# print(combined_products)

# /// Result - printed output: ///
# [('Laptop', 7000, 4), ('Printer', 1550, 5), ('Mouse', 200, 16)]

# Commentar: Combination of lists with different lengths gives
#            intersection of those lists, ie. number of elements in result list
#            is goint to be equal to numer of elements of shortests list.



# D.5 Use tuple unpacking directly in a for loop over zipped data.
#-----------------------------------------------------------------

# names = ["Laptop", "Printer", "Mouse", "Keyboard", "UPS"]
# prices = [7000, 1550, 200, 300]  # kr
# stock = [4, 5, 16, ]

# for name, price, quantity in zip(names, prices, stock):
#     tuples = (name, price, quantity)
#     print (tuples)

# print(type(tuples))

# /// Result - printed output: ///
# ('Laptop', 7000, 4)
# ('Printer', 1550, 5)
# ('Mouse', 200, 16)
# <class 'tuple'>

# D.6 Swap two variables without a temporary variable.
#-----------------------------------------------------

# 1. Swap with a temporary variable: 
# x = 5
# y = 10
# print(x, y)
# temp = x
# x = y
# y = temp
# print(x, y)

# /// Result - printed output: ///
# 5 10
# 10 5

# 2. Swap without a temporary variable - with tuple unpackning
x = 7
y = 11
# print(x, y)
# x, y = y, x
# print(x, y)

# /// Result - printed output: ///
# 7 11
# 11 7


#******************************************************************************************************
#  LAB 6                             Part E - sorted and lambda                                       *
#******************************************************************************************************


# E.1 Sort a list of words by length using sorted(..., key=...)
#--------------------------------------------------------------

# words = ["python", "java", "pascal", "C", "C#", "C++", "COBOL", ]

# sorted_words = sorted(words, key=len)

# print(sorted_words)

# /// Result - printed output: ///
#    ['C', 'C#', 'C++', 'java', 'COBOL', 'python', 'pascal']


# E.2 Sort a list of student dictionaries by score ascending and descending.
#---------------------------------------------------------------------------

# students  = [
#     {"name": "Anna", "score": 85},
#     {"name": "Bob", "score": 50},
#     {"name": "Charlie", "score": 65},
#     {"name": "Diana", "score": 75}
# ]

# students_asc = sorted(students, key=lambda student: student["score"])
# students_desc = sorted(students, key=lambda student: student["score"], reverse=True)

# print("Ascending list of students by score: ", students_asc)
# print("Descending list of students by score: ", students_desc)

# /// Result - printed output: ///
#  Ascending list of students by score:  [{'name': 'Bob', 'score': 50}, {'name': 'Charlie', 'score': 65}, 
#                                         {'name': 'Diana', 'score': 75}, {'name': 'Anna', 'score': 85}]
# Descending list of students by score:  [{'name': 'Anna', 'score': 85}, {'name': 'Diana', 'score': 75},
#                                         {'name': 'Charlie', 'score': 65}, {'name': 'Bob', 'score': 50}]


# E.3 Sort products by price using a lambda.
#-------------------------------------------

# fruts = [
#     {"product": "apple",  "price" : 10},
#     {"product": "banana", "price" : 15},
#     {"product": "mango",  "price" : 20},
#     {"product": "pears",  "price" : 12}
# ]

# sort_fruts_by_price = sorted(fruts, key=lambda fruct: fruct["price"] )

# print(sort_fruts_by_price)

# /// Result - printed output: ///
#     [{'product': 'apple', 'price': 10}, {'product': 'pears', 'price': 12}, 
#      {'product': 'banana', 'price': 15}, {'product': 'mango', 'price': 20}]


# E.4 Sort people by last name when each item is a dictionary containing first_name and last_name.
#-------------------------------------------------------------------------------------------------


# E.5 Write a normal named function for a sort key, then replace it with lambda.
#      Compare when each is clearer.
#------------------------------------------------------------------------------




#*******************************************************************************************************
#  LAB 6                      Part F - Applied challenge: Data cleanup                                 *
#*******************************************************************************************************


# F.1 Start with a list of at least twelve messy dictionaries representing product:
#     inconsistent name casing/spacing, category, price and stock.
#----------------------------------------------------------------------------------

# names = ["Laptop", "Printer", "Mouse", "Keyboard", "UPS"]
# prices = [7000, 1550, 200, 300]  # kr
# stock = [4, 5, 16, ]

# products = [
#     {"name": "  Laptop  ", "category": "Electronics", "price": 7000.00, "stock": 4},
#     {"name": "Printer  ", "category": "Electronics", "price": 1550.00, "stock": 5},
#     {"name": "   Mouse", "category": "Electronics", "price": 200.00, "stock": 16},
#     {"name": "UPS  ", "category": "Electronics", "price": 3000.00, "stock": 3},
#     {"name": "wireless mouse", "category": "electronics", "price": "25.50", "stock": 0},
#     {"name": " KEYBOARD ", "category": "ELECTRONICS", "price": 45.0, "stock": 12},
#     {"name": "monitor 27 inch", "category": "Electronics ", "price": 300.00, "stock": 3},
#     {"name": "  usb-c cable ", "category": "Accessories", "price": 12.99, "stock": 50},
#     {"name": " desk lamp", "category": "home & kitchen", "price": 35.00, "stock": 0},
#     {"name": "BLUETOOTH speaker", "category": "Electronics", "price": 89.99, "stock": 15},
#     {"name": "  water bottle  ", "category": "fitness", "price": 18.50, "stock": 20},
#     {"name": "notebook A5", "category": "stationery", "price": 4.50, "stock": 100}  
# ]

# # F.2 Create a cleanded list where names/categories are normalized. Use comprehensions where readable.
# #-----------------------------------------------------------------------------------------------------

# cleaned_list = [
#     { 
#         "name": prod["name"].strip().title(),
#         "category": prod["category"].strip().title(),
#         "price": float(prod["price"]),
#         "stock": prod["stock"]
#     }
#     for prod in products
# ]

# print("\n   --- Cleanded list of the products:   ---\n")

# for item in cleaned_list:
#     print(item)

# # F.3 Create a list of in-stock products.
# #----------------------------------------

# in_stock_prod = [prod for prod in cleaned_list if prod["stock"] > 0]

# print("\n   ---  List of products in the stock:   ---\n")

# for item in in_stock_prod:
#     print(item)
# print()

# # F.4  Create a set of unique normalized categories.
# #---------------------------------------------------

# categories = {cat["category"].strip().title() for cat in products}

# print("\n   ---  Set of unique normalized categories:   ---\n")

# print(categories)
# print()

# # F.5 Create a dictionary mapping product name to inventory value (price * stock).
# #---------------------------------------------------------------------------------

# inventory_values = {
#     prod["name"]: prod["price"] * prod["stock"] 
#     for prod in cleaned_list
# }

# print("\n   --- Dictionary of inventory values per product:   ---\n")

# for name, value in inventory_values.items():
#     print(f"{name:20s}: {value:8.2f} kr")
# print()



# # F.6 Sort procucts by inventory value from highest to lowest.
# #-------------------------------------------------------------

# sorted_inventory = dict(
#     sorted(inventory_values.items(), key=lambda item: item[1], reverse=True)
# )

# print("\n   --- Products Sorted by Inventory Value (Highest to Lowest):   ---\n")

# for name, value in sorted_inventory.items():
#     print(f"{name:20s}: {value:8.2f} kr")



# # F.7 Use enumerate to print a ranked report.
# #--------------------------------------------

# print("\n" + "=" * 45)
# print("          RANKED REPORT       ")
# print("=" * 45)

# for rank, (name, value) in enumerate(sorted_inventory.items(), start=1):
#     print(f"{rank:2d}. | {name:20s} | {value:8.1f} kr")

# print("=" * 45)

# F.8 Use zip to combine at least one pair of separate derived lists in a meaningful way.
#----------------------------------------------------------------------------------------


# F.9 Write both a deliberately over-complicated comprehension and a clearer alternative.
#     Explain why the clearer version wins. 
#----------------------------------------------------------------------------------------




#*******************************************************************************************************
#  LAB 6                         Part G - Stretch challenges                                           *
#*******************************************************************************************************

# G.1 Flatten a simple list of lists using a comprehension.
#----------------------------------------------------------


# G.2 Create a multiplication table structure using a nested comprehension, then decide 
#     whether the result is readable enlugh.
#----------------------------------------------------------------------------------------


# G.3 Given names and scores, create only passing student dictionaries in one readable comprehension.
#----------------------------------------------------------------------------------------------------


# G.4 Use any() and all() to answer useful questions about a score list, after first solving them with loops.
#------------------------------------------------------------------------------------------------------------


# G.5 Create five examples where Pythonic syntax reduces boilerplate without reducing clarity.
#---------------------------------------------------------------------------------------------


# **********************************  END of LAB 6  ********************************************************