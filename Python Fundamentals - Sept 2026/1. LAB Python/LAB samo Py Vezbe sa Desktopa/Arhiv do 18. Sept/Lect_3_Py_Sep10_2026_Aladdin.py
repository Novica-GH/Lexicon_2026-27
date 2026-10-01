# 2026-09-10 


# Comparisons

# print(5 > 2)
# print(5 < 2)
# print(5 == 2)
# print(5 != 2)
# print(5 >= 2)
# print(5 <= 2)
#----------------------------------------

# Important distinction to make

# number = 10

#print(number == 10) # return True
#---------------------------------------

# print(1 == 1)      # return True
# print(1 == '1')    # return False
# print('1' =='1')   # return True
#-------------------------------"

#+++++++++++++++++++++++++++++++++++++++++++++++++++
# Boolean opperators: and, or , not     &&  ||  !
#---------------------------------------------------

# AND     -  All conditions True -> True
# age = 23
# has_ticket = True

# print(age >=18 and has_ticket)
#---------------------------------
 
# OR      -  At least one condition must be True -> True   

# is_admin = False
# is_teacher = True

# print (is_admin or is_teacher)
#--------------------------------

# NOT      -  Reverse the boolean value

# is_logged_in = False

# print(is_logged_in)
# print (not is_logged_in)
#-----------------------------------

# Key word "in"

# languages = ["Python", "Java", "C#"]

# print("Python" in languages)
# print("Rust" in languages)
# print ("Rust" not in languages)
#------------------------------------------

# Identation

# In many languages {} uses to write code blocks (like in Java, C#, JavaScript, ...)

# But, Python doesn't use {} to define normal code blocks!
# Python uses {} for Identation
# In next exempel, : oznacava da print() pripada if bloku. I to se zove identacija...

# age = 20

# if age >= 18:
#     print("Adult")  # na osnovu identacije samo ovaj print pripada if-u - i obicno je uvucen za 4 mesta u desno.
#                     # Znaci na osnovu uvlacenja i posle : pravimo blok...
# print("test")       # ovaj deo ne pripada if-u, na osnovu ili zbog identacije.  
#-----------------------------------

# else - inace uradi - alternativa:

# age = 20

# if age >= 18:
#     print("Adult")

# else:
#     print("Under 18") 
#---------------------------------------------
#  elif - like case in Pascal - OBS! Order metters!

# score = 80

# if score >= 90:
#     print("Grade A")
# elif score>= 80:               # case
#     print("Grade B")
# elif score >= 70:              # case
#     print("Grade C")
# else:                          # inace uradi ovo
#     print("Below C")
#
# Ovde je redosled uslova jako bitan za ispis i logiku problema!
#--------------------------------------------------

age = 15
has_ticket = True

# if age >= 18 and has_ticket:
#     print ("You may enter!")
# else: 
#     print("Entry denied!")

#------------------------

# age = 15
# has_ticket = True

# if age >= 18: 
#     if has_ticket:
#         print ("You may enter!")
#     else:
#         print("You need a ticket!")
# else: 
#     print("Entry denied, you are to young!")

#------------------------


# Falsy -> empty-string/list/zero/None
#Truthy ? -> Something that allways gives true??? It needs to be checked by teacer Aladdin.

# Empty values are empty strings, empty lists, zero - generally treated that as falsy! False
#----------------------------------

# name=""               # If we change name to "Aladdin", it going to write (We have a name)

# if name:   
#     print("We have a name")
# else:
#     print("The name is empty")
#--------------------------------

# items = []

# if items:
#     print ("The list contains data")
# else:
#     print("The list is empty")
#------------------------------------
name=""  # If we change name to "Aladdin", it going to write (We have a name)

# if name:   
#     print("We have a name")
# else:
#     print("The name is empty")
#----------------------------------------------





#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
#     LOOPS
#################################################################


languages = ["Python", "Java", "C#", "JavaScript"]

    # print(languages[0])
    # print(languages[1])
    # print(languages[2])
    # print(languages[3])
   # Umesto ovog gore, da ne bismo pisali print za svakog clana liste, to elegantnije mozemo resiti petljom for:

 # for-loop

# for language in languages:
#     print(language)

# word = "Python"

# for character in word: 
#     print(character)
#----------------------

# numbers = [3, 8, 12, 5, 20, 7]

# for number in numbers:
#     if number>=10:
#        print (number)
#------------------------

# numbers = [-4, -3, -2, -1, 0, 1, 2, 3, 4, 5, 6]

# for number in numbers:
#     if number %2 ==0:   # check if number is even. If is it so, print that number
#         print(number)


# student = {
#     "name": "Ada",
#     "age" : 25,
#     "course": " AI Developer"
# }

# for key in student:
#     # print(key)
#     print(key, student[key])

    #------------------------------
#     student = {
#     "name": "Ada",
#     "age" : 25,
#     "course" : {
#     " AI Developer",   # OBS Ovde mi fali course ili course 2 1
#     "course" : "English" 
#     }
#     }
# for key in student:
#     # print(key)
#     print(key, student[course]]course1) # Ovde mi fali coruse ili course 21

    #----------------------------------------------

# student = {
#     "name" : "Ada",
#     "age": 25,
#     "course": "AI Developer"
# }

# for key, value in student.items():
#     print ??????????????

# students = [
#     {
#         "name": "Anna", 
#         "score":85
#         }
#     {"name": "Bob", "score":62},
#     {"name": "Charlie", "score":91}
# ]
#---------------------------------

# students = [
#     {"name": "Anna", "score":85},
#     {"name": "Bob", "score":62},
#     {"name": "Charlie", "score":91}
# ]

# # for student in students:
# #     print(student["name"])

# for student in students:
#     if student["score"] >= 70:
#         print (student["name"],"passed")
#------------------------------------------

# for number in range(5):
#     print(number)


# for number in range(2,10):
#     print(number)

# for number in range(2,10,2):
#     print(number)
#--------------------------

# languages = ["Python", "Java", "C#"]

# for i in range (len(languages)):   # primer 1 i primer 2 rade isto, 
#     print(languages[i])

# for language in languages:         #primer 2 - on je udobniji
#     print (language)

#-------------------------------

# languages = ["Python", "Java", "C#"]

# for index, language in enumerate(languages):
#     print(index,language)

#************************************************************
#
# WHILE - loops

# count = 1

# while count <= 5:
#     print(count)
#     count = count + 1  #  The same expresion is:  count += count - Python's way

#-----------------------

# while count <= 5:
#     print(count)
#*****************************************

# break and continue

# numbers = [2, 4, 5, 7, 8, 10]

# for number in numbers: 
#     if number %2 != 0:
#         print("Found an odd numer;",number)
#         break


# numbers = [2, 4, 5, 7, 8, 10]

# for number in numbers:
#     if number ==3:
#         continue
#     print(number)


