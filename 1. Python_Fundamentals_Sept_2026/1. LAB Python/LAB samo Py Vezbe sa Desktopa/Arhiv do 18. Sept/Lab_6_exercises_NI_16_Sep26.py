#******************************************************************************************
# Novica Ivkovic
# Cours: System Developer Python and AI
# September 16 2026 - Today's study goal is: REPETIION - COMPREHENSION
#                     
#*******************************************************************************************

#********************************************
# Part A - List comprehension
#*********************************************

# Part A.1. Create squares for numbers 1-20 using a normal loop, then a list comprehension.
#------------------------------------------------------------------------------------------

# squares_loop = []

# for number in range (1, 21):
#     squares_loop.append(number **2)

# print("We are going through normal loop:", squares_loop)

# squares_comprehension = [number **2 for number in range(1, 21)]

# print("We are going through list comprehension:", squares_comprehension)


# Part A.2. Create a list containing only even numbers from 1-100
#----------------------------------------------------------------
     

# 1st way - classic

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



# Part A.3 Convert a list of names to stripped, title-cased names.
#-----------------------------------------------------------------

# 1st way - classic by for-loop

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

# via - list comprehension

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

# Kasnije ...





#********************************************************
# Part B - Dictionary and set comprehensions
#********************************************************


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


# start_list = ["Ada", "bob", "Gvido", "Lucia", "Stefan", "Petar", "EMIL"]

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
                  

    
#*************************************************************************************************
# PART C - enumerate
#************************************************************


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
# PART D - zip and unpacking
#**********************************************************************************

# D.1 Combine separate name and score lists using zip and print each pair.
#-------------------------------------------------------------------------


# D.2 Create a dictionary using dict(zip(keys, values)).
#-------------------------------------------------------


# D.3 Combine three lists: product name, price and stock.
#--------------------------------------------------------

# D.4 Investigate what happens when zipped lists have different lengths.
#-----------------------------------------------------------------------


# D.5 Use tuple unpacking directly in a for loop over zipped data.
#-----------------------------------------------------------------


# D.6 Swap two variables without a temporary variable.
#-----------------------------------------------------



#******************************************************************************************************
# Part E - sorted and lambda
#******************************************************************************************************


# E.1 Sort a list of words by length using sorted(..., key=...)
#--------------------------------------------------------------

# E.2 Sort a list of student dictionaries by score ascending and descending.
#---------------------------------------------------------------------------


# E.3 Sort products by price using a lambda.
#-------------------------------------------


# E.4 Sort people by last name when each item is a dictionary containing first_name and last_name.
#-------------------------------------------------------------------------------------------------


# E.5 Write a normal named function for a sort key, then replace it with lambda.
#      Compare when each is clearer.
#------------------------------------------------------------------------------




#*******************************************************************************************************
# Part F - Applied challenge: Data cleanup
#*******************************************************************************************************


# F.1 Start with a list of at least twelve messy dictionaries representing product:
#     inconsistent name casing/spacing, category, price and stock.
#----------------------------------------------------------------------------------

# F.2 Create a cleanded list where names/categories are normalized. Use comprehensions where readable.
#-----------------------------------------------------------------------------------------------------


# F.3 Create a list of in-stock products.
#----------------------------------------


# F.4  Create a set of unique normalized categories.
#---------------------------------------------------


# F.5 Create a dictionary mapping product name to inventory value (price * stock).
#---------------------------------------------------------------------------------


# F.6 Sort procucts by inventory value from highest to lowest.
#-------------------------------------------------------------


# F.7 Use enumerate to print a ranked report.
#--------------------------------------------


# F.8 Use zip to combine at least one pair of separate derived lists in a meaningful way.
#----------------------------------------------------------------------------------------


# F.9 Write both a deliberately over-complicated comprehension and a clearer alternative.
#     Explain why the clearer version wins. 
#----------------------------------------------------------------------------------------




#*******************************************************************************************************
# Part G - Stretch challenges
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


#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
#*******************************************************************************************************

# names = ["Ana", "David", "Sara"]
# scores = [85, 92, 91]

# for position, (name, score) in enumerate(zip(names, scores), start=1):
#     if score>=80:
#         print(position, name)

students = [
    {"name":"Ana", "score": 85},
    {"name":"David", "score": 92},
    {"name":"Sara", "score": 78},
    {"name":"Leo", "score": 92},

]

result = sorted(students, key=lambda student: student["score"], reverse=True)

print(result[3]["name"])
