#****************************************************************************************
#  Novica Ivkovic                                                                       *   
#  Cours: System Developer Python and AI                                                *
#  September 10 2026 - LAB 3                                                            *
#        Today's study goal is: Conditions and Loops                                    *
#****************************************************************************************


#****************************************************************************************
#    LAB 3                    Part A - Conditions                                       *
#****************************************************************************************

# Part A.1. Write a program that classifies a number as positive, negative or zero.
#----------------------------------------------------------------------------------

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



# Part A.2. Ask for an age and classify it into at least four age groups using if/elif/else.
#-------------------------------------------------------------------------------------------

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



# Part A.3 Creata a login check using a stored username and password. Both must match.
#-------------------------------------------------------------------------------------

# username = "User_name"
# password = "Password"

# input_username = input("Input your username: " ).strip()
# input_passwort = input("Input your password: ").strip()

# if input_username.lower() == username.lower() and input_password == password:
#     print("Wellcome! Wath would you like to do today?") #...
# else:
#     print("Error! Your username or password are inte correck. Please, try again.") #...



# Part A.4 Given score from 0-100, print a grade using at least five ranges. 
#          Think carefully about condition order.
#---------------------------------------------------------------------------
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



# Part A.5 Create a shipping rule based on order total and whether 
#          the customer is a member. Use and/or.
#-----------------------------------------------------------------

# order_total = 127
# is_member = False

# # if is_member or order_total > 200:
# #     shipping_cost = 0
# # elif not is_member and order_total >= 200:
# #     shipping_cost = 50
# # else:
# #     shipping_cost = 100

# # print(f"Order Total: {order_total}")
# # print(f"Is Member: {is_member}")
# # print(f"Shipping Cost: {shipping_cost}")


# # Part A.6. Write five expressions using, ==, !=, >, <,>= and <= 
#             and predict each boolean result before running.
# #----------------------------------------------------------------

# # 1. (==)
# expr1 = (5 * 2) == 10
# # Prediction: True (10 is equal 10)

# # 2. (!=) and (>)
# expr2 = (15 != 15) or (20 > 10)
# # Prediction: True (First part is False, but another is True, based on that 'or' gives True)

# # 3. (<)
# expr3 = len("Python") < 4
# # Prediction: False (Length of word "Python" is 6, and 6 is not less then 4)

# # 4. (>=)
# expr4 = 100 >= 100
# # Prediction: True (100 is equal 100)

# # 5. (<=)
# expr5 = (3 + 5) <= 7
# # Prediction: False (8 is not less then 7)


# # Testing results:
# print("Expr 1 (==):", expr1)  # Expected: True
# print("Expr 2 (!=, >):", expr2)  # Expected: True
# print("Expr 3 (<):", expr3)  # Expected: False
# print("Expr 4 (>=):", expr4)  # Expected: True
# print("Expr 5 (<=):", expr5)  # Expected: False



#***************************************************************************************
#     LAB 3           Part B - Truthy, falsy and membership                            *
#***************************************************************************************

# Part B.1 Create examples with empty string, non-empty string, zero, non-zero integer,
#          empty list and non-empty list. Test each directly in an if statement.
#---------------------------------------------------------------------------------------

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

# empty_list =["","hhhhh"]   # Here can we change [] to some another non-empty list, for exempel [5] or ["Djoka"]
# print(empty_list)
# print(len(empty_list))
# if empty_list:
#     print("The list is non longer empty!")
# else:
#     print("The list is empty!")



# Part B.2 Ask for a langyage and check whether it exists in a predefined list of supported languages.
#-----------------------------------------------------------------------------------------------------

# languages = ["English", "French", "Italian", "5",'ABC', "I'm not ", "Java"] # A litle bit experiment...
# print(languages)
# print("Python" in languages)
# print("Italian" in languages)
# print("Java" not in languages)
# print("C" not in languages)



# Part B.3 Create a list of blocked usernames and reject a supplied username if it appears in the list.
#------------------------------------------------------------------------------------------------------

# blocked_usernames = ["admin", "administrator", "owner", "superuser", "root", "mile_007"]

# input_username = input("What is your user name: ")

# if input_username in blocked_usernames:
#     print(f"Error: The specified user name '{input_username}' is not allowed to use. Please, choose another username.")
#     input_username = input("Chose another user name: ")
#     if input_username in blocked_usernames:
#         print(f"Error: The specified user name'{input_username}' is not allowed to use. Please, wait 10 minutes and try again.")

# else:
#     print(f"Your user name '{input_username}'is accepted.")    



# Part B.4 Use not to express at least two conditions in a readable way.
#-----------------------------------------------------------------------

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



#**********************************************************************************
#    LAB 3                   PART C - For loops                                   *
#**********************************************************************************


# C.1. Loop overa list of names and print a numbered greeting for each.
#----------------------------------------------------------------------

# names = ["Ada", "Anna", "Tom", "Yerry", "Luisa", "Silvia", "Peter"]

# for number, name in enumerate(names, start=1):
#     print(f"{number}. Hej {name}, you are our lucky candidate.")


# C.2 Loop over numbers 1-50 and print only even numbers.
#--------------------------------------------------------

# i=1
# for i in range(1,51):
#     if i%2 ==0:
#         print(i)
#     i+=i


# C.3 Calculate a sum of a list manually using a loop rather than sum().
#-----------------------------------------------------------------------

# numbers = (1, 2, 3, 4, 5, 6, 7)

# summa=0
# for i in numbers :
#     summa += i     
    
# print(f"Summ of all elements in list numbers is: {summa}")


# C.4 Find the largest number in a list manually without max().
#--------------------------------------------------------------

# numbers = (1, 20, 3, 4, 5, 6, 7)

# maximum = 0
# for i in numbers :
#     if maximum < i:
#         maximum = i  
    
# print(f"Maximum of all elements in list numbers is: {maximum}")


# C.5 Count how many words in a list have more then five caracters.
#------------------------------------------------------------------

# words = ("Anna", "Bob", "Jack", "Marry", "Tom", "Jerry", "Nick", "Christopher")

# counter = 0

# for i in words:
#     if len(i) > 5:
#         counter += 1

# print(f"Total number of words in list words that have more then 5 characters is: {counter}") 


# C.6 Given a list of scores, count passes and failures using a treshold of 70.
#------------------------------------------------------------------------------

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
#---------------------------------------------------------------------------------------

# voters = {"Ava": 55, "Adam": 33, "Tom": 19, "Elly": 27, "Klas":65}
# print(voters)

# # for name in voters.keys():  # This is exempel 1 with .keys()
# #     print(name)

# for age in voters.values():   # This is the second exempel 1 with .values()
#     print(age)

# for name, age in voters.items():
#     print(f"{name} is {age} years old.")  # This is the third exempel with .items()




#**************************************************************************************
#      LAB 3             PART D - Range, enumerate and nested loops                   *
#**************************************************************************************


# D.1 Use range to print 10 down to 1.
#-------------------------------------

# for i in range(10,0,-1):
#     print(i)


# D.2 Generate the multiplication table for a number supplied by the user.
#-------------------------------------------------------------------------


# number = int(input("Enter a number for the multiplication table: "))

# print(f"\n---  Multiplication table for the number {number}  ---")

# for i in range(1, 11):
#     result = number * i
#     print(f"{number} x {i:2d} = {result}")


# D.3 Use enumerate to print a playlist with track numbers starting at 1.
#------------------------------------------------------------------------

# playlist = [
#     "Bohemian Rhapsody - Queen",
#     "Hotel California - Eagles",
#     "Imagine - John Lennon",
#     "Sweet Child O' Mine - Guns N' Roses",
#     "Billie Jean - Michael Jackson"
# ]
# print("="*90)
# print("---   PLAYLIST   ---")
# print("="*90)
# for track_number, song in enumerate(playlist, start=1):
#     print(f"{track_number}. {song}")
# print("="*90)


# D.4 Use mested loops to print coordinate pairs x=1..3 and y=1..4.
#------------------------------------------------------------------

# for x in range(1, 4):         # x goes from 1 to 3
#     for y in range(1, 5):     # y goes from 1 to 4
#         print(f"({x}, {y})")


# D.5 Create a simple 5x5 text grid using nested loops.
#------------------------------------------------------

# rows = 5
# cols = 5

# for r in range(rows):
#     for c in range(cols):
#         print("* ", end="")  # 'end=""' stops a new line efter every "*" symbol till end of all columns in row.
#     print()  # New line after we are done with all column for current row.




#************************************************************************************
#      LAB 3               Part E - While loops                                     *
#************************************************************************************


# E.1 Create a countdown from 10 to 0.
#-------------------------------------

# count = 10

# while count >= 0:
#     print(count)
#     count -= 1  


# E.2 Ask repeatedly for a password until the correct password is entered.
#-------------------------------------------------------------------------

# correct_password = "python123"  

# password_input = input("Enter password: ")

# while password_input != correct_password:
#     print("Incorrect password! Try again.\n")
#     password_input = input("Enter password: ")

# print("\nAccess granted! Welcome.")
# print()


# E.3 Create a manu that repeats until the user chooses 'quit'. 
#     The menu can simply print which option was selected.
#--------------------------------------------------------------


# while True:
#     print("="*30)
#     print("     ---     MENU    ---")
#     print("="*30)
    
#     print("1. Film")
#     print("2. Music")
#     print("3. Theatre")
#     print("Type 'quit' to exit.")
    
#     user_choice = input("Select an option: ").strip().lower()

#     if user_choice == "quit":
#         print("Exiting the program... Goodbye!")
#         break
#     elif user_choice == "1":
#         print("You selected: Film.")
#     elif user_choice == "2":
#         print("You selected: Music")
#     elif user_choice == "3":
#         print("You selected: Theatre.")
#     else:
#         print("Invalid option, please try again.")


# E.4 Ask the user for numbers until they enter 0. Keep a running total.
#----------------------------------------------------------------------

# running_total = 0

# while True:
#     number = int(input("Enter a number (or 0 to stop): ")) # It is possible to define number as float, but ...
    
#     if number == 0:
#         break
        
#     running_total += number
#     print(f"Current running total: {running_total}")

# print(f"\nFinal Total: {running_total}\n")


# E.5 Create a guessing loop with a fixed secret number. Tell the user whether each guess is too high or too low.
#---------------------------------------------------------------------------------------------------------------

# secret_number = 42

# print("\n   --- Guess the Secret Number ---\n")

# while True:
#     guess = int(input("Enter your guess: "))
    
#     if guess == secret_number:
#         print("Congratulations! You guessed the correct number!")
#         break
#     elif guess < secret_number:
#         print("Too low! Try again.\n")
#     else:
#         print("Too high! Try again.\n")
# print()



#********************************************************************************************
#     LAB 3                 Part F - Break and continue                                     *
#********************************************************************************************


# F.1 Loop through numbers 1-100 and stop when you reach the first number divisible by both 7 and 9.
#---------------------------------------------------------------------------------------------------

# for number in range(1, 101):
#     if number % 7 == 0 and number % 9 == 0:
#         print(f"You found the number: {number}")
#         break
#     print(number, end=" ") # With "end=" " can we write all numbers in one line....



# F.2 Loop through a list of strings and skip empty strings using continue.
#--------------------------------------------------------------------------

# strings = ["python", "", "java", "  ", "", "C#", "C++"]

# for s in strings:
#     if not s.strip():     # Check if string is empty or contains only whitespace
#         continue
    
#     print(f"Not empty strings: {s}")



# F.3 Search a list for a target name. Print 'found' and break when it appears; otherwise
#     explain how you know it was not found.      
#----------------------------------------------------------------------------------------

# names = ["Ada", "Anna", "Tom", "Yerry", "Luisa", "Silvia", "Peter"]
# target_name = "Novica"
# print()

# for name in names:
#     if name == target_name:
#         print(f"Found: {target_name}")
#         break
# else:
#     print(f"Target '{target_name}' was not found after checking all elements in the list.")
# print()


# 
# F.4 Process a list of numeric values where negative values should be skipped and 
#     processing stops completely when the value 999 appears.    
#----------------------------------------------------------------------------------

# numbers = [10, -55, 20, -12, 45, 777, 999, 303, 123, -200]

# for num in numbers:
#     if num == 999:
#         print("Congratulations, you have found the number 999!")
#         break
    
#     if num < 0:
#         continue  # Skip negative numbers
    
#     print(f"Processing value: {num}")



#****************************************************************************************************
#     LAB 3              Part G - Applied  challenge: Console study tracker                         *
#****************************************************************************************************


# G.1 Create a list of dictionaries representing at least ten study sessions with subject and minutes.
#-----------------------------------------------------------------------------------------------------

study_sessions = [
    {"subject": "Python Programming", "minutes": 45},
    {"subject": "Mathematics", "minutes": 60},
    {"subject": "Database Systems", "minutes": 30},
    {"subject": "Python Programming", "minutes": 90},
    {"subject": "Web Development", "minutes": 50},
    {"subject": "Mathematics", "minutes": 40},
    {"subject": "Data Structures", "minutes": 75},
    {"subject": "Python Programming", "minutes": 60},
    {"subject": "Operating Systems", "minutes": 45},
    {"subject": "Web Development", "minutes": 35}
]

# for index, session in enumerate(study_sessions, start=1):
#     print(f"Session {index:2d}: {session['subject']} - {session['minutes']} mins")



# G.2 Loop through the sessions and calculate total minutes.
#-----------------------------------------------------------

# I use a dictionary {study_sessions} from G.1
# total_minutes = 0

# for session in study_sessions:
#     total_minutes += session["minutes"]

# print(f"Total study time: {total_minutes} minutes")



# G.3 Calculate total minutes per subject using a dictionary that starts empty and is uppdated inside the loop.
#--------------------------------------------------------------------------------------------------------------

# I am using the {study_sessions} dictionary from G.1

# subject_totals = {}

# for session in study_sessions:  #creating a new dictionary with uniq subjects and sum of minutes
#     subject = session["subject"]
#     minutes = session["minutes"]
    
#     if subject in subject_totals:
#         subject_totals[subject] += minutes
#     else:
#         subject_totals[subject] = minutes



# print("\n---   TOTAL MINUTES PER SUBJECT   ---\n") # printing uniq dictionary
# for subject, total in subject_totals.items():
#     print(f"{subject}: {total} minutes")
# print()


 
# G.4 Identify the longest study session without max(..., key=...).
#--------------------------------------------------------------------

# Here too, I use the {study_sessions} dictionary from G.1.

# longest_study_session = None
# # print(type(longest_study_session)) # test
# max_minutes = 0

# for session in study_sessions:
#     if session["minutes"] > max_minutes:
#         max_minutes = session["minutes"]
#         longest_study_session = session

# # Display the result
# print("\n--- LONGEST STUDY SESSION ---")
# if longest_study_session:
#     print(f"Subject: {longest_study_session['subject']}")
#     print(f"Duration: {longest_study_session['minutes']} minutes\n")


# G.5 Print only sessions longer than 45 minutes.
#------------------------------------------------

# longest_study_session = None
# limit_minutes = 45    #  we use this variable in stead of 45 in if-statement, to have flexibility if we want to change limit.

# print(f"\n--- SESSION(S) LONGER THEN {limit_minutes} minutes  ---\n")

# for session in study_sessions:
#     if session["minutes"] > limit_minutes:   
#         print(f"Subject: {session['subject']:20s} - Duration: {session["minutes"]} minutes.")
# print()


# G.6 Create a repeated menu that lets a user: view all sessions, view total time, filter by subject, or quit.
#-------------------------------------------------------------------------------------------------------------





# G.7 Use break/continue where they genuinely improve the flow.
#---------------------------------------------------------------



#***********************************************************************************************
#      LAB 3                Part H - Stretch challenges                                        *
#***********************************************************************************************


# H.1 Print FizzBuzz from 1 to 100: multiplies of 3 -> Fizz, 5->Buzz, ->FizzBuzz.
#--------------------------------------------------------------------------------



# H.2 Given a sentence, count vowels without using .count() repeatedly.
#----------------------------------------------------------------------

# def count_vowels(text):
#     vowels = set("aeiouAEIOU")
#     total_vowels = 0
    
#     for char in text:
#         if char in vowels:
#             total_vowels += 1
    
#     return total_vowels

# print("\n  ---  Count vowels in a sentence  --- \n")
# sentence = input("Enter a sentence:")
# total = count_vowels(sentence)

# print(f"Sentence: '{sentence}'")
# print(f"Total vowels count: {total}")



# H.3 Find all duplicate values in a list using loops and collections.
#---------------------------------------------------------------------

# def find_duplicates(items):
#     bas_set = set()
#     duplicates = set()
    
#     for item in items:
#         if item in bas_set:
#             duplicates.add(item)
#         else:
#             bas_set.add(item)
            
#     return list(duplicates)


# # Example usage
# numbers = [1, 3, 4, 2, 3, 5, 1, 7, 8, 3, 2]
# duplicate_numbers = find_duplicates(numbers)

# print("Original list:", numbers)
# print("Duplicate values:", duplicate_numbers)

 
# H.4 Build a simple text histogram: for each number in [3,5,2], print that many * characters.
#---------------------------------------------------------------------------------------------






# ********************************   END - LAB 3   *********************************************