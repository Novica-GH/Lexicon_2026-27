#********************************************************************************************
#  Novica Ivkovic                                                                           *
#  Cours: System Developer Python and AI                                                    *
#  September 16 2026 - LAB 7                                                                *
#             Today's study goal is: OOP - Classes / objects / methods / state /instance    *
#                                          class attributes / collections of objects        *
#********************************************************************************************


#********************************************************************************************
#  LAB 7                     Part A - Classes and objects                                    *
#********************************************************************************************

# Part A.1. Create a Blok class with title, author and pages. Create at least four Book objects and print their atributes.
#------------------------------------------------------------------------------------------


# class Book:
#     def __init__(self, title, author, pages):
#         self.title = title
#         self.author = author
#         self.pages = pages

# book1 = Book("1984", "George Orwell", 300)
# book2 = Book("The Great Gatsby", "F. Scott Fitzegerald", 200)
# book3 = Book("War and peace", "Tolstoj", 1200)
# book4 = Book("Na Drini cuprija", "Ivo Andric", 500)

# books = [book1, book2, book3, book4]

# print()
# for b in books:
#     print(f"Title: {b.title:25s} | Author: {b.author:20s} | Pages: {b.pages}")
# print()




# Part A.2. Create a Laptop class with brand, model, ram_gb and price. Create three separate objects and change the price of one object.
#----------------------------------------------------------------

# class Laptop:
#     def __init__(self, brand, model, ram_gb, price):
#         self.brand = brand
#         self.model = model
#         self. ram_gb = ram_gb
#         self.price = price

# laptop1 = Laptop("Toshiba","Satelite", 4, 6000)
# laptop2 = Laptop("Lenovo","ThinkPad", 16, 8000)
# laptop3 = Laptop("HP","Spectre", 16, 10000)

# laptop2.price = 9000

# print(f"New laptop price for {laptop2.brand} {laptop2.model} is: {laptop2.price} kr" )

     


# Part A.3 Create two objects with the same attribute values. Use is to check whether they are tha same object.
#-----------------------------------------------------------------

# class Laptop:
#     def __init__(self, brand, model, ram_gb, price):
#         self.brand = brand
#         self.model = model
#         self. ram_gb = ram_gb
#         self.price = price

# laptop1 = Laptop("Lenovo","ThinkPad", 16, 8000)
# laptop2 = Laptop("Lenovo","ThinkPad", 16, 8000)

# check_object12 = laptop1 is laptop2
# print(f"laptop1 is laptop2: {check_object12}")

# # -> False -> laptop 1 and laptop 2 are two different objects!



# Part A.4  Add a default value to  at least one __int__ parameter.
#------------------------------------------------------------------


# class Laptop:
#     def __init__(self, brand, model, ram_gb=16, price=10000.0):
#         self.brand = brand
#         self.model = model
#         self. ram_gb = ram_gb
#         self.price = price


# laptop1 = Laptop("Toshiba","Satelite", 4, 6000.0)
# laptop2 = Laptop("Lenovo","ThinkPad", 8)
# laptop3 = Laptop("HP", "Spectre")

# print(f"{laptop1.brand} {laptop1.model} | RAM: {laptop1.ram_gb} GB | Price: {laptop1.price}" )
# print(f"{laptop2.brand} {laptop2.model} | RAM: {laptop2.ram_gb} GB | Price: {laptop2.price}" )
# print(f"{laptop3.brand} {laptop3.model} | RAM: {laptop3.ram_gb} GB | Price: {laptop3.price}" )




# Part A.5 Create one object using keyword arguments.
#----------------------------------------------------------------------------------------------------------------

# class Laptop:
#     def __init__(self, brand, model, ram_gb=16, price=10000.0):
#         self.brand = brand
#         self.model = model
#         self. ram_gb = ram_gb
#         self.price = price

# laptop_keyword = Laptop(
#     brand = "HP",
#     model="Spectre",
#     ram_gb=16,
#     price = 12000.0
# )

# print(f"Brand: {laptop_keyword.brand}")
# print(f"Model: {laptop_keyword.model}")
# print(f"RAM: {laptop_keyword.ram_gb} GB")
# print(f"Price: {laptop_keyword.price} kr")
        



#***********************************************************************************************
#  LAB 7               Part B - Methods and state  
#***********************************************************************************************


# Part B.1 Extend your Book class with an is_long() method that returns True if the book has more than 300 pages.
#--------------------------------------------------------------------

# class Book:
#     def __init__(self, title, author, pages):
#         self.title = title
#         self.author = author
#         self.pages = pages


#     def is_long(self):          # New method that returns True/False
#         return self.pages > 300


# book1 = Book("1984", "George Orwell", 300)
# book2 = Book("The Great Gatsby", "F. Scott Fitzegerald", 200)
# book3 = Book("War and peace", "Tolstoj", 1200)
# book4 = Book("Na Drini cuprija", "Ivo Andric", 500)

# books = [book1, book2, book3, book4]

# print()
# for b in books:
#     print(f"Title: {b.title:20s} | Author: {b.author:20s} | Pages: {b.pages:5} | Is long: {b.is_long()}")
# print()



# Part B.2  Create a BAnkAccout class with owner and balance. Add a deposit() method that changes the balance.
#----------------------------------------------------------------------------------------------------------

# class BankAccount:
#     def __init__(self, owner, balance):
#         self.owner = owner
#         self.balance = balance

#     def deposit(self, amount):
#         self.balance += amount

# account = BankAccount("Ada", 2000)

# account.deposit(700)

# print(account.balance)



# Part B.3 Add a wthdraw() method. Prevent withdrawals that would make the balance negative by raising a Value Error.
#--------------------------------------------------------------------------------------

# class BankAccount:
#     def __init__(self, owner, balance):
#         self.owner = owner
#         self.balance = balance

#     def deposit(self, amount):
#         self.balance += amount

#     def withdraw(self, amount):
#         if amount > self.balance:
#             raise ValueError("Not enough money for this withdrawal.")
#         self.balance -= amount

# account = BankAccount("Ada", 2000)

# account.deposit(700)
# print(f" Balance after deposit: {account.balance}")

# account.withdraw(6000)
# print(f" Balance after withdrawal: {account.balance}") #Warning



# Part B.4 Create a Task class with title and completed=False. Add complete() and reopen() methods.
#----------------------------------------------------------------------------------------------------

# class Task:
#     def __init__(self, title, completed=False):
#         self.title = title
#         self.completed = completed

  
#     def complete(self):   # Method 
#         self.completed = True

   
#     def reopen(self): #Method
#         self.completed = False

# task1 = Task("Finish GitHub folders and structure.")

# print(f"Task: '{task1.title}' | Completed: {task1.completed}") # False


# task1.complete()
# print(f"After 17h complete(): '{task1.title}' | Completed: {task1.completed}") # True


# task1.reopen()
# print(f"After reopen():   '{task1.title}' | Completed: {task1.completed}") # False





# Part B.5 Create at least two objects from one of your classes and show that changing the state of one object does not change the other.
#----------------------------------------------------------------------------------------------------



# class Task:
#     def __init__(self, title, completed=False):
#         self.title = title
#         self.completed = completed

#     def complete(self):
#         self.completed = True

#     def reopen(self):
#         self.completed = False



# task1 = Task("Prepare GitHub report - folders and files")  # Two objects
# task2 = Task("Commit the work file wery often during the day")

# print("--- Start Condition ---")

# print(f"Task 1: '{task1.title}' | Completed: {task1.completed}")
# print(f"Task 2: '{task2.title}' | Completed: {task2.completed}")

# task1.complete()   # Change here

# print("\n--- After changing task1 (task1.complete()) ---")

# print(f"Task 1: '{task1.title}' | Completed: {task1.completed}")
# print(f"Task 2: '{task2.title}' | Completed: {task2.completed}")





    
#****************************************************************************************************
#  LAB 7                     PART C - Instande and class attributes                                 *
#****************************************************************************************************


# C.1. Create a Product class with name and price as instance attributes.
#--------------------------------------------------------------------

# class Product:
#     def __init__(self, name, price):
#         self.name = name    
#         self.price = price  


# product1 = Product("Laptop", 10000.0)  #  Objekt - instance -  classe Product
# product2 = Product("Mouse", 250.0)


# print(f"\nProduct 1: {product1.name} | Price: {product1.price} SEK")
# print(f"Product 2: {product2.name} | Price: {product2.price} SEK\n")





# C.2 Add a class attribute caled tax_rate that is shared by all Product ojbects.
#-----------------------------------------


# class Product:
#     tax_rate = 0.25  # 25%

#     def __init__(self, name, price):
#         self.name = name   
#         self.price = price  


# product1 = Product("Laptop", 8000.0)
# product2 = Product("Mouse", 250.0)


# print(f"\nTax rate (over class): {Product.tax_rate * 100}%\n")


# print(f"{product1.name} tax rate: {product1.tax_rate * 100}%")
# print(f"{product2.name} tax rate: {product2.tax_rate * 100}%\n")




# C.3 Add a price_with_tax() method that returns the price including tax.
#------------------------------------------------------------

# class Product:
#     tax_rate = 0.25  

#     def __init__(self, name, price):
#         self.name = name    
#         self.price = price  

    
#     def price_with_tax(self):
#         return self.price * (1 + self.tax_rate)



# product1 = Product("Laptop", 8000.0)
# product2 = Product("Mouse", 300.0)


# print(f"Product: {product1.name}")
# print(f"Base price: {product1.price} kr")
# print(f"Price with tax: {product1.price_with_tax()} kr\n")

# print(f"Product: {product2.name}")
# print(f"Base price: {product2.price} kr")
# print(f"Price with tax: {product2.price_with_tax()} kr\n")




# C.4 Create at least three Product objects and print theri prices with tax.
#------------------------------------------------------------------------------------------------


# C.5 Change Product.tax_rate and show how it affects the Product objects.
#------------------------------------------------------------------------------------------------


# C.6 Give one Product object its own tax_rate. Print the tax rate from that object, another 
# Product object and the Product class.
#------------------------------------------------------------------------------------------------



#************************************************************************************************
#  LAB 7                         PART D - Collections of objects                                *
#************************************************************************************************

# D.1 Create at least six Student objects with name and score.
#-------------------------------------------------------------------------

# class Student:
#     def __init__(self, name, score):
#         self.name = name
#         self.score = score

# student1 = Student("Ada", 75)
# student2 = Student("Grace", 85)
# student3 = Student("Bob", 65)
# student4 = Student("Charlie", 95)
# student5 = Student("Sussie", 55)
# student6 = Student("Petra", 65)
# student7 = Student("Diana", 80)


# print(student1.name, student1.score)
# print(student2.name, student3.name, student4.score)
# print(student7.score, student6.score, student5.score)




# D.2 Store all Student objects in a list.
#-------------------------------------------------------

# class Student:
#     def __init__(self, name, score):
#         self.name = name
#         self.score = score


# student1 = Student("Ada", 75)
# student2 = Student("Grace", 85)
# student3 = Student("Bob", 65)
# student4 = Student("Charlie", 95)
# student5 = Student("Sussie", 55)
# student6 = Student("Petra", 65)
# student7 = Student("Diana", 80)



# students = [student1, student2, student3, student4, student5, student6, student7]

# print("\n--- List of Students ---\n")
# for s in students:
#     print(f"Name: {s.name:10s} | Score: {s.score}")
# print()


# D.3 Loop through the list and print each student's name and score.
#--------------------------------------------------------

# class Student:
#     def __init__(self, name, score):
#         self.name = name
#         self.score = score


# student1 = Student("Ada", 75)
# student2 = Student("Grace", 85)
# student3 = Student("Bob", 65)
# student4 = Student("Charlie", 95)
# student5 = Student("Sussie", 55)
# student6 = Student("Petra", 65)
# student7 = Student("Diana", 80)

# students = [student1, student2, student3, student4, student5, student6, student7]

# for student in students:
#     print(f"Student: {student.name:10s} | Score: {student.score}")



# D.4 Add a get_status() method that returns "PASS" OR "FAIL" based on the score.
#-----------------------------------------------------------------------

class Student:
    def __init__(self, name, score):
        self.name = name
        self.score = score

    
    def get_status(self):
        if self.score >= 70:
            return "PASS"
        else:
            return "FAIL"

student1 = Student("Ada", 75)
student2 = Student("Grace", 85)
student3 = Student("Bob", 65)
student4 = Student("Charlie", 95)
student5 = Student("Sussie", 55)
student6 = Student("Petra", 65)
student7 = Student("Diana", 80)

students = [student1, student2, student3, student4, student5, student6, student7]


print("\n--- Student Exam Results ---\n")
for student in students:
    print(f"Name: {student.name:10s} | Score: {student.score:2d} | Status: {student.get_status()}")
    print()





# D.5 Loop through the students again and print each student's name and status.
#-----------------------------------------------------------------


# D.6 Use a list comprehension to create a new list containing only students with a score of 70  or higher.
#-----------------------------------------------------




#******************************************************************************************************
#  LAB 7                        Part E - Objects inside objects                                       *
#******************************************************************************************************


# E.1 Create a Teacher class with a name
#--------------------------------------------------------------



# E.2 
#---------------------------------------------------------------------------




# E.3 
#-------------------------------------------



# E.4 
#-------------------------------------------------------------------------------------------------


# E.5 
#------------------------------------------------------------------------------




#*******************************************************************************************************
#  LAB 7                    Part F - Applied challenge: Course manager                                 *
#*******************************************************************************************************


# F.1 
#----------------------------------------------------------------------------------



# F.2 
#-----------------------------------------------------------------------------------------------------



# F.3 
#----------------------------------------



# F.4  
#---------------------------------------------------



# F.5 
#---------------------------------------------------------------------------------




# F.6 
#-------------------------------------------------------------




# F.7 
#--------------------------------------------



# F.8 
#----------------------------------------------------------------------------------------


# F.9 
#----------------------------------------------------------------------------------------




#*******************************************************************************************************
#  LAB 7                         Part G -  Strech challenges                                         *
#*******************************************************************************************************

# G.1 
#----------------------------------------------------------


# G.2 
#----------------------------------------------------------------------------------------


# G.3 
#----------------------------------------------------------------------------------------------------


# G.4 
#------------------------------------------------------------------------------------------------------------


# G.5 
#---------------------------------------------------------------------------------------------


# **********************************  END of LAB 6  ********************************************************