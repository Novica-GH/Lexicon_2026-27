#******************************************************************************************
# Novica Ivkovic
# Cours: System Developer Python and AI
# September 15 2026 - Today's study goal is: Local/global/Override/*args/**kvargs/Unpack dictionary
#                
#
#*******************************************************************************************
# Part A - LOCAL AND GLOBAL VARIABLE
#***************************************************************************** 
#
# def calculate_total(price, quantity):
#     return price * quantity

# result = calculate_total(199,3)

# print(result)
# #-----------------------------------------

# def greet():
#     message = "Hello from global scope"  # Local scope
#     print(message)

# print(mesaga) # problem - mesage je lokalna promenljiva u funkciji i vratice Error

# #"------------------------------------------"

# message = "Hello from global scope"    # Global scope

# def greet():
#     print(message)


#--------------------------

# message = "Global message"

# def greet():
#     message = "Local message"
#     print(message)


# greet()
# greet(message)

#--------------------------------------------------------

# def greet(name):
#     message = "Hello " + name
#     print(message)

# greet("Ada")  # Ok 

# print(name)   # Problem, name id defined localy
#-------------------------------------------------------

# lookup rule ->  LEGB

#L = Local
#E = Enclosing
#G = Global
#B = Built-in

# name = "Global Ada"

# def greet():
#     name = "Local Grade"
#     print(name)

# greet()
#----------------------------------------

# numbers = [1, 2, 3]

# print(len(numbers))
#-------------------------------

# list = [1, 2, 3]

# print(list)

# new_list = list("Python") # Problem override - OVER RIDE
#--------------------------------

#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# tIPS avoid names list, str, int, print, sum, max
#  Tips: avoid alla sluzbene reci
#----------------------------------------------------

# def outer():
#     message = "Hello from outer"

#     def inner():
#         print(message)

#     inner()

# outer()

#-------------------------------------------------

# counter = 0

# def increase_counter():      #Ovde se counter nece povecati
#     counter += 1
#     print("Inside: ",counter)

# increase_counter()

# print("Outside: ", counter)
#---------------------------------------------------------

#counter = 0

# def increase_counter():     # Ovo ce dati povecanje countera
#     global counter
#     counter += 1
#     print("Inside: ",counter)

# increase_counter()

# print(counter)


# counter2 = 0

# def increase_counter(current_counter):
#     return current_counter(counter2)

# print(counter2)

#---------------------------------------------

# x = 10 

# def example():
#     x = 20
#     print("Inside: ",x)

# example()

# print("Outside:", x)
#----------------------------------------


# total = 100

# def add_tax():
#     total = total * 1.25
#     return total

# add_tax()  # UnboundLocalError: cannot access local variable 'total' where it is not associated with a value


# Rewrite the function WITHOUT using global 

total = 100

# def add_tax():
#     total_1 = total * 1.25   # Moje resenje
#     print(total_1)
#     return total_1
    

# add_tax()
# #-----------------------------------------------

# total = 100

# def add_tax(amount):          # Elegant sollution OK OK
#     return amount * 1.25
    
# total = add_tax(total)

# add_tax()
#--------------------------------


# total = 100

# def add_tax():
#     total = 100
#     total = total * 1.25   # Murtaza
#     return total
    

# add_tax()



#******************************************************************************************
# Part B 10:15 - A problem with fixt number in parameters.  
#*************************************************
#ANOTHER FUNCTION PROBLEM:

# def add_number(a,b):   # Nisam cu pitanje
#     return a + b

# print(add_number(10,20))
# #-----------------------------------

# def add_number(a,b,c):  
#     return a + b + c 

# print(add_number(10,20,30))
# #-----------------------Another day I want more variables

# def add_number(a,b,c,d,e):  
#     return a + b + c +d +e

# print(add_number(10,20,30, 40, 50 ))

#------------------------------

#*************************************************************************************************
# For this situations Python has something for us: args

# args - are standard collection
#************************************************************#

# def show_numbers(*args):   # Sada ce parametar primiti neograniceno mnogo argumenata
#     print(args)

# show_numbers(10, 20, 30)    # ovo su uredjeni parovi - torke - tupples
# show_numbers(1)
# show_numbers(1,2)
# show_numbers(1,2,3,4,5)

# def show_numbers(*numbers):   # Sada ce parametar primiti neograniceno mnogo argumenata
#     print(numbers)

#-------------------------------------++++++++++++++++++++++++++++++++

# def show_names(*args):
#     for name in args:
#         print(name)


# show_names("Ada","Grace","Guido")
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++

# def add_numbers(*args):
#     total = 0

#     for number in args:
#         total += number

#     return total

# print(add_numbers(10,20))
# print(add_numbers(10,20,30,40))
# print(add_numbers(1,2,3, 4, 5, 6))
#---------------------------------------------------------------

# def calculate_total(discount, *prices):
#     total = 0

#     for price in prices:
#         total += price

#     return total *(1 - discount)

# print(calculate_total(0.10,100,200,300))  # Prvi argument je prvi parametar u funkciji, dok svi ostali parametri idu na drugi parametar funkcije.


#************************************************************************************************
# USEFUL with *args:   for tuples
#**********************************************************************************
# - The function should accept several positional values
# - The exact number of values is not known in advance

# - If function demand just 2 parameters, than we don't need args!
# - But in cases, that we.....

# def calculate_area(width, height):   # Ovde nam je sve dovloljno za zadatak. Ne treba args
#     return width * height

# # less clearer

# def calculate_area(*args): # ovo je fleksibilna verzija, ali je i zbunjujuca!!!
#     return args[0]* args[1]
#---------------------------------------------------------


# # OBS WC WC WC
# def add_three(a,b,c):
#     return a+b+c

# numbers = (5,10,15)

# print(add_three(*numbers)) # add OK

# values = (50,10,15, 20) # TypeError: add_three() takes 3 positional arguments but 4 were given

# print(add_three(*values))
#---------------------------------------


#******************************************************************************************************
# named arguments    **KWARGS ->  dictionary
#******************************************************************************************************

# - name age, ....... city, email, role, department
# - We might not know all parameters...
# - And Python provides:  **kwargs

# - We can acces variables from kvargs....


# def show_user(**kwargs):
#     print(kwargs)

# show_user(name="Ada", age=36, city="London")

#+++++++++++++++++++++++++++++++++++++++++++++++++++
#--------------------------------

# def show_user(**information):
#     print(information)

# show_user(name="Ada", age=36, city="London")


#---------------------Acces variables from kvargs:

# def show_user(**kwargs):
#     print("Name: ", kwargs["name"])
#     print("Age: ", kwargs["age"])

# show_user(name="Ada", age= 36)
#-------------------------------------------

# def show_user(**kwargs):
#     print("Name: ", kwargs.get("name", "unknown"))
#     print("Age: ", kwargs.get("age", "unknown"))
#     print("City: ", kwargs.get("city", "unknown"))

# show_user(name="Ada", age=36)
#------------------------------------------------

# - With dictionaries can we do different things....

# def show_information(**kwargs):
#     for key, value in kwargs.items():
#         print(key, ":", value)


# show_information(
#     name="Ada", 
#     age=36,
#     city="London",
#     language = "Python"
# )

#--------------------------------------------------

# def create_user(username, **kwargs):
#     print("Username:", username)

#     for key, value in kwargs.items():
#         print(key, ":",value)

# create_user(
#     username = "ada123",
#     age = 36,
#     city = "London",
#     language = "Python"
#  )
#-------------------------------------------------------




#*******************************************************************************************************
# 11:10 Treci cas -  UNPACK Dictionary
#*******************************************************************************************************

#keys needs to mach parameter names

# def introduce(name, age, city):
#     print(name, age, city)

# person = {
#     "name":"Ada",
#     "age": 36,
#     "city": "London"
# }

# # introduce(
# #     name=person["name"]
# #     age=person["age"]
# #     city=person["city"]
# # )

# introduce(**person)    # -> introduce (name"Ada, age=36, city="London")
 


#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
#*******************************************************************************************************
# Last part of the lesson - kombine *args and **kwargs
#*******************************************************************************************************

# these function here allows to accept flexible arguments

def example(required, *args, **kwargs):
    print("Required:", required)
    print("Args:", args)
    print("Kwargs:", kwargs)


example(
    "Hello",
    10,
    20,
    30,
    name="Ada",
    active=True
)






#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

# *******************************************************************************************************