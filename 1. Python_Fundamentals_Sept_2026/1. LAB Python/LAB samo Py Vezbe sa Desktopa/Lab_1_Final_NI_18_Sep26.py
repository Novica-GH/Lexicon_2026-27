#*******************************************************************************************
#  Novica Ivkovic                                                                           *         
#  Cours: System Developer Python and AI                                                    *
#  September 8 2026 - LAB 1                                                                 *
#       Today's study goal is Python basics                                                 *
#********************************************************************************************


#********************************************************************************************
#   LAB 1                   Part A - Warm-up: Python basics                                 *
#********************************************************************************************

# Part A.2. Create variables for a person's name, age height in meters and whether
#     they are currently a student. Print both the values and their types.
#--------------------------------------------------------------------------------

# person = "Adam"
# age = 18
# height = 1.75
# currently_study = True
#print (person)
#print(type(person))
#print (age)
#print(type(age))
#print (height, " m")
#print(type(height))
#print (currently_study)
#print(type(currently_study))



# Part A.3 Change the value stored in one variable to a different data type. Print its type before and
#          after the change. Explain in a comment what this demonstrates about Python.
#----------------------------------------------------------------------------------------------------

#number = 5
#print(type(number))
#Print data type before change
#number = 5/2
#print(type(number))
# Print data type after change
# This demonstate that we kan change data type without deklaration or definition, but via operation with it.



# Part A.4 Create two numeric variables and calculate addition, subtraction, multiplication, normal division, 
# floor division, remainder and exponentioation.. Print a readable label before each result.
#-----------------------------------------------------------------------------------------------------------

# print("")
# print ("Input the first number:")
# a = input()     #Input a by default is string, even it is a number, ie. 5
# print (type(a))
# a = int(a)      #Change a wich is a string to integer
# if a < 1:
#     print("Try a to be positiv integer!")
#     print("Input again first number: ")
#     a = int(input())
# print (type(a))
# print ("Input the second number:")
# b = int(input())  #Here I do inputing and transform to integer directly 
# print(type(b))
# if b == 0:
#     print("b have to be different of 0!")
#     print("Input again second number: ")
#     b = int(input())
#
# print (f"{a} is the first number and {b} is the second number.")
# sum = a + b
# print(f"{a} + {b} is equal {sum}")
# sub = a - b
# print(f"{a} - {b} is equal {sub}")
# product = a * b
# print(f"{a} * {b} is equal {product}")
# div = a / b
# div = int(div)   # Here we would like to have integer dividing
# print(f"{a} / {b} is equal {div}")
# div_f = a / b
# print(f"{a} // {b} is equal {div_f}")
# remainder = a%b
# print(f"{a} % {b} is equal {remainder}")
# exponent = a ** b
# print(f"{a} ** {b} is equal {exponent}")
# print("")



# Part A.5 Write three examples where explicit type conversion is necessary:
#         string to int, int to float and number to string
#---------------------------------------------------------------------------
#
# a_input = input("Input some number: ")
# a= int(a_input)
# print(a, type(a))

# b= float(a)
# print(b, type(b))

# c = str(a)
# print(c, type(c))




#************************************************************************************************
#   LAB 1                   Part B - User input and calculation                                 *
#************************************************************************************************

#Part B.1 Build a small profile program that asks for name and year of birth,
#         then prints an approximate age using the current year supplied in a variable.
#--------------------------------------------------------------------------------------

# n_input = input("What is your name: ")
# name = str(n_input)
# y_input = input("What is your year of birth: ")
# year = int(y_input)
# current_year = 2026
# old = 2026 - year
# print (f"Hi {name}, you are {old} year old.")



#Part B.2 Ask the user for the price of an item and a discount procentage. 
#         Calculate and print the final price. Round the displayed result to two decimals.
#-----------------------------------------------------------------------------------------

# p_input = input("Hi, what is the price of this item: ")
# price = float(p_input)
# d_input = input("Tell me the discount for this item in procetage: ")
# discount = float(d_input)
# final_price = price * (100 - discount)/100
# #final_price = round(price * (100 - discount)/100,2) Alternative solution with 2 decimal places
# print (f"Hi, your final price is {final_price:.2f} $.") #Alternative 2 for 2 dec.places
# final_price = round(final_price, 2)
# print (f"Hi, your final price is {final_price} $&.") # OBS!!! This PART have a PROBLEM - only 1 dec!



# Part B.3 Ask for a temperature in Celsius and convert it to Fahrenheit using F=C*9/5 + 32.
#-----------------------------------------------------------------------------------------

# t_input = input("Hi, what the current temperature in Celsius? ")
# temperature = float(t_input)
# fahrenheit = temperature * 9/5 +32
# print (f"Hi, {temperature:.0f}  temperature in Celsius is {fahrenheit:.0f} in Fahrenheit.")



# Part B.4 Ask for the length and widh of a room and calculate area and perimeter. Use descriptive
#         variable names. Python Foundation - Lesson 1 Exercises Page 2
#-------------------------------------------------------------------------------------------------

# l_input = input("Hi, what is length of this room? ")
# length = float(l_input)
# w_input = input("Hi, what is widh of this room? ")
# widh = float(w_input)
# area = length * widh
# perimeter = 2 * (length + widh)
# print (f"Hi, area for this room is {area:.2f} m2.")
# print (f"Hi, perimeter for this room is {perimeter:.2f} m.")



# Part B.5 Extend one of the programs so invalid numeric input is discussed in comments: 
#         what would happen today if the user entered 'hello'? Go not solove it with exceptions yet.
#    - Handling invalid numeric input without exceptions (try-except)  
#---------------------------------------------------------------------------------------------------

#p_input = input("Hi, what is the price of this item: ")
#
# COMMENT / DISCUSSION:
# What happens today if the user enters 'hello'?
# If we directly call float ('hello'), Pyton throws a ValueError (could not convert)
# and the program crashes immediately.
# Since we cannot use try-except blocks yet, we can check if the input is valid using
#
# Checking if input consists only of digits (or replacing decimal point for float character)
#
# if p_input.replace('.', '', 1).isdigit():
#     price = float(p:input)

#     d_input = input("Tell me the discount for this item in percentage: ")

#     if d_input.replace('.', '', 1).isdigit():
#         discount = float(d_input)

#         final_price = price * (100 - discount) / 100
#         print(f"Hi, your final price is {final_price:.2f}.")
#     else:
#         print("Invalid discount percentage entered! Please enter a valid number.")
# else:
#     print("Invalid price entered! Please enter a valid numeric value.")
#
# Kljucne tacke za komentar u zadatku su:
# 1. Trenutno ponasanje(Behavior): Poziv float("hello") ili int("hello") 
#    momentalno rusi aplikaciju uz ValueError.
# 2. Alternativa bez izuzetka (non-exception check): Metod
# p_input.replace('.', '', 1).isdigit() proverava da li string sadrizi samo cifre
#     (uz tolerisanje jedne tacke za decimalne brojeve) pre nego sto se uopste pozove float().




#*******************************************************************************************************
#   LAB 1                           PART C - Strings                                                   *
#*******************************************************************************************************

# C.1. Store a full sentence in a variable. Print its length, uppercase version, lowercase version 
#    and a version with leading/trailing whitespace removed.
#-------------------------------------------------------------------------------------------------

# sentence_input = input("Hi, write your sentence: ")
# sentence = str(sentence_input) # Ovo je visak, jer je u prethodnom redu, by default, vec unesen string!
# length = len(sentence)
# print(f"Length of your sentence is: {sentence}")
# uppercase = sentence.u
# widh = float(w_input)
# area = length * widh
# perimeter = 2 * (length + widh)
# print (f"Hi, area for this room is {area:.2f} m2.")
# print (f"Hi, perimeter for this room is {perimeter:.2f} m.")
# text = "0123456789"
#print(text[1:len(text)-1])
#print(text[0:5])
#print(text[::-1])



# C.2 Ask for first name and last name. Create a formatted full name using an f-string.
#--------------------------------------------------------------------------------------

# first_name = input("Tell me your name: ")
# last_name = input("Tell me your last name: ")

# full_name = f"{first_name} {last_name}"

# print(f"Your formated full name is: {full_name}.")




# C.3 Given the string 'python programming', print the first character, last character, 
#     first six characters, last eleven characters and the entire string reversed.
#--------------------------------------------------------------------------------------

# sentence = 'python programming'

# print(f"The first character is: {sentence[0]}")

# print(f"The last character is: {sentence[-1]}")

# print(f"The first six characters are: {sentence[:6]}")

# print(f"The last 11 characters are: {sentence[-11:]}")

# print(f"The entire string reversed is: {sentence[::-1]}")
#-------------------------------------------------------------------


# C.4 Create a username generator: ask for first and last name, remove surrounding spaces,
#     convert to lowercase and create a username using the first three letters of the first
#     name plus the first five letters of the last name.
#------------------------------------------------------------------------------------------

# first_name = input("Tell me your name: ")
# last_name = input("Tell me your last name: ")

# clean_first_name = first_name.strip().lower()
# clean_last_name = last_name.strip().lower()

# username = clean_first_name[:3] + clean_last_name[:5]

# print(f"Generated user name is: {username}")




# C.5 Given an email adress, use string operations to extract the part before @ and the domain
#      after @. Assume exactly one @ for this exercise.
#-----------------------------------------------------------------------------------------

# email = "petar.petrovic@gmail.com"

# username, domain = email.split('@')

# print(f"User name is: {username}")
# print(f"Domain is: {domain}")
#--------------------------------------------------------


# C.6 Create a sentence containing the word 'Java'. Relpace it with 'Python' and print both
#      the original and changed sentence.
#------------------------------------------------------------------------------------------

# original_sentence = " I have had learned Java a long, long time ago."

# changed_sentence = original_sentence.replace ("Java", "Python")

# print(f"Original sentence is: {original_sentence}")
# print(f"Changec sentence is: {changed_sentence}")



#****************************************************************************************************
#   LAB 1                       PART D - String investigation                                       *
#****************************************************************************************************

# D.1 Predict the output of at least eight expressions using indexing and slicing before running them.
#      Include positive indexes, negative indexes, omitted start/end values and a step.
#----------------------------------------------------------------------------------------------------

# expression = "Programming is fantastic!"

# expres1 = expression[1] # Positive index.
# expres2 = expression[-1] # Negative index.
# expres3 = expression[:5] # Omitted start.
# expres4 = expression[5:] # Omitted end.
# expres5 = expression[3:10:2] # Range - index 3 to 10, with positiv step 2.
# expres6 = expression[10:3:-2] # Range - index 10 to 3, with negativ step -2.
# expres7 = expression[::-1] # Reversed the whole string.
# expres8 = expression[7::-1] # Reversed the string slice.
# print (expres1, expres2, expres3, expres4, expres5, expres6, expres7, expres8)



# D.2 Create a variable containing 'Artificial Intelligence'. Produce at least six different slices 
#     from it and comment what each slice means.
#--------------------------------------------------------------------------------------------------

# variabla ="Artificial Intelligence"
#          01234567891123456789011
# print(len(variabla)) 
# slice1 = variabla[0:5] #  This is a slice of first 5 charachters.
# slice2 = variabla[1:10] #  This is a slice of 9 charachters, starting with the second character in the string.
# slice3 = variabla[:-1] # This is a sclice of all characters from the string, withoout the last one.
# slice4 = variabla[:5:2] # This slice we made when we take every second character from the first 5 characters in the string.
# slice5 = variabla[20:10:-2] # This slice takes every second character starting from index 20 to index 10.  
# slice6 = variabla[15::-3] # This slice takes every third character starting from index 15 to index 0.
# slice7 = variabla[10::5] # This slice takes every fifth character starting from index 10 and go the last character in the string.
# print(slice1)
# print(slice2)
# print(slice3)
# print(slice4)
#print(slice5)
#print(slice6)
#print(slice7)




# D.3 Investigate the difference between .split(), .strip(), replace() and the in operator. 
#      Write one ueful example of each.
#------------------------------------------------------------------------------------------

# .split() - Divide a string to few parts by separator and pach them in a list.
# .strip() - Cleaning all blancks from the begining and from the end of a string and return changed (cleaned) string.
# .replace() - Replace one or all the same parts in one string with the another word(part). And return changed string.
# in - check if one part of a string is in the string. Or if some element is in a collection. It returnes True/False.



# D.4 Demonstrate string immutability: attempt conceptually to change one character, explain why direct
#     character assignment fails, then create a new modified string instead
#------------------------------------------------------------------------------------------------------

# string = "Python"
# string[0] = "M" # This attempt gives Error => String is immutable

# modified_string_1 = "M" + string[1:]  # This is one way how we kan create another string with changed character
# print(modified_string_1)
# modified_string_2 = string.replace("P", "M") # And this is another way
# print(modified_string_2)




#******************************************************************************************************
#   LAB 1               Part E - Applied challenge: Registration summary                              *
#******************************************************************************************************

# E.1 Build a console program that collects: first name, last name, city, year of birth and
#      favourite programming language.
#------------------------------------------------------------------------------------------

# first_name = input("Hi, tell me your name: ")
# last_name = input("Tell now me your last name: ")
# city = input("What is the name of your city: ")
# b_y = input("What year were you born: ")
# prog_language = input("What is you favourite programming language: ")

# print(f"{first_name} {last_name} born in {b_y} lives in {city} and likes {prog_language}.")



# E.2 Normalize text input so accidental surrounding spaces do not affect the result.
#------------------------------------------------------------------------------------

# text = "    Text text text    "

# clean_text = text.strip()
# print(clean_text)


# E.3 Create a generated user ID from parts of the person's name and year of birth.
#----------------------------------------------------------------------------------

# name = input("Hi, tell me your name: ")
# birth_year = input("What year were you born: ")

# userID = name[:4] + birth_year[2:4]

# print(f"Generated userID is: {userID}")


# E.4 Print a clean multi-line summary using f-strings.
#------------------------------------------------------

# first_name = input("Hi, tell me your name: ")
# last_name = input("Tell now me your last name: ")
# city = input("What is the name of your city: ")
# b_y = input("What year were you born: ")
# prog_language = input("What is you favourite programming language: ")

# summary = f"""
# ****************************************************************************
#                   PERSON SUMMARY
# ****************************************************************************
#     Citizen:              {first_name} {last_name}
#     City   :              {city}
#     Born   :              {b_y}
#     Programming language: {prog_language}
# ----------------------------------------------------------------------------
# """
# print(summary)
#-------------------------------------------------


# E.5 Print the initials, full name length excluding the space, and the favourite language reversed.
#---------------------------------------------------------------------------------------------------

# first_name = input("Hi, tell me your name: ")
# last_name = input("Tell now me your last name: ")
# language = input("What is you favourite language: ")
# initials = first_name.strip()[0] + last_name.strip()[0]
# full_name = first_name.strip() + " " + last_name.strip()
# length = len(full_name)-1
# lang_reversed = language[::-1]
# summary = f"""
# ****************************************************************************
#                    PERSON SUMMARY
# ****************************************************************************
#      Initials:              {initials}
#      Full name:             {full_name}
#      Name's length:         {length}
#      Favourite language-1:  {lang_reversed}
# ----------------------------------------------------------------------------
# """
# print(summary)
#----------------------------------------------------



# E.6 Add at least three extra pieces of derived information of your own choice using only concepts
#     from Lesson 1.
#--------------------------------------------------------------------------------------------------

# first_name = input("Hi, tell me your name: ")
# last_name = input("Tell now me your last name: ")
# language = input("What is you favourite language: ")
# email = "novica.ivkovic@google.com"
# password = input("Hi, input your password: ")
# pass_1 = password[0]
# phone = input("What is you telefon number: ")
# phone_last4 = phone[-4::1]
# #1.
# username = email.split("@")[0] # take username from email
# name_of_user = username.split(".")[0] # separate username to name och last name and take just name.

# secret_password = pass_1 + "*" * len(password) # 2. Write first character of password and rest is *.
# print(secret_password)
# print(f"Your phone has these last 4 digits: {phone_last4}") # 3. Write 4 last phone numer's digits.



#*******************************************************************************************************
#   LAB 1                   Part F - Stretch challenges Phyton Foundation                              *
#*******************************************************************************************************

# F.1 Create a simple second converter: input total seconds and calculate whole hours, 
#     remaining minutes and remaining seconds using // and %.

# total_seconds = int(input("Input total number of seconds: "))

# hours = total_seconds // 3600
# rest_h_seconds = total_seconds % 3600

# minutes = rest_h_seconds // 60
# seconds = rest_h_seconds % 60

# print(f"Total {total_seconds} seconds givs {hours} hours, {minutes} minutes and {seconds} seconds.")



# F.2 Given a four-digit integer, extract and print each digit without converting the number to a string.
#-------------------------------------------------------------------------------------------------------

# number = int(input("Input four digits number: "))

# tusentals = number // 1000

# hundratals = (number // 100) % 10

# tiotals = (number // 10) % 10

# units = number % 10 

# print(f"Original number is: {number}")
# print(f"Digit thousands is: {tusentals}")
# print(f"Digit hundreds is: {hundratals}")
# print(f"Digit tens is: {tiotals}")
# print(f"Digit units is: {units}")




# F.3 Create a text masking program that displays only the first two and last two characters of a supplied 
#     word, replacing the middle with * caracters.
#---------------------------------------------------------------------------------------------------------

# word = input("Write a worid for masking: ")
# word_len = len(word)

# if word_len > 4:
#     first_2 = word[:2]
#     last_2 = word[-2:]

#     stars = "*" * (word_len - 4)

#     masked_word = first_2 + stars + last_2
# else:
#     masked_word = word

# print(f"Original word is: {word} and masked word is: {masked_word}")


# 
# F.4 Write five short'predict before running'examples that you could give to another student.
#     Include at least one type conversation and two string slices.
#-----------------------------------------------------------------------------------------

# text_1 = "Hello World"
# text_2 = "Name" 
# text_3 = "Year"
# text_4 = "1236"
# text_5 = "2 + 2"

# 
# **********************************   END - LAB 1   ******************************************* 