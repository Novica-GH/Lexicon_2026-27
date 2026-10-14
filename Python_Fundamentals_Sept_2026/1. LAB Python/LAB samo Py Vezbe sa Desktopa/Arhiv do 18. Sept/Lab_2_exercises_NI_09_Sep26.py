#******************************************************************************************
# Novica Ivkovic
# Cours: System Developer Python and AI
# September 9 2026 - LAB 2
#
#*******************************************************************************************
#     LAB 2 - Collections in Python
#*********************************************
#
# Part A - Lists
#*******************************************************************************************
#
# A.1. Create a list of at least eight programming languages. Acces the first, last, third and secont-to-last values.

# prog_languages = [ "Ada", "Basic", "C", "C++", "C#", "Cobol", "Fortran", "Pascal"]
# print(prog_languages)
# print(prog_languages[0])
# print(prog_languages[-1])
# print(prog_languages[2])
# print(prog_languages[-3])
#-------------------------------
           

# A.2. Print three defferent slices of the list, then print the list in reverse order using slicing.

prog_languages = [ "Ada", "Basic", "C", "C++", "C#", "Cobol", "Fortran", "Pascal"]

print(prog_languages[:5])
print(prog_languages[1:4])
print(prog_languages[6:])
print(prog_languages[::-1])
#--------------------------------


# A.3. Use append, insert, remove and pop. After each operation, print the list so the change is visible.

# prog_languages = [ "Ada", "Basic", "C", "C++", "C#", "Cobol", "Fortran", "Pascal"]

# prog_languages.append("PL/1")
# print(prog_languages)

# prog_languages.insert(1,"Visual Basic")
# print(prog_languages)

# prog_languages.remove("Basic")
# print(prog_languages)

# prog_languages.pop()
# print(prog_languages)
#---------------------------


# A.4. Create a numerical list. Calculate its length, minimum, maximum and sum using built-in functions.

# numbers = [1, 3, 5, 7, 9, 11]
# print(numbers)
# length = len(numbers)
# minimum = min(numbers)
# maximum = max(numbers)
# summa = sum(numbers)
# print(length, minimum, maximum, summa)
#-------------------------------------------

# A.5. Sort one list ascending and another descending. Explain in a comment the difference between chnanging a list with. sort()
#       and creating a sorted result with sorted().

# list_1 = [1, 4, 2, 7, 9, 5]
# list_1.sort()
# print (f"Ascending (list_1): {list_1}")

# list_2 = [11,33,52,95,14,8,65]
# desc_list_2 = sorted(list_2, reverse=True)
# print(f"Descending (list_2): {desc_list_2}")
# print(f"Original list_2 remain unchanged: {list_2}")

# Explanation of the difference between .sort() and sorted():
# .sort() method modifies the original list, while sorted() leaves the origina list completely unchanged.
#-----------------------------------------------------------

# A.6. Demonstrate the reference/copy issue using list_b = list_a. Then fix it with .copy().

#Reference
# list_a = [1, 4, 2, 7, 9, 5]
# print("Reference method:")
# print(f"Original list_a: {list_a}")
# list_b = list_a  # in this moment both lists points to the same list in memory

# list_b.append(10)
# print (f"list_a after append in reference version: {list_a}")
# print(f"list_b after append in reference version: {list_b}")
# print()

# #Copy
# list_a = [1, 2, 6, 3, 5]
# print("Copy method:")
# print(f"Original list_a: {list_a}")
# list_b = list_a.copy()  # in this moment list_b take a new place in memory

# list_b.append(20)
# print (f"list_a after append in copy version: {list_a}")
# print(f"list_b after append in copy version: {list_b}")
#----------------------------------------------------------

#
#*************************************************************************************************
# Part B - Tuples and unpacking
#************************************************
#
# B.1 Create a tuple representing RGB values. Unpack it into three variables and print them.

# rgb = ("red", "green", "blue")

# r, g, b = rgb

# print(r)
# print(g)
# print(b)
#-----------------------------------------------------------

# B.2 Create a tuple containting a person's name, age and city. Unpack and use the values in a formatted sentence.

# person = ("Adam", 33, "Stockholm")

# name, age, city = person

# print(f"Citizen {name} {age} years old, lives in {city}.")
#-----------------------------------------------------------

# B.3 Attempt to reason about changing one tuple element. Explain in a commnt why tuples are useful when values should not be changed.

# person = ("Adam", 33, "Stockholm")
# person[0] = "Tom"  # => TypeError: 'tuple' object does not support item assignment

# Why tuples are useful when values should not be changed?

# 1. Data protection - Immutability helps with data integrity.
# 2. System performance - Because we alreadu know that tuples are immutable, that means that Python
#                         is going to allocate a fixed memory size for them(tuples)
# 3. Wery clear code - Like Alladin said - tuples are very Pythonic - I translate this like user friendly.
#----------------------------------------------------------------------

# B.4 Create a list containing at least four coordinate tuples such as (10, 20). Access iondividual x and y values.

# list_of_pairs = [(10, 20), (30, 40), (50, 60), (70, 80)]

# first_pair = list_of_pairs[0]  # This is first tuple in the list
# print(f"This is the first pair in the list: {first_pair}")
# print()

# x1 = list_of_pairs[0][0]       # This is the first coordinate from the first tuple in the list.
# y1 = list_of_pairs[0][1]       # This is the second coordinate from the first tuple in the list.

# print(f"The first point in the list has coordinates: x = {x1} and y = {y1}.")
 
# x2, y2 = list_of_pairs[1]  # This is the other way how we can reach the individual x and y values.

# print(f"The second point in the list has coordinates: x = {x2} and y = {y2}.") 

# print(f"\n--- All coordinates in the list ---")
# for index, (x,y) in enumerate(list_of_pairs, start=1):
#     print(f"The point {index}: x-axis = {x}, y-axis ={y}")
#------------------------------------------------------------------------------------
#
#
#
#********************************************************************************************
# Part C - Sets
#*******************************************************************
#
# C.1 Create a list containing duplicate course names. Convertit to a set and compare the lengths before and after.



# C.2 Create two sets representing skills of two developers. Find skills they share, skills only the first has, 
#     and all skills represented by either person.

# C.3. Create a set and practide add, remove/discard and membership testing.

# C.4 Explain in comments why a set is a better shoice than a list for one real-world uniqueness problem.

#
#**************************************************************************************
#  Part D - Dictionaries
#***************************************************************************************
#
# D.1 Create a dictionary for a laptop with brand, RAM, storage and price. Read every value by key.

# D.2 Uppdate the price , add an operating_system key and remove one key.

# D.3 Use .get() for both en existing and a missing key. Compare it conecepyually with direct indexing.

# D.4  Print keys, values and itemso separately.

# D.5. Create a dictionary mappint five course names to number of study hours. 
#      Calculate the total hours using the dictionaty values.

#
#*******************************************************************************
# Part E - Nested collections
#********************************************************************************