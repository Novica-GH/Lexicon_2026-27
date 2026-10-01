
#******************************************************************************************
# Novica Ivkovic
# Cours: System Developer Python and AI
# September 16 2026 - Today's study goal is: Repetition and - Comprehension list/ ...
#                   - Tomorow TEST
#                   - On Friday cach up day - to complete all previous tasks.
#*******************************************************************************************

# Just remember.
#
# [....] -> list comprehension
# {key:value ...} -> dictionary comprehension
# { ... } -> set comprehension
# ( ... ) -> generator expression, not tuple comprehension


# Here you have today’s lab! 🙂
 
# A little update on the plan for the rest of the week:
# Tomorrow: Normal lesson as usual + lab.
# Thursday: We’ll have a small test covering everything we’ve gone through so far. The test will not be graded. Instead, it’s a way for you to see how you’re doing and make sure you’re keeping up with what we’ve covered so far. You’ll also have time to catch up on any labs from this week that you haven’t finished yet.
# Friday: We’ll have a catch-up day. This will also be the deadline for all labs from this part of the course. By the end of the day, we expect your GitHub to be updated with your solutions to all the labs we’ve completed so far.
# Deadline: Friday, September 18, 2026.

# Repetition:
#   "_" - donja crta se standardno uzima za zamenu za clana liste


###########################################
# Part 1 - Repetition - List of numbers
#*********************************************

#  "_" - donja crta se standardno uzima za zamenu za clana liste

# numbers = [1, 2, 3, 4, 5]

# doubled_numbers = []

# for number in numbers:
#     doubled_numbers.append(number * 2)

# print(doubled_numbers)
#------------------------------------------------

# List comprehension
#---------------------------------

# numbers = [1, 2, 3, 4, 5]

# # doubled_numbers = [for number in numbers]  # Some people like this way, but it doesn't work.

# doubled_numbers = [number * 2 for number in numbers] # this works - 

# print(doubled_numbers)
#------------------------------------------------------------------

# numbers = [1, 2, 3, 4, 5]

# squares = [number **2 for number in numbers]

# print(squares)
#--------------------------

# names = ["ada", "grace", "guido"]      

# #upper_names = [for name in names] # nepotpuno, fali name pre for

# upper_names = [name.title() for name in names]

# print(upper_names)

#-------------------------------------

# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]   # OBS
 
# even_numbers = []

# for number in numbers:
#     if number % 2 == 0:
#         even_numbers.append(number)

# print(even_numbers)

# even_numbers = [number for number in numbers if (number % 2 == 0)]

# print(even_numbers)

#----------------------------------------------------------------

# numbers = [1, 2, 3, 4, 5, 6]

# result = [number **2 for number in numbers if number % 2 == 0]

# print(result)
#-------------------------------------

# names = ["Ada", "Bob", "Alexander", "Grace", "Li"]

# x = [name for name in names if len(name >= 5)]

# print(x)

# long_names = [name for name in names if (len(name) >= 5)]

# print(long_names)
#----------------------------------



#******************************************************************************************
# Part 2 - Dictionary comprehension
#
#   {} - creates a dictionary
#
#  .items() - for key values
#*************************************************




# numbers = [1, 2, 3, 4, 5]  # I want to this nubers are my key

# squares = {}

# for number in numbers:
#     squares[number] = number ** 2

# print(squares)
#------------------

# squares = {number: number ** 2 for number in numbers} #   {} - creates dictionary

# print(squares)
#+++++++++++++++++++++++++++++++++++++++++++++++

# prices = {
#     "apple" : 10,
#     "banana" : 5,
#     "orange" : 8
# }

# double_prices = {product: price * 2 for product, price in prices.items()}

# print(double_prices)
#---------------------------------------------

# scores = {
#     "Anna": 85,
#     "Bob" : 62,
#     "Charlie" : 91,
#     "Diana": 70
# }

# passed = {
#     name: score
#     for name, score in scores.items()
#     if score >= 70
# }

# # #  OR:  passed = { name: score for name, score in scores.items() if score >= 70}

# print(passed)
#-------------------



#*************************************************************************************************
# PART 3 - SETS - Set comprehension - allso support ??? 
#
# Sets - Unique value counts
#************************************************************


# words = ["python", "java", "python", "csharp", "java"]

# lengths = {len(word) for word in words}

# print(lengths)





#************************************************************************************************
# PART 4 - Tuple - comprehension
#**********************************************************************************

# numbers = (number * 2 for number in range(5))  # <generator object <genexpr> at 0x000001DB4FD6C520>
# print(numbers)  

# Just remember.
#
# [....] -> list comprehension
# {key:value ...} -> dictionary comprehension
# { ... } -> set comprehension
# ( ... ) -> generator expression, not tuple comprehension






#******************************************************************************************************
# Part 5 - Enumerate
#******************************************************************************************************


# languages = ["Python", "Java", "C#"]

# for index in range(len(languages)):  # This is possible, byt Python givs something bettre
#     print(index, languages[index])

# OR:
# for index, languages in enumerate(languages):
#     print(index, language)
#------------------------------------

# for position language in enumerat (languages, start=1):
#     print(position, language)

# # OR:
# for language in languages:
#     print(language)

# for index, languages in enumerate(languages):
# #     print(index, language)






#*******************************************************************************************************
# Part 6 - ZIP
#*******************************************************************************************************

# names = ["Ada", "Bob", "Alexander", "Grace", "Li"]
# scores = [85, 62, 91, 84]

# for index in range(len(names)):
#     print(names[index], scores[index])
# print()

# for name, score in zip(names, scores):  # print wery elegant
#     print(name, score)
# print()

# pairs = list(zip(names, scores))   # list of tupples
# print(pairs)
#-----------------------------------------------
# 3 liste

# names = ["Ada", "Bob", "Alexander", "Grace", "Li"]
# scores = [85, 62, 91, 84, 55]
# cities = ["Stockholm", "London", "Berlin", "Bern", "Paris"]

# for name, score, city in zip(names, scores, cities):
#     print(name, score, city)

#--------------------------------------------------10:26

# names = ["Ada", "Bob", "Alexander", "Grace", "Li"]  # 5 names
# scores = [85, 62, 91, 84]                           # 4 scores                       

# for name, score in zip(names, scores):
#     print(name, score)                              # print just 2 tuples
#---------------------------------------------

# names = ["Ada", "Bob", "Alexander"] 
# scores = [85, 62, 55]  

# student_scores = dict(zip(names, scores))

# print(student_scores)

#----------------------------------------10:29



#*******************************************************************************************************
# Part 7 - UNPACKING
#*******************************************************************************************************

#   "_" - donja crta se standardno uzima za zamenu za clana liste


# coordinates = (10, 20)
# #  print(coordinates) # test
# #  print(type(coordinates)) # test
# x, y = coordinates

# print(x)
# print(y)
# print(type(coordinates))

# # /// Result ///:
# # 10
# # 20
# # <class 'tuple'>

#----------------------10:33

# names = ["Ada", "Grace", "Guido"]
# print(type(names))

# first, second, third = names

# print(first)
# print(second)
# print(third)
# print(type(names))

# # # /// Result ///:
# Ada
# Grace
# Guido
# <class 'list'>

#++++++++++++++++++++++++++++++++++++++++++++

# numbers = [10, 20, 30, 40, 50]

# first, *rest = numbers

# print(first)
# print(type(first))
# print(rest)
# print(type(rest))

# /// Result ///:
# 10
# <class 'int'>
# [20, 30, 40, 50]
# <class 'list'>
#--------------------------

# numbers = [10, 20, 30, 40, 50]
# first, *middle, last = numbers

# print(first)
# print(middle)
# print(last)

# print("First:", first)
# print("Middle:", middle)
# print("Last: ", last)
# print(type(numbers))

# /// Result ///:
# 10
# [20, 30, 40]
# 50
# First: 10
# Middle: [20, 30, 40]
# Last:  50
# <class 'list'>
#++++++++++++++++++++++++++++++-10:39

# person = ("Ada", 36, "London")

# name, _, city = person    #   "_" - donja crta se standardno uzima za zamenu za clana liste

# print(name)
# print(_)
# print(city)

# print(person)
# print(type(person))

# /// Result ///:
# Ada
# 36
# London
# ('Ada', 36, 'London')
# <class 'tuple'>
#+++++++++++++++++++++++++++++++ 10:43

#*******************************************************************************************************
# Part 8 - Combine lists/dictionaries/
#*****************************************************************************************************

# first = [1, 2, 3]
# second = [4, 5, 6]

# combined = [*first, *second]

# print(combined) # OK combined: list + list = 1 list (concatenation)
# print(type(combined))
# x = print(first, second) # print two separat lists
# print(x)
# print(type(x))



# /// Result ///:
# [1, 2, 3, 4, 5, 6]  - Concatenation two lists in one list
# <class 'list'>
# [1, 2, 3] [4, 5, 6]  - Print two lists separately!
# <class 'NoneType'>   - OBS! None (special) Type! 

#-------------------------10:46

# defaults = {
#     "theme": "light",
#     "language": "English"
# }

# user_settings = {
#     "language" : "Swedish",   # Swedish is going to be print, because it is last defined/specified
#     "notifications": True
# }

# settings = {               # Settings je zapravo unija prethodna 2 recnika, gde se uzima
#     **defaults,            # poslednja vrednost nekog ponovljenog(zajednickog) clana (prva kolona)
#     **user_settings
# }

# print(settings)

# /// Result ///: 
# {'theme': 'light', 'language': 'Swedish', 'notifications': True}

#--------------------------------------10:50




#*******************************************************************************************************
# Part 9 - Lambda function - (litle anonym function)
#  
#*******************************************************************************************************

# def double(number):
#     return number *2

# print(double(5))
#------------------------10:53

# double = lambda number : number * 2

# # lambda
# # parameters
# # colon
# # expression

# print(double(5))
#--------------------------------------10:56


#*******************************************************************************************************
# Part 10 - Extra exempel - 10:58
#*******************************************************************************************************

# names = ["Ada", "Bob", "Alexander", "Grace", "Li"] 

# print(sorted(names)) - # sorting by ABCD...

# def get_length(name):
#     return len(name)

# sorted_names = sorted(names, key=get_length)

# print(sorted_names)
#-----------------------------11:00
# names = ["Ada", "Bob", "Alexander", "Grace", "Li"] 

# sorted_names = sorted(names, key=lambda name: len(name))

# print(sorted_names)
#---------------------------- 11:02

#Paus 11:02-11:10

#*******************************************************************************************************
# Part 11 - Sort Dictionaries
#*******************************************************************************************************

# students = [
#     {"name": "Anna", "score" : 85},
#     {"name": "Bob", "score" : 62},
#     {"name": "Charlie", "score" : 91}
# ]

# sorted_students = sorted(
#     students,
#     key=lambda student:student["score"],
#     reverse=True
# )

# print(sorted_students)

#"--------------------------------------- 11:15

# numbers =[1, 2, 3, 4, 5]

# doubled = map(lambda number: number *2, numbers)

# print(doubled)  # <map object at 0x0000026B63045A80>

# doubled = list(map(lambda number: number *2, numbers))

# print(doubled)  # it works now

# doubled = [number * 2 for number in numbers]

# print(doubled)

#-----------------------------11:18



#*******************************************************************************************************
# Part 12 - FILTER
#*******************************************************************************************************
#Repetition lambda  - Part 9
# def double(number):
#     return number *2

# print(double(5))
#------------------------10:53

# double = lambda number : number * 2

# # lambda
# # parameters
# # colon
# # expression
#**************End of Repetition************************

# numbers =[1, 2, 3, 4, 5]

# even_numbers = list(
#     filter(lambda number: number % 2 == 0, numbers)
# )

# print(even_numbers)

# na klasican nacin bez lambde: 
# even_numbers = [number for number in numbers if number % 2 == 0]



# even_numbers = [
#     number
#     for number in numbers
#     if number % 2 == 0   
# ]

# print(even_numbers)



#*******************************************************************************************************
# End in 11:27
# *******************************************************************************************************