#******************************************************************************************
# Novica Ivkovic
# Cours: System Developer Python and AI
# September 10 2026 - Today's study goal is: Conditions and Loops
#
#*******************************************************************************************
# Part A - Conditions
#*********************************************
#
# Part A.1. Write a program that classifies a number as positive, negative or zero.

# print("Input one number: ")
# n = int(input())
# if n<0:
#     print("Your number is negative.")
# elif n == 0:
#     print("You have entered a zero.")
# elif n==5:
#     print("You have entered number 5.") # In case that we want to extract number 5, beside 0.
# elif n==10:
#     print("You have entered number 10.")  #In case that we want to extract number 10 beside 0 and 5
# else:
#     print("Your number is a positive number.")
#-----------------------------------------------

# Part A.2. Ask for an age and classify it into at least four age groups using if/elif/else.
#     
# print("How old are you : ")
# n = int(input())
# if 1 <= n < 6:
#     print("You are in kindergarden.")
# elif n<=0:
#     print("You have entered a negativ number or zero!")
# elif 6 <= n < 13:
#     print("You are in the Primary school.")
# elif 13 <= n < 20:
#     print("You are a teenager.")
# elif 20 <= n < 30:
#     print("You are a young adult.")
# else:
#     print("Your are an adult person.")
#-----------------------------------------------

# Part A.3 Creata a login check using a stored username and password. Both must match.
#
# username = "User_name"
# password = "Password"

# input_username = input("Input your username: " ).strip()
# input_passwort = input("Input your password: ").strip()

# if input_username.lower() == username.lower() and input_password == password:
#     print("Wellcome! Wath would you like to do today?") #...
# else:
#     print("Error! Your username or password are inte correck. Please, try again.") #...


#
# Part A.4 Given score from 0-100, print a grade using at least five ranges. Think carefully about condition order.
# 
# print("Input one whole number beetwen 0 and 100")
# score = int(input())
# if 0<= score < 50:
#     print("You have got F.")
# elif 50<= score < 65:
#     print("You have got E.")
# elif 65<= score < 70:
#     print("You have got D.")
# elif 70<= score < 80:
#     print("You have got C.")
# elif 80<= score < 90:
#     print("You have got B.")
# elif 90<= score <= 100:
#     print("Excellent! You have got A.")



#
# Part A.5 Create a shipping rule based on order total and whether the customer is a member.
#          Use and/or.
#
# Part A.6. Write five expressions using, ==, !=, >, <,>= and <= and predict each boolean result before running.



#******************************************************************************************
# Part B - Truthy, falsy and membership
#*************************************************
#
# Part B.1 Create examples with empty string, non-empty string, zero, non-zero integer, empty list and non-empty list. 
#         Test each directly in an if statement.

# empty_stringic =""   # here can we change "" to something ie. "non_empty string"
# print(len(empty_stringic))  
# print(bool(empty_stringic))
# if empty_stringic:
#     print("Empty is no longer empty!")
# else:
#     print("Empty is realy empty!")
#----------------------------------

# zero_OK = -42  # Here can we change 0 to some another number (non-zero integer)
# print(len(zero_OK))  # OBS!!! TypeError: object of type 'int' has no len()
# print(bool(zero_OK))

# if zero_OK:
#     print("Zero is no longer zero!")
# else:
#     print("Zero is realy 0!")
#--------------------------------------

# empty_list =["","hhhhhhhhhh"]   # Here can we change [] to some another non-empty list, for exempel [5] or ["Djoka"]
# print(empty_list)
# print(len(empty_list))
# if empty_list:
#     print("The list is non longer empty!")
# else:
#     print("The list is empty!")
#---------------------------------------------
#
#
# Part B.2 Ask for a langyage and check whether it exists in a predefined list of supported languages.

# languages = ["English", "French", "Italian", "5",'ABC', "I'm not ", "Java"] # A litle bit experiment...
# print(languages)
# print("Python" in languages)
# print("Italian" in languages)
# print("Java" not in languages)
# print("C" not in languages)
#--------------------------------
#
# Part B.3 Create a list of blocked usernames and reject a supplied username if it appears in the list.
#

# blocked_usernames = ["admin", "administrator", "owner", "superuser", "root", "mile_007"]

# input_username = input("What is your user name: ")

# if input_username in blocked_usernames:
#     print(f"Error: The specified user name '{input_username}' is not allowed to use. Please, choose another username.")
#     input_username = input("Chose another user name: ")
#     if input_username in blocked_usernames:
#         print(f"Error: The specified user name'{input_username}' is not allowed to use. Please, wait 10 minutes and try again.")

# else:
#     print(f"Your user name '{input_username}'is accepted.")    
#--------------------------------------------------------------------
#
# Part B.4 Use not to express at least two conditions in a readable way.
# 
# blocked_usernames = ["admin", "administrator", "owner", "superuser", "root", "mile_007"]
# length = 8 

# input_username = input("What is your user name: ")
# user_length = len(input_username)

# if not input_username in blocked_usernames and not user_length < length:
#     print(f"Your user name '{input_username}'is accepted.")
# else:
#     if input_username in blocked_usernames:
#         print(f"Error: The specified user name '{input_username}' is not allowed to use. Please, choose another username.")
#     else:
#         print(f"Error: The specified user name '{input_username}' need to have at least 8 characters. Please, choose another username.")

#---------------------------------------------

#    
#*************************************************************************************************
# PART C - For loops
#************************************************************
#
# C.1. Loop overa list of names and print a numbered greeting for each.

# names = ["Ada", "Anna", "Tom", "Yerry", "Luisa", "Silvia", "Peter"]

# for number, name in enumerate(names, start=1):
#     print(f"{number}. Hej {name}, you are our lucky candidate.")

# C.2 Loop over numbers 1-50 and print only even numbers.

# i=1
# for i in range(1,51):
#     if i%2 ==0:
#         print(i)
#     i+=i


# C.3 Calculate a sum of a list manually using a loop rather than sum().

# numbers = (1, 2, 3, 4, 5, 6, 7)

# summa=0
# for i in numbers :
#     summa += i     
    
# print(f"Summ of all elements in list numbers is: {summa}")


# C.4 Find the largest number in a list manually without max().

# numbers = (1, 20, 3, 4, 5, 6, 7)

# maximum = 0
# for i in numbers :
#     if maximum < i:
#         maximum = i  
    
# print(f"Maximum of all elements in list numbers is: {maximum}")

# C.5 Count how many words in a list have more then five caracters.

# words = ("Anna", "Bob", "Jack", "Marry", "Tom", "Jerry", "Nick", "Christopher")

# counter = 0

# for i in words:
#     if len(i) > 5:
#         counter += 1

# print(f"Total number of words in list words that have more then 5 characters is: {counter}") 

# C.6 Given a list of scores, count passes and failures using a treshold of 70.

# scores = [75, 85, 50, 60, 35, 89, 55, 92, 70, 52, 67]

# passes = 0
# failur = 0

# for i in scores:
#     if i >= 70:
#         passes += 1
#     else:
#         failur += 1

# print(f"Pass with 70 or more points are: {passes}")
# print(f"Failur on the test: {failur}")



# C.7 Loop over a dictionary using keys, values and .items() in three separate examples.

voters = {"Ava": 55, "Adam": 33, "Tom": 19, "Elly": 27, "Klas":65}
print(voters)

# for name in voters.keys():  # This is exempel 1 with .keys()
#     print(name)

for age in voters.values():   # This is the second exempel 1 with .values()
    print(age)

# for name, age in voters.items():
#     print(f"{name} is {age} years old.")  # This is the third exempel with .items()


#************************************************************************************************
# PART D - Range, enumerate and nested loops
#**********************************************************************************
#
# D.1 Use range to print 10 down to 1.

# for i in range(10,0,-1):
#     print(i)


# D.2 Generate the multiplication table for a number supplied by the user.



# D.3 Use enumerate to print a playlist with track numbers starting at 1.

# D.4 Use mested loops to print coordinate pairs x=1..3 and y=1..4.

# D.5 Create a simple 5x5 text grid using nested loops.


#******************************************************************************************************
# Part E - While loops
#******************************************************************************************************


# E.1 Create a countdown from 10 to 0.

# E.2 Ask repeatedly for a password until the correct password is entered.

# E.3 Create a manu that repeats until the user chooses 'quit'. The menu can simply print which option was selected.

# E.4 Ask the user for numbers until they enter 0. Keep a running total.

# E.5 Create a guessing loop with a fixed secret number. Tell the user whether each guess is too high or too low.
#



#*******************************************************************************************************
# Part F - Break and continue
#*******************************************************************************************************


# F.1 Loop through numbers 1-100 and stop when you reach the first number divisible by both 7 and 9.

# F.2 Loop through a list of strings and skip empty strings using continue.

# F.3 Search a list for a target name. Print 'found' and break when it appears; otherwise
#     explain how you know it was not found.      
# 
# F.4 Process a list of numeric values where negative values should be skipped and processing stops completely
#     when the value 999 appears.    
# 
# ************************************************************************************************** 


#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
#*******************************************************************************************************
# Part G - Applied  challenge: Console study tracker
#*******************************************************************************************************
#


# G.1 Create a list of dictionaries representing at least ten study sessions with subject and minutes.

# G.2 Loop through the sessions and calculate total minutes.

# G.3 Calculate total minutes per subject using a dictionary that starts empty and is uppdated inside the loop.
# 
# G.4 Identify the longest study session without max(..., key=...).

# G.5 Print only sessions longer than 45 minutes.

# G.6 Create a repeated menu that lets a user: view all sessions, view total time, filter by subject, or quit.

# G.7 Use break/continue where they genuinely improve the flow.
# 


#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
#*******************************************************************************************************
# Part H - Stretch challenges
#*******************************************************************************************************


# H.1 Print FizzBuzz from 1 to 100: multiplies of 3 -> Fizz, 5->Buzz, ->FizzBuzz.

# H.2 Given a sentence, count vowels without using .count() repeatedly.

# H.3 Find all duplicate values in a list using loops and collections.
# 
# H.4 Build a simple text histogram: for each number in [3,5,2], print that many * characters.
# 
# *******************************************************************************************************