#******************************************************************************************
# Novica Ivkovic
# Cours: System Developer Python and AI
# September 14 2026 - Today's study goal is: Functions  (with Aladdin)
#                    
#*******************************************************************************************
# Part A - FUNCTIONS - REUSABLE COD
#*********************************************
#
# 
# print("Hello")
# len("Python")
# type(10)

# def greet(): 
#     print("Hello!") #identation here is to mark the block

# greet()
# greet()
# greet()
#------------------------

# def say_good_morning(): # Use the truth name to describe what function does.
#     print("Good morning!")

# say_good_morning()
#---------------------------------

# def greet(name): # Exempel function with input argument (name) - ie. #parameter - when we define funciton
#      print("Hello!", name) #identation here is to mark the block

# greet("Ada") # Here is Ada - argument
# greet("Guido")
#-------------------------------------------------

# def introduce(name, age):   # Order matters!
#      print(name, "is", age, "years old.")

# introduce("Biljana")  # Problem! This function has 2 parameters, and we call it without them.

# def introduce(name, age):
#      print("Name: ", name)
#      print("Age:", age)

# #introduce(36, "Ada") # This is wrong because name goes first
# introduce(age=36, name="Ada")   #Keyword arguments - Allow reverse order, but we need to know keyword arguments.
#------------------------------------------------------------

# def calculate_tax(income, tax_rate):  # This function doesn't have return value
#     tax = income * tax_rate
#     print(tax)

# calculate_tax(50000, 0.3)
#------------------------------

# def calculate_tax(income, tax_rate): # This function has return
#     tax = income * tax_rate
#     #print(tax)
#     return tax

# result = calculate_tax(5000,0.3)
# print(result)
#------------------------------------------------------

# def add_with_print(a, b):   
#     print(a+b)                 # Function write 8, byt it doesn't return 8 (value of function)

# result = add_with_print(5,3)
# print("Result: ", result)
#-------------------------------------

# def add_with_print(a, b):   
#      return a + b                 # Function write returns value here

# result = add_with_print(5,3)
# print("Result: ", result)
#--------------------------------


# def calculate_tax(income, tax_rate):
#     return income * tax_rate
# tax = calculate_tax(50000, 0.3)

# income_after_tax = 50000- tax

# print("Tax:", tax)
# print("Income after tax:", income_after_tax)
#-----------------------------------------------------

# def calculate_tax(income, tax_rate):
#     return income * tax_rate

# print(calculate_tax(500000, 0.3))
# #----------------------------------------

# def example():
#     print("Before return")
#     return 10
#     print("After return")  # This part of code is not a part of a function example - it comes efter return...

# result = example()
# print(result)
#-----------------------------------

# def check_grade(score):
#     if score >= 70:
#         return "PASS"
#     else:
#         return "FAIL"

# print(check_grade(87))
# print(check_grade(65))
#------------------------- OR

# def check_grade(score):     "  SCORE - PASS - FAIL"
#     if score >= 70:
#         return "PASS"  # Here we don't have else part...
    
#     return "FAIL"

# print(check_grade(65))
# print(check_grade(89))
#-------------------------------------------

# def get_first_item(items):    # OBS!!!!!
#     return item(0) 

# language = ["Python", "Java", "C#"]

# print(get_firtst_item(language))
# #----------------------------------------------


# def print_languages(languages):
#     for language in languages:
#         print(language)

# my_languages = ["Python", "Java", "C#"]

# print_language  # Opet fali
#-------------------------------------------

# def count_passing_scores(scores):
#     passed = 0

#     for score in scores: 
#         if score >= 70:
#             passed += 1
#     return passed
# scores = [85, 62, 91, 72, 47]

# result = count_passing_scores(scores)

# print("Passed", result)



#-------------------------------------
#Dictionary exampel  -  PASS - FAIL
#+++++++++++++++++++++++++++++++++++++++++++
# def get_student_status(student):
#     if student["score"] >= 70: 
#         return "PASS"

#     return "FAIL"
# #print(type("FAIL"))  # My extra check (not by Aladdin)

# student = {
#     "name": "Ada",
#     "score": 95
# }
# print(type(student["name"]))  # My extra check (not by Aladdin)
# print(type(student["score"]))  # My extra check (not by Aladdin)

# status = get_student_status(student)

# print(student["name"],status)
#----------------------------------------

#+++++++++++++++++++++++++++++++++++++++++++++++++++
# Primer sa listama
#+++++++++++++++++++++++++++++++++++++++++++++++++++

# students = [                           # This is a list of dictionary - elements are a row in dictionary
#     {"name": "Anna", "score": 85},      # This is a first elemen of list (student[0]), but here [{'name': 'Anna', 'score': 85}]
#     {"name": "Ava", "score": 55},       # This is a second elemen of list (student[1]) -||-  -||-  -||-
#     {"name": "Mike", "score": 75},      # This is a third elemen of list (student[2])  -||-  -||-
#     {"name": "Luckas", "score": 95},    # This is a fourth elemen of list (student[3]) -||- -||-
# ]


# def get_student_status(student):    # This  function returns students status by score (PASS/FAIS)
#     if student["score"] >= 70:      # Here we compare score condition.
#         return "PASS"
#     return "FAIL"

# i=0
# for student in students:                   # Here we go through the for-loop from list element 0-3
#     status = get_student_status(student)    # 1st step: function(0), ie. from {"name": "Anna", "score": 85} -> 85
#     print(i, student["name"], status)          # Here we print just name from previous list-element            -> Anna 
#     i +=1
    #----------------------------------------------------------






#***************************************
#  10:15 - SEcond part
# *******************************************************
# ++++++++++++++++++++++++++++++++++++++++++++++

# def greet(name, greeting="Hello"):
#     print(greeting, name)

# greet("Ada")  # Hello Ada
# greet("Ada","Good morning")  # Good morning Ada
#-------------------------------------------------

#++++++++++++++++++++++++++++++++++++
# Exempel - Do not this!
#def greet(greeting = "Hello", name):   # OBS This is not good - we need parameter first!!!!
#    print(greeting, name)              # OBS Undefineded parameter comes firs!
#-----------------------------------------------



# def create_user(name, role="student", active=True):
#     print("Name:", name)
#     print("Role:", role)
#     print("Active: ", active )

# create_user("Ada")
#create_user("Ada, role="teacher")
#create_user("Ada", active=False)
#---------------------------------------------------------



# def min_and_max(numbers):
#     return min(numbers), max(numbers)

# #result = min_and_max([4,8,1,12,3])
# smallest, largest = min_and_max([4,8,1,12,3])

# # print(result)
# # print(type(result))
                
# print("Smallest:", smallest)
# print("Largest:", largest)
#-------------------------------------------


# Exempel 2 functions - combination  # Funkcija poziva drugu funkciju

# def calculate_tax(income, tax_rate):                   # Problem here is that we define tax in the second function
#     return income * tax_rate

# def calculate_income_after_tax(income, tax_rate):
#     tax = calculate_tax(income, tax_rate)
#     return income - tax

# result = calculate_income_after_tax(50000, 0.3)

# print(result)
#---------------------------------------------------------



#*****************************************************************
#  VERY IMPORTANT TERMS:    
#"+++++++++++++++++++++++++++++++++++++++++++++++"

# numbers = [5, 2, 6, 1]

# print(len(numbers))   # Built - in - function len

# numbers.sort()          #  Method belonging to the list object -> sort je metod
# print(numbers)          #  To jest, ugradjena funkcijak koju pozivamo sa tacka-nesto je metoda

# def get_first_items(items):     # Function   -- while (items)- is parameter of function
#     return items[]

# print(get_first_items(numbers))

# OBS it is commin Hypens!!!

#**************************************************************



# def add(a: int, b: int) -> int:
#     return a + b

# #print(add(5,7))

# print(add("Hello", "World")) # This is going to get concatenation -> HellWorld

#-------------------------------

#***********************************************************
# docstrings - Describes what functions exctualy does.

# def calculate_area(width, height):
#     """Return the area of a rectangle.
#     ********************************************************
#     -----------------------------------------------------
#     +++++++++++++++++++++++++++++++++++++++++++++++++++++++++"""
#     return width * height

# #print(calculate_area(5,3))
# print(calculate_area.__doc__)
#----------------------------------------------------

# def greet():
#     print("Hello",name, age)

# greet("Ada")


#Think about: orders, ...



#########################################  END OF TODAYS LECTION  ##############




