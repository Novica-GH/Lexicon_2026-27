#********************************************************************************************
#  Novica Ivkovic                                                                           *
#  Cours: System Developer Python and AI                                                    *
#  September 16 2026 - LAB 7                                                                *
#             Today's study goal is: OOP - Classes / objects / methods / state /instance    *
#                                          class attributes / collections of objects        *
#********************************************************************************************
#********************************************************************************************


#********************************************************************************************
#  LAB 7                     Part A - Classes and objects                                    *
#********************************************************************************************

# Part A.1. Create a Blok class with title, author and pages. 
#           Create at least four Book objects and print their atributes.
#-----------------------------------------------------------------------


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

# print(f"\n --- TITLE    ---             ---    AUTHOR   ---       ---   PAGES  ---\n ")
# for b in books:
#     print(f"Title: {b.title:25s} | Author: {b.author:20s} | Pages: {b.pages}")
# print()




# Part A.2. Create a Laptop class with brand, model, ram_gb and price. 
#           Create three separate objects and change the price of one object.
#----------------------------------------------------------------------------

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

# print(f"\nNew laptop price for {laptop2.brand} {laptop2.model} is: {laptop2.price} kr\n" )

     


# Part A.3 Create two objects with the same attribute values. Use is to check whether they are tha same object.
#--------------------------------------------------------------------------------------------------------------

# class Laptop:
#     def __init__(self, brand, model, ram_gb, price):
#         self.brand = brand
#         self.model = model
#         self. ram_gb = ram_gb
#         self.price = price

# laptop1 = Laptop("Lenovo","ThinkPad", 16, 8000)
# laptop2 = Laptop("Lenovo","ThinkPad", 16, 8000)

# check_object12 = laptop1 is laptop2
# print(f"\nlaptop1 is laptop2: {check_object12}\n")

# -> False -> laptop 1 and laptop 2 are two different objects!




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

# print(f"\n{laptop1.brand} {laptop1.model} | RAM: {laptop1.ram_gb} GB | Price: {laptop1.price}" )
# print(f"{laptop2.brand} {laptop2.model} | RAM: {laptop2.ram_gb} GB | Price: {laptop2.price}" )
# print(f"{laptop3.brand} {laptop3.model} | RAM: {laptop3.ram_gb} GB | Price: {laptop3.price}\n" )




# Part A.5 Create one object using keyword arguments.
#----------------------------------------------------

# class Laptop:
#     def __init__(self, brand, model, ram_gb=16, price=10000.0):
#         self.brand = brand
#         self.model = model
#         self. ram_gb = ram_gb
#         self.price = price


# laptop_keyword = Laptop(
#     brand   = "HP",
#     model   = "Spectre",
#     ram_gb  = 16,
#     price   = 12000.0
# )

# # OR: laptop_keyword = Laptop( brand = "HP", model="Spectre", ram_gb=16, price = 12000.0)

#  # Print by key
# print(f"Brand: {laptop_keyword.brand}")
# print(f"Model: {laptop_keyword.model}")
# print(f"RAM: {laptop_keyword.ram_gb} GB")
# print(f"Price: {laptop_keyword.price} kr")
        



#***********************************************************************************************
#  LAB 7               Part B - Methods and state  
#***********************************************************************************************


# Part B.1 Extend your Book class with an is_long() method that returns True if the book has more than 300 pages.
#----------------------------------------------------------------------------------------------------------------

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

# print("\n ---  TITLE   ---           |   ---   AUTHOR   ---         |  PAGES       | LONGER 300  \n")
# for b in books:
#     print(f"Title: {b.title:20s} | Author: {b.author:20s} | Pages: {b.pages:5} | Is long: {b.is_long()}")
# print()



# Part B.2  Create a BankAccout class with owner and balance. Add a deposit() method that changes the balance.
#----------------------------------------------------------------------------------------------------------

# class BankAccount:
#     def __init__(self, owner, balance):
#         self.owner = owner
#         self.balance = balance

#     def deposit(self, amount):
#         self.balance += amount

# account = BankAccount("Ada", 2000)

# account.deposit(700)

# print(f"\n {account.owner} has {account.balance} kr on account.\n")




# Part B.3 Add a wthdraw() method. Prevent withdrawals that would make the balance negative by raising a Value Error.
#--------------------------------------------------------------------------------------------------------------------

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
# print(f"\n Balance after deposit: {account.balance}")

# account.withdraw(6000)
# print(f" Balance after withdrawal: {account.balance}\n") #Warning the withdraw amount is larger then balance!



# Part B.4 Create a Task class with title and completed=False. Add complete() and reopen() methods.
#-------------------------------------------------------------------------------------------------

# class Task:
#     def __init__(self, title, completed=False):
#         self.title = title
#         self.completed = completed

  
#     def complete(self):   # Method 
#         self.completed = True

   
#     def reopen(self): #Method
#         self.completed = False

# task1 = Task("Finish GitHub folders and structure.")

# print(f"\nTask: '{task1.title}' | Completed: {task1.completed}") # False


# task1.complete()
# print(f"After 17h complete(): '{task1.title}' | Completed: {task1.completed}") # True


# task1.reopen()
# print(f"After reopen():   '{task1.title}' | Completed: {task1.completed}\n") # False





# Part B.5 Create at least two objects from one of your classes and show that changing the state 
#            of one object does not change the other.
#------------------------------------------------------------------------------------------------



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

# print("\n                 --- Start Condition ---")

# print(f"Task 1: '{task1.title}' | Completed: {task1.completed}")
# print(f"Task 2: '{task2.title}' | Completed: {task2.completed}")

# task1.complete()   # Change here

# print("\n           --- After changing task1 (task1.complete()) ---")

# print(f"Task 1: '{task1.title}' | Completed: {task1.completed}")
# print(f"Task 2: '{task2.title}' | Completed: {task2.completed}")





    
#****************************************************************************************************
#  LAB 7                     PART C - Instande and class attributes                                 *
#****************************************************************************************************


# C.1. Create a Product class with name and price as instance attributes.
#------------------------------------------------------------------------

# class Product:
#     def __init__(self, name, price):
#         self.name = name    
#         self.price = price  


# product1 = Product("Laptop", 10000.0)  #  Objekt - instance -  classe Product
# product2 = Product("Mouse", 250.0)


# print(f"\nProduct 1: {product1.name} | Price: {product1.price} SEK")
# print(f"Product 2: {product2.name}  | Price:   {product2.price} SEK\n")





# C.2 Add a class attribute caled tax_rate that is shared by all Product ojbects.
#--------------------------------------------------------------------------------


# class Product:
#     tax_rate = 0.25  # 25%

#     def __init__(self, name, price):
#         self.name = name   
#         self.price = price  


# product1 = Product("Laptop", 8000.0)
# product2 = Product("Mouse", 250.0)


# print(f"\nTax rate (over class): {Product.tax_rate * 100}%\n") # Read tax_rate direct from the class


# print(f"{product1.name} tax rate: {product1.tax_rate * 100}%")      # Read tax_rate from one object.
# print(f"{product2.name} tax rate: {product2.tax_rate * 100}%\n")    # Read tax_rate from another object.




# C.3 Add a price_with_tax() method that returns the price including tax.
#------------------------------------------------------------------------

# class Product:
#     tax_rate = 0.25  

#     def __init__(self, name, price):
#         self.name = name    
#         self.price = price  

    
#     def price_with_tax(self):
#         return self.price * (1 + self.tax_rate)



# product1 = Product("Laptop", 8000.0)
# product2 = Product("Mouse", 300.0)


# print(f"\nProduct: {product1.name}")
# print(f"Base price: {product1.price} kr")
# print(f"Price with tax: {product1.price_with_tax()} kr\n")

# print(f"Product: {product2.name}")
# print(f"Base price: {product2.price} kr")
# print(f"Price with tax: {product2.price_with_tax()} kr\n")




# C.4 Create at least three Product objects and print theri prices with tax.
#---------------------------------------------------------------------------

# class Product:
#     tax_rate = 0.25  # Klasni atribut za pdv (25%)

#     def __init__(self, name, price):
#         self.name = name    
#         self.price = price  

#     def price_with_tax(self):
#         return self.price * (1 + self.tax_rate)



# product1 = Product("Laptop", 8000.0)
# product2 = Product("Mouse", 300.0)
# product3 = Product("Keyboard", 500.0)


# products = [product1, product2, product3]

# print("\n --- PRODUCTS INFO  ---")

# for p in products:
#     print(f"\nProduct: {p.name}")
#     print(f"Base price: {p.price:.2f} kr")
#     print(f"Price with tax: {p.price_with_tax():.2f} kr\n")





# C.5 Change Product.tax_rate and show how it affects the Product objects.
#-------------------------------------------------------------------------

# class Product:
#     tax_rate = 0.25     # Start tax rate

#     def __init__(self, name, price):
#         self.name = name
#         self.price = price

#     def price_with_tax(self):
#         return self.price * (1 + self.tax_rate)


# product1 = Product("Laptop", 8000.0)
# product2 = Product("Mouse", 300.0)
# product3 = Product("Keyboard", 500.0)

# print("\n--- Before change (tax_rate = 0.25) ---\n")
# print(f"{product1.name}: {product1.price_with_tax():.2f} kr")
# print(f"{product2.name}: {product2.price_with_tax():.2f} kr")
# print(f"{product3.name}: {product3.price_with_tax():.2f} kr")


# Product.tax_rate = 0.20   # Changing tax rate

# print("\n--- After change - Product.tax_rate = 0.20 ---\n")
# print(f"{product1.name}: {product1.price_with_tax():.2f} kr")
# print(f"{product2.name}: {product2.price_with_tax():.2f} kr")
# print(f"{product3.name}: {product3.price_with_tax():.2f} kr\n")




# C.6 Give one Product object its own tax_rate. Print the tax rate from that object, 
#     another Product object and the Product class.
#------------------------------------------------------------------------------------

# class Product:
#     tax_rate = 0.20  # Start tax rate - Class atribute

#     def __init__(self, name, price):
#         self.name = name
#         self.price = price



# product1 = Product("Laptop", 8000.0)
# product2 = Product("Mouse", 300.0)


# product1.tax_rate = 0.10   # special tax rate, just för this object


# print(f"\nproduct1 ({product1.name}) tax rate: {product1.tax_rate}")  # 0.10  - Separate defined (individual) atribut
# print(f"product2 ({product2.name}) tax rate: {product2.tax_rate}")    # 0.20  - Object takes tax_rate from the class Product
# print(f"Product class tax rate:              {Product.tax_rate}")     # 0.20  - Product class atribut




#************************************************************************************************
#  LAB 7                         PART D - Collections of objects                                *
#************************************************************************************************

# D.1 Create at least six Student objects with name and score.
#-------------------------------------------------------------

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
# print(student2.name, student3.name, student4.score)     # :) 
# print(student7.score, student6.score, student5.score)   # :) :) :)




# D.2 Store all Student objects in a list.
#-----------------------------------------

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
#--------------------------------------------------------------------

# class Student:
#     def __init__(self, name, score):
#         self.name = name
#         self.score = score

# print("\n--- List of Students/score ---\n")

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
# print()





# D.4 Add a get_status() method that returns "PASS" OR "FAIL" based on the score.
#--------------------------------------------------------------------------------

# class Student:
#     def __init__(self, name, score):
#         self.name = name
#         self.score = score

    
#     def get_status(self):
#         if self.score >= 70:
#             return "PASS"
#         else:
#             return "FAIL"

# student1 = Student("Ada", 75)
# student2 = Student("Grace", 85)
# student3 = Student("Bob", 65)
# student4 = Student("Charlie", 95)
# student5 = Student("Sussie", 55)
# student6 = Student("Petra", 65)
# student7 = Student("Diana", 80)

# students = [student1, student2, student3, student4, student5, student6, student7]


# print("\n        --- Student Exam Results ---\n")

# for student in students:
#     print(f"Name: {student.name:10s} | Score: {student.score:2d} | Status: {student.get_status()}")
# print()





# D.5 Loop through the students again and print each student's name and status.
#------------------------------------------------------------------------------

# class Student:
#     def __init__(self, name, score):
#         self.name = name
#         self.score = score

#     def get_status(self):
#         if self.score >= 70:
#             return "PASS"
#         else:
#             return "FAIL"

# student1 = Student("Ada", 75)
# student2 = Student("Grace", 85)
# student3 = Student("Bob", 65)
# student4 = Student("Charlie", 95)
# student5 = Student("Sussie", 55)
# student6 = Student("Petra", 65)
# student7 = Student("Diana", 80)

# students = [student1, student2, student3, student4, student5, student6, student7]

# print("\n       --- Students Exam Results ---\n")

# for student in students:
#     print(f"Name: {student.name:10s} | Score: {student.score:2d} | Status: {student.get_status()}")


# print("\n   --- Student / Status ---\n")

# for student in students:
#     print(f"Name: {student.name:10s} | Status: {student.get_status()}")
# print()




# D.6 Use a list comprehension to create a new list containing only students with a score of 70  or higher.
#-----------------------------------------------------------------------------------------------------------

# class Student:
#     def __init__(self, name, score):
#         self.name = name
#         self.score = score

#     def get_status(self):
#         if self.score >= 70:
#             return "PASS"
#         else:
#             return "FAIL"

# student1 = Student("Ada", 75)
# student2 = Student("Grace", 85)
# student3 = Student("Bob", 65)
# student4 = Student("Charlie", 95)
# student5 = Student("Sussie", 55)
# student6 = Student("Petra", 65)
# student7 = Student("Diana", 80)


# students = [student1, student2, student3, student4, student5, student6, student7]

# passed_students = [student for student in students if student.score >= 70]


# print("\n --- Students with score 70 or higher ---\n")

# for student in passed_students:
#     print(f"Name: {student.name:10s} | Score: {student.score}")

# print()



#******************************************************************************************************
#  LAB 7                        Part E - Objects inside objects                                       *
#******************************************************************************************************


# E.1 Create a Teacher class with a name
#---------------------------------------


# class Teacher:
#     def __init__(self, name):
#         self.name = name


# teacher1 = Teacher("Prof. Donatello ")

# print(f"\nTeacher name: {teacher1.name}\n")


# E.2 Create a Course class with a course name and a teacher. The teacher should be a Teacher object.
#----------------------------------------------------------------------------------------------------

# class Teacher:
#     def __init__(self, name):
#         self.name = name

# class Course:
#     def __init__(self, course_name, teacher):
#         self.course_name = course_name
#         self.teacher = teacher                     # The teacher should be a Teacher object.


# teacher1 = Teacher("Prof. Donatello")
# course1 = Course("Python Programming", teacher1)  # The teacher should be a Teacher object.


# print(f"\nCourse name: {course1.course_name}")      #  Classic way
# print(f"Teacher name: {course1.teacher.name}\n")    #  Objects inside objects    





# E.3 Create a Teacher object and use it when creating a Course object
#---------------------------------------------------------------------

# class Teacher:
#     def __init__(self, name):
#         self.name = name


# class Course:
#     def __init__(self, course_name, teacher):
#         self.course_name = course_name
#         self.teacher = teacher           #  The same like in E.2



# teacher1 = Teacher("Prof. Donatello")

# course1 = Course("Python Programming", teacher1)




# E.4 Print the course name and the teacher's name through the Course object
#----------------------------------------------------------------------------

# class Teacher:
#     def __init__(self, name):
#         self.name = name

# class Course:
#     def __init__(self, course_name, teacher):
#         self.course_name = course_name
#         self.teacher = teacher                     # The teacher should be a Teacher object.


# teacher1 = Teacher("Prof. Donatello")
# course1 = Course("Python Programming", teacher1)  # The teacher should be a Teacher object.


# print(f"\nCourse name: {course1.course_name}")      #  Classic way
# print(f"Teacher name: {course1.teacher.name}\n")    #  Objects inside objects  





# E.5 Extend Course so that is also contains an initially empty list of Student objects.
#---------------------------------------------------------------------------------------

# class Teacher:
#     def __init__(self, name):
#         self.name = name


# class Student:
#     def __init__(self, name, score):
#         self.name = name
#         self.score = score


# class Course:
#     def __init__(self, course_name, teacher):
#         self.course_name = course_name
#         self.teacher = teacher
        
#         self.students = []  # an initially empty list of Student objects



# teacher1 = Teacher("Prof. Donatello")               # object teacher1
# course1 = Course("Python Programming", teacher1)    # object course1

# print(f"Course: {course1.course_name}")
# print(f"Teacher: {course1.teacher.name}")
# print(f"Initial students list: {course1.students}")  # Print empty list of Student objects





# E.6 Add an add_student() method and use it to add at least three Student objects to the course.
# #-----------------------------------------------------------------------------------------------

# class Teacher:
#     def __init__(self, name):
#         self.name = name


# class Student:
#     def __init__(self, name, score):
#         self.name = name
#         self.score = score


# class Course:
#     def __init__(self, course_name, teacher):
#         self.course_name = course_name
#         self.teacher = teacher
#         self.students = []  

#     def add_student(self, student):
#         self.students.append(student)



# teacher1 = Teacher("Prof. Donatello")
# course1 = Course("Python Programming", teacher1)


# student1 = Student("Ada", 85)       # 3 students objects
# student2 = Student("Nada", 95)
# student3 = Student("Senada", 78)


# course1.add_student(student1)       # We use method add_student to add student1 to the cours.
# course1.add_student(student2)       # The same for student2
# course1.add_student(student3)       # ...and for student3

#     # test
# print(f"\nCourse: {course1.course_name}")
# print(f"Teacher: {course1.teacher.name}")
# print("Added Students:")
# for s in course1.students:
#     print(f"- {s.name} (Score: {s.score})")
# print()





# E.7 Loop through course.students and print the name of every student.
#----------------------------------------------------------------------

# class Teacher:
#     def __init__(self, name):
#         self.name = name


# class Student:
#     def __init__(self, name, score):
#         self.name = name
#         self.score = score


# class Course:
#     def __init__(self, course_name, teacher):
#         self.course_name = course_name
#         self.teacher = teacher
#         self.students = []

#     def add_student(self, student):
#         self.students.append(student)


# teacher1 = Teacher("Prof. Donatello")
# course1 = Course("Python Programming", teacher1)

# course1.add_student(Student("Ada", 85))
# course1.add_student(Student("Nada", 95))
# course1.add_student(Student("Senada", 78))


# print(f"\nCourse: {course1.course_name}")
# print(f"Teacher: {course1.teacher.name}")
# print("Students:")

# for student in course1.students:
#     print(student.name)
# print()





#*******************************************************************************************************
#  LAB 7                    Part F - Applied challenge: Course manager                                 *
#*******************************************************************************************************




# F.1 Build a small course management program using Student, Teacher an Course classes.
#---------------------------------------------------------------------------------------

# class Teacher:
#     def __init__(self, name):
#         self.name = name


# class Student:
#     def __init__(self, name):
#         self.name = name  


# class Course:
#     def __init__(self, course_name, teacher):
#         self.course_name = course_name
#         self.teacher = teacher
#         self.students = []

#     def add_student(self, student):
#         self.students.append(student)


#     def display_course_info(self):
#         print("*" * 32)
#         print(f"COURSE:  {self.course_name}")
#         print(f"TEACHER: {self.teacher.name}")
#         print("-" * 32)
#         print("STUDENTS:")
#         if not self.students:
#             print("  (No students on the course)")
#         else:
#             for student in self.students:
#                 print(f" • {student.name:<15}")
#             print("-" * 30)            
#         print("*" * 32 + "\n")

#  # end of 3 class definition


#  # def 2 objects - class Teacher
# teacher_python = Teacher("Prof. Donatello")
# teacher_math = Teacher("Dr Gaus")

#  # def 2 objects - class Course
# python_course = Course("Python OOP Fundamentals", teacher_python)
# math_course = Course("" \
# "Komplex Mathematics", teacher_math)

#  # def 4 objects - class Student
# s1 = Student("Ada")
# s2 = Student("Senada")
# s3 = Student("Nada")
# s4 = Student("Rada")

#  # schedule of students by courses (py and math)
# python_course.add_student(s1)
# python_course.add_student(s2)
# python_course.add_student(s3)

# math_course.add_student(s1)
# math_course.add_student(s4)


#  # test - printing reports by courses
# print()
# python_course.display_course_info()
# math_course.display_course_info()





# # F.2 Student should contain at least name and score.
# #-----------------------------------------------------

# class Teacher:
#     def __init__(self, name):
#         self.name = name


# class Student:
#     def __init__(self, name, score):
#         self.name = name
#         self.score = score


# class Course:
#     def __init__(self, course_name, teacher):
#         self.course_name = course_name
#         self.teacher = teacher
#         self.students = []

#     def add_student(self, student):
#         self.students.append(student)


#     def display_course_info(self):
#         print("*" * 40)
#         print(f" COURSE:  {self.course_name}")
#         print(f" TEACHER: {self.teacher.name}")
#         print("-" * 40)
#         print("  STUDENTS:         SCORE:")
#         if not self.students:
#             print("  (No students on the course)")
#         else:
#             for student in self.students:
#                 print(f"  • {student.name:<15} Score: {student.score}")
#             print("-" * 40)
#         print("*" * 50 + "\n")

#  # end of 3 class definition


#  # def 2 objects - class Teacher
# teacher_python = Teacher("Prof. Donatello")
# teacher_math = Teacher("Dr Gaus")


#  # def 2 objects - class Course
# python_course = Course("Python OOP Fundamentals", teacher_python)
# math_course = Course("Komplex Mathematics", teacher_math)


#  # def 4 objects - class Student
# s1 = Student("Ada", 85)
# s2 = Student("Senada", 65)
# s3 = Student("Nada", 95)
# s4 = Student("Rada", 78)


#  # schedule of students by courses (py and math)
# python_course.add_student(s1)
# python_course.add_student(s2)
# python_course.add_student(s3)

# math_course.add_student(s1)
# math_course.add_student(s4)

#  # test - printing reports by courses
# print()
# python_course.display_course_info()
# math_course.display_course_info()





# F.3 Student should have a method that returns "PASS" or "FAIL".
#-----------------------------------------------------------------

# class Teacher:
#     def __init__(self, name):
#         self.name = name


# class Student:
#     def __init__(self, name, score):
#         self.name = name
#         self.score = score

#     def get_status(self, passing_score=70):
#         # a method that returns "PASS" or "FAIL"
#         if self.score >= passing_score:
#             return "PASS"
#         else:
#             return "FAIL"


# class Course:
#     def __init__(self, course_name, teacher):
#         self.course_name = course_name
#         self.teacher = teacher
#         self.students = []

#     def add_student(self, student):
#         self.students.append(student)


#     def display_course_info(self):
#         print("*" * 50)
#         print(f"        COURSE:  {self.course_name}")
#         print(f"        TEACHER: {self.teacher.name}")
#         print("-" * 50)
#         print(" STUDENTS:        SCORE:         PASS/FAIL:")
#         if not self.students:
#             print("  (No students on the course)")
#         else:
#             for student in self.students:
#                 print(f" • {student.name:<15} Score: {student.score:<9} {student.get_status()}")
#             print("-" * 50)
#         print("*" * 50 + "\n")

#  #end of 3 class definition


#  # def 2 objects - class Teacher
# teacher_python = Teacher("Prof. Donatello")
# teacher_math = Teacher("Dr Gaus")

#  # def 2 objects - class Course
# python_course = Course("Python OOP Fundamentals", teacher_python)
# math_course = Course("Komplex Mathematics", teacher_math)

#  # def 5 objects - class Student
# s1 = Student("Ada", 85)
# s2 = Student("Senada", 65)
# s3 = Student("Nada", 95)
# s4 = Student("Rada", 78)
# s5 = Student("Serenada", 72)

#  # schedule of students by courses (py and math)
# python_course.add_student(s1)
# python_course.add_student(s2)
# python_course.add_student(s3)

# math_course.add_student(s1)
# math_course.add_student(s4)
# math_course.add_student(s5)

#  # test - printing reports by courses
# python_course.display_course_info()
# math_course.display_course_info()





# F.4  Teacher should contain at least a name.
#---------------------------------------------------

# class Teacher:
#     def __init__(self, name):
#         self.name = name





# F.5 Course should contain a name, a Teacher object and a list of Student objects.
#---------------------------------------------------------------------------------

# class Teacher:
#     def __init__(self, name):
#         self.name = name


# class Student:
#     def __init__(self, name, score):
#         self.name = name
#         self.score = score

#     def get_status(self, passing_score=70):
#         # a method that returns "PASS" or "FAIL"
#         if self.score >= passing_score:
#             return "PASS"
#         else:
#             return "FAIL"

# class Course:
#     def __init__(self, course_name, teacher):
#         self.course_name = course_name
#         self.teacher = teacher
#         self.students = []

#     def add_student(self, student):
#         self.students.append(student)

#  #end of 3 class definition


#  # def 1 object - class Teacher
# teacher_python = Teacher("Prof. Donatello")

#  # def 1 object - class Course
# python_course = Course("Python OOP Fundamentals", teacher_python)

#   # def list of students - 2 students:
# python_course.add_student(Student("Ada", 85))
# python_course.add_student(Student("Bob", 65))

#  # print test:
# print("*" * 32)
# print(f"COURSE: {python_course.course_name}")
# print(f"TEACHER: {python_course.teacher.name}")
# print("STUDENTS:")

# for s in python_course.students:
#     print(f" - {s.name} (Score: {s.score}, Status: {s.get_status()})")
# print("*" * 32)



# F.6 Add methods for adding a student and showing how many students are currently in the course.
#--------------------------------------------------------------------------------------------------

# class Teacher:
#     def __init__(self, name):
#         self.name = name

# class Student:
#     def __init__(self, name, score):
#         self.name = name
#         self.score = score

#     def get_status(self):
#         return "PASS" if self.score >= 70 else "FAIL"


# class Course:
#     def __init__(self, course_name, teacher):
#         self.course_name = course_name
#         self.teacher = teacher
#         self.students = []

#     # - Add method for adding a student:
#     def add_student(self, student):
#         self.students.append(student)

#     # - Add method for showing how many students are currently in the course
#     def get_student_count(self):
#         return len(self.students)

#     def show_student_count(self):
#         print(f"\nTotal students in '{self.course_name}: {self.get_student_count()}\n")

# # end of class definition

# teacher = Teacher("Prof. Donatello")
# course = Course("Python OOP Fundamentals", teacher)

# # Adding students:
# course.add_student(Student("Ada", 85))
# course.add_student(Student("Bob", 92))
# course.add_student(Student("Grace",75))

# course.show_student_count()


# F.7 Add a mehod that returns a list containing only the students who passed.
#------------------------------------------------------------------------------

# class Teacher:
#     def __init__(self, name):
#         self.name = name


# class Student:
#     def __init__(self, name, score):
#         self.name = name
#         self.score = score

#     def get_status(self):
#         return "PASS" if self.score >= 70 else "FAIL"


# class Course:
#     def __init__(self, course_name, teacher):
#         self.course_name = course_name
#         self.teacher = teacher
#         self.students = []

#     def add_student(self, student):
#         self.students.append(student)

#     def get_student_count(self):
#         return len(self.students)

#     # Add a mehod that returns a list containing only the students who passed
#     def get_passing_students(self):
#         return [student for student in self.students if student.get_status() == "PASS"]  # list




# teacher = Teacher("Prof. Donatello")
# course = Course("Python OOP Fundamentals", teacher)

# course.add_student(Student("Ada", 85))
# course.add_student(Student("Nada", 92))  
# course.add_student(Student("Bob", 62))
# course.add_student(Student("Charlie", 68))  


# passing_students = course.get_passing_students()

# print(f"\nTotal students: {course.get_student_count()}")
# print(f"Students who passed ({len(passing_students)}):")

# for student in passing_students:
#     print(f"- {student.name}: {student.score} points")
# print()
    



# F.8 Add validation somewhere in your program using ValueError. Chose a validation that makes sense.
#----------------------------------------------------------------------------------------

# class Teacher:
#     def __init__(self, name):
#         self.name = name


# class Student:
#     def __init__(self, name, score):
#         self.name = name
        
#         # Adding validation here: Check score for students in range [0, 100]
#         if not isinstance(score, (int, float)):
#             raise ValueError("Score must be a number (int or float).")
        
#         if score < 0 or score > 100:
#             raise ValueError(f"Invalid score ({score}). Score must be between 0 and 100.") # ValueError
            
#         self.score = score

#     def get_status(self):
#         return "PASS" if self.score >= 50 else "FAIL"


# class Course:
#     def __init__(self, course_name, teacher):
#         self.course_name = course_name
#         self.teacher = teacher
#         self.students = []

#     def add_student(self, student):
#         self.students.append(student)

#     def get_passing_students(self):
#         return [student for student in self.students if student.get_status() == "PASS"]

#  # end of a part with classes definition

# teacher = Teacher("Prof. Donatello")
# course = Course("Python Fundamentals", teacher)

# print()
# # Using try/except -  for OK input
# try:
#     s1 = Student("Ada", 85)
#     course.add_student(s1)
#     print(f"Successfully added: {s1.name}")
# except ValueError as err:
#     print(f"Error creating student: {err}")

# # Using try/except -  for BAD input ->  Value Error
# try:
#     s2 = Student("Bob", -15)
#     course.add_student(s2)
# except ValueError as err:
#     print(f"Error caught: {err}")

# # BAD input for Score över 100 -> ValueError
# try:
#     s3 = Student("Anna", 105)
#     course.add_student(s3)
# except ValueError as e:
#     print(f"Error caught: {e}")
# print()





# F.9 Create at least five Student objects, one Teacher object and one Course object. 
#              Demonstrate that your methods work.
#--------------------------------------------------------------------------------------

# class Teacher:
#     def __init__(self, name):
#         self.name = name


# class Student:
#     def __init__(self, name, score):
#         self.name = name
#         self.score = score


# class Course:
#     def __init__(self, course_name, teacher):
#         self.course_name = course_name
#         self.teacher = teacher
#         self.students = []

#     def add_student(self, student):
#         self.students.append(student)

#     def calculate_average_score(self):
#         if not self.students:
#             return 0.0
#         total_score = sum(student.score for student in self.students)
#         return total_score / len(self.students)

#     def display_course_info(self):
#         print("*" * 50)
#         print(f"        COURSE:  {self.course_name}")
#         print(f"        TEACHER: {self.teacher.name}")
#         print("-" * 50)
#         print("             ADDED STUDENTS:")
#         if not self.students:
#             print("  (No students on the course)")
#         else:
#             for student in self.students:
#                 print(f"        • {student.name:<15} Score: {student.score}")
#             print("-" * 50)
#             avg = self.calculate_average_score()
#             print(f"        Average Class Score: {avg:.2f}")
#         print("*" * 50 + "\n")

#  # end of 3 class definition


#  # def 1 object - class Teacher
# teacher_python = Teacher("Prof. Donatello")

#  # def 1 object1 - class Course
# python_course = Course("Python OOP Fundamentals", teacher_python)

#  # def 5 objects - class Student
# s1 = Student("Ada", 85)
# s2 = Student("Nada", 95)
# s3 = Student("Rada", 78)
# s4 = Student("Senada", 65)
# s5 = Student("Serenada", 72)

#  # Adding students in a cours
# python_course.add_student(s1)
# python_course.add_student(s2)
# python_course.add_student(s3)
# python_course.add_student(s4)
# python_course.add_student(s5)

#  # test - printing reports by courses
# print()
# python_course.display_course_info()





# F.10. Print a simple course summary containing the course name, teacher name, number of students 
# and the names of the students who passed.
#---------------------------------------------------------------------------------------------------


# class Teacher:
#     def __init__(self, name):
#         self.name = name

# class Student:
#     def __init__(self, name, score):
#         self.name = name
        
#         if not isinstance(score, (int, float)):
#             raise ValueError("Score must be a number.")
#         if score < 0 or score > 100:
#             raise ValueError(f"Invalid score ({score}). Must be between 0 and 100.")
            
#         self.score = score

#     def get_status(self):
#         return "PASS" if self.score >= 70 else "FAIL"

# class Course:
#     def __init__(self, course_name, teacher):
#         self.course_name = course_name
#         self.teacher = teacher
#         self.students = []

#     def add_student(self, student):
#         self.students.append(student)

#     def get_student_count(self):
#         return len(self.students)

#     def get_passing_students(self):
#         return [s for s in self.students if s.get_status() == "PASS"]

#     def print_summary(self):
#         passing_students = self.get_passing_students()

#         print("*" * 35)
#         print(f"Course Name: {self.course_name}")
#         print(f"Teacher Name: {self.teacher.name}")
#         print(f"Total Students: {self.get_student_count()}")
#         print("-" * 35)
#         print("Passing Students:")
        
#         if not passing_students:
#             print("  None")
#         else:
#             for student in passing_students:
#                 print(f"  • {student.name} ({student.score} pts)")
#         print("*" * 35)

# # end of classes definition 


# teacher = Teacher("Prof. Donatello")
# course = Course("Python Fundamentals", teacher)

# # Adding students
# course.add_student(Student("Ada", 85))
# course.add_student(Student("Ava", 62))  # FAIL
# course.add_student(Student("Anna", 92))
# course.add_student(Student("Mila", 58)) # FAIL
# course.add_student(Student("Emil", 99))

# course.print_summary()





#-----F11 - My extra: Two teachers - two courses - 5 students  ---------------------------------------

# class Teacher:
#     def __init__(self, name):
#         self.name = name


# class Student:
#     def __init__(self, name, score):
#         self.name = name
#         self.score = score


# class Course:
#     def __init__(self, course_name, teacher):
#         self.course_name = course_name
#         self.teacher = teacher
#         self.students = []

#     def add_student(self, student):
#         self.students.append(student)

#     def calculate_average_score(self):
#         if not self.students:
#             return 0.0
#         total_score = sum(student.score for student in self.students)
#         return total_score / len(self.students)

#     def display_course_info(self):
#         print("*" * 50)
#         print(f"        COURSE:  {self.course_name}")
#         print(f"        TEACHER: {self.teacher.name}")
#         print("-" * 50)
#         print("             ADDED STUDENTS:")
#         if not self.students:
#             print("  (No students on the course)")
#         else:
#             for student in self.students:
#                 print(f"        • {student.name:<15} Score: {student.score}")
#             print("-" * 50)
#             avg = self.calculate_average_score()
#             print(f"        Average Class Score: {avg:.2f}")
#         print("*" * 50 + "\n")

#  # end of 3 class definition

#  # def 2 objects - class Teacher
# teacher_python = Teacher("Prof. Donatello")
# teacher_math = Teacher("Dr Gaus")


#  # def 2 objects - class Course
# python_course = Course("Python OOP Fundamentals", teacher_python)
# math_course = Course("Komplex Mathematics", teacher_math)

#  # def 5 objects - class Student
# s1 = Student("Ada", 85)
# s2 = Student("Senada", 65)
# s3 = Student("Nada", 95)
# s4 = Student("Rada", 78)
# s5 = Student("Serenada", 72)

#  # schedule of students by courses (py and math)
# python_course.add_student(s1)
# python_course.add_student(s2)
# python_course.add_student(s3)

# math_course.add_student(s1)
# math_course.add_student(s4)
# math_course.add_student(s5)

#  # test - printing reports by courses
# python_course.display_course_info()
# math_course.display_course_info()







#*******************************************************************************************************
#  LAB 7                         Part G -  Strech challenges                                         *
#*******************************************************************************************************


# G.1 Add a method that updates a student's score with validation.
#----------------------------------------------------------


# G.2 Add a method to Course that finds students above a score threshold.
#----------------------------------------------------------------------------------------


# G.3 Create another Course object and show that its student list is separate from the first course.
#----------------------------------------------------------------------------------------------------


# G.4 Add one useful class attribute to Student, Teacher or Course and explain in a comment why it belongs to the class tather than an individual object.
#------------------------------------------------------------------------------------------------------------


# G.5 
#---------------------------------------------------------------------------------------------


# **********************************  END of LAB 7  ********************************************************