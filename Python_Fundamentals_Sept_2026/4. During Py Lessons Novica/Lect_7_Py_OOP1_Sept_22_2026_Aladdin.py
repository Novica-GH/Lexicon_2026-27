#******************************************************************************************
# Novica Ivkovic
# Cours: System Developer Python and AI
# September 22 2026 - Today's study goal is: OOP
#                     
#
#*******************************************************************************************
# Part A - Structured data
#*********************************************
#
# Pr.1

# student= {
#     "name": "Ada",
#     "score": "91",
#     "active":True
# }
#  # mozemo imati funkcije nad ovim strukturama....

#  def get_status(student):
#     if student["score"]>=70;
#       return "Pass"
# return "Fail" 
# print(get_status(student))

# # Zasto onda klase postoje?
# # Bihejvijer

# print(get_status(student))'





#******************************************************************************************
# Part B - Class and objects
#*************************************************


# class -  A Class is a definition or a blue print

# object (An object is an instance created from the clas)

# primeri imena klasa: Student, BankAcount

# class Student: 
#      pass

# student1 = Student()  # student1 is instanceo of Student

# #print(student1)
# print(type(student1))
# # <class '__main__.Student'>

# student2 = Student()

# print(student1)
# print(student2)

# print(student1 is student2)

#-----------------------------------------------------------

# adding info (atributes)  manually

# class Student:
#     pass

# student1 = Student()

# student1.name="Ada"
# student1.score=91

# # print(student1.name)
# # print(student1.score)

# # object state

# student2 = Student()

# student2 = Student()

# student2.name = "Grace"
# student2.score = 85

# print(student1.name, student1.score)
# print(student2.name, student2.score)

# student3 = Student()

# student3.name = "Alan"

# print(student3.score)

#-----------------------------------------
# Zbog problema manuelnog dodavanja atributa, Pajton ima metode: 

# __Init__  ( dva _ = __)

# class Student:
#     def __init__(self, name, score):   # self refers to the specific object we working (student1)
#         self.name = name
#         self.score = score

# student1 = Student("Ada", 91)  # When this object is created, onda je self 

# # print(student1.name)
# # print(student1.score)

# # self -> student1
# # name -> Ada
# # score -> 91

# student2 = Student("Grace", 85)

# print(student1.name)
# print(student2.name)

# ----------------------------------------------

# self.name = name

# class Student:

#     def __init__(self, name, score):
#         self.name = name        # atribute
#         self.score = score      # atribute

# class Student:

#     def __init__(self, student_name, student_score):  # paremeters
#         self.name = student_name        # atribute
#         self.score = student_score      # atribute

# student = Student("Ada", 91)

# print(student.name)
# print(student.score)
#----------------------------------------------


# class Student:

#     def __init__(self, name, score=0, active=True):
#         self.name = name        # atribute
#         self.score = score      # atribute
#         self.active = active

# student1 = Student("Ada", 91)
# student2 = Student("Bob")

# print(student1.name, student1.score, student1.active)
# print(student2.name, student2.score, student2.active)  # i ovo ce raditi dobro, povuci ce iz 1
# # sto je dobra stvar kod OOP

# Keywords arguments also works
#------------------------------

# student3 = Student(
#     name="Grace",
#     score=99,
#     active=False
# )

# print(student3.name)
# print(student3.score)
# print(student3.active)

#-----------------------------------------------
    # Mozemo dati studentima radne zadatke

# class Student:
#     def __init__(self, name, score):
#         self.name = name
#         self.score = score

#     def introduce(self):
#         print("Hello my name is", self.name)

# student1 = Student("Ada", 91)

# # student1.introduce()

# student2 = Student("Grace", 85)


# student1.introduce()
# student2.introduce()

#---------------------------------------------------
  #OBS   
# class Student:
#     def __init__(self, name, score):
#         self.name = name
#         self.score = score

#     def get_stats(self):
#         if self.score >=70:
#             return "Pass"
        
#         return "Fail"

# student1 = Student("Ada", 91)
# student2 = Student("Bob", 62)

# print(student1.get_status())
# print(student2.get_status())


#--------------------------------

# class Student:
#     def __init__(self, name, score):
#         self.name = name
#         self.score = score

#     def update_score(self, new_score):
#         if new_score(self, new_score)>100:
#             raise ValueError(
#                 "Score must be between 0 and 100"
#             )
#         self.score = new_score

# student = Student("Ada", 80)

# student.update_score(150)

# print(student.score)
# student.update_score(96)   # promena - this method -> changes the state of the object
# print(student.score)


#------------------------------

# class BankAccount: 
#     def __init__(self, owner, balance=0):
#         self.owner = owner,
#         self.balance = balance

# account = BankAccount("Ada", 1000)
# print(account.balance)

#*-------------------------------
# class BankAccount: 
#     def __init__(self, owner, balance=0):
#         self.owner = owner,
#         self.balance = balance

#     def deposit(self, amount):
#         self.balance += amount


# account = BankAccount("Ada", 1000)
# account.deposit(500)

# print(account.balance)



#************************************************************
# PART 2 10:20
#************************************************************

# istance attributes


# class Student:
#      def __init__(self, name):
#          self.name = name
         
# student1 = Student("Ada")
# student2 = Student ("Grace")

# student1.name = "Ada Lovelace" # dodatak

# print(student1.name)
# print(student2.name)



#************************************************************************************************
# PART D - Class atributes
#**********************************************************************************

# class Student:
#     school = "Lexicon"   # class atribute

#     def __init__(self, name):
#         self.name = name

# student1 = Student("Ada")
# student2 = Student("Grace")


# # print(student1.school)  # Lexicon
# # print(student2.school)  # Lexicon

# # print(Student.school) # Lexicon

# # ako probamo da promenim klass atribut  ?????

# Student.school = "AI academy"

# student1.school = "Another school"

# print(student1.school)  # AI academy
# print(student2.school)  # AI academy
# print(Student.school) # Lexicon


# Class atributes -> shared class - level data 
#  instance attributes -> data belogning to an individual object

#-------------------------------------------------------------
#Problem sa kucanjem

# class Product: 
#     tax_rate = 0.25 

#     def __init__(self, name, price):
#         self.name = name
#         self.price = price


#     def price_with_tax(self):
#         return self.price * (1 + self.tax_rate)

# product1 = Product("Keyboard", 800)
# product2 = Product("Mouse", 300)

# print(product1.price_with_tax())
# print(product2.price_with_tax())


# #******************************************************************************************************
# # Part E - While loops
# #******************************************************************************************************

# class Student:

#     def __init__(self,name, price):
#         self.name = name
#         self.score = price


#     def get_status(self):
#         if self.score >= 70:
#             return "Pass"
        
#         return "Fail"    
    
# students = [
#     Student("Anna", 85),
#     Student("Bob", 62),
#     Student("Charlie", 91)
# ]

# for student in students:
#     print(
#         student.name,
#         student.score,
#         student.get_status()
#     )

# passed_students = [
#     student 
#     for student in students 
#     if student.score >=70
# ]


# for student in passed_students:
#     print(student.name)



#*******************************************************************************************************
# Part F - 
#*******************************************************************************************************


# class Teacher:
#     def __init__(self,name):
#         self.name= name

# class Course:
#     def __init__(self, name, teacher):
#         self.name = name
#         self.teacher = teacher

# teacher = Teacher("Grace")

# course = Course(
#     "Python Foundation",
#     teacher
# )

# print(course.name)

# print(course.teacher.name)

#---------------------------
    
class Student:
    def __init__(self,name):
        self.name= name

class Course: 
    def __init__(self, name):
        self.name = name
        self.student =[]

    def add_student(self, student):
        self.student.append(student)

course = Course("Python Foundation")

student1 = Student("Ada")
student2 = Student("Grace")

course.add_student(student1)
course.add_student(student2)

for student in course.students:
    print(student.name)










#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
#*******************************************************************************************************
# Part G - Applied  challenge: Console study tracker
#*******************************************************************************************************







#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
#*******************************************************************************************************
# Part H - Stretch challenges
#*******************************************************************************************************




# *******************************************************************************************************