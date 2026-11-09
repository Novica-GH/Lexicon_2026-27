# ==================================================
# ALADINOVA PREDAVANJA OD 2026-09-22
# ==================================================


# student = {
#     "name" : "Ada",
#     "score": "91",
#     "active": True
# }

# # print(student)


# def get_status(student):
#     if student["score"] >= 70:
#         return "Pass"

#     return "Fail"

# print(get_status(student))

#------------------------------------------


# class (blueprint)
# object (instance created from the class)




#---------------------------------------


# class Student:
#     pass



# student1 = Student()

# # print(student1)
# # print(type(student1))


# student2 = Student()


# print(student1)
# print(student2)


# print(student1 is student2)


#---------------------------------------

# adding info manually
#-------------------------------

# class Student:
#     pass


# student1 = Student()

# student1.name = "Ada"    # atributi
# student1.score = 91


# # print(student1.name)
# # print(student1.score)

# # object state

# student2 = Student()

# student2.name = "Grace"
# student2.score = 85


# print(student1.name, student1.score)
# print(student2.name, student2.score)



# student3 = Student()

# student3.name = "Alan"

# print(student3.score)  # Problem, jer score nije definisano za studenta 3 (rucno)



#---------------------------------------


# __init__   # Specijalna ugrađena metoda u Pythonu. - initialize (inicijalizovati / podesiti na početne vrednosti).



class Student:
    def __init__(self, name, score):
        self.name = name
        self.score = score


# student1 = Student("Ada", 91)

# # print(student1.name)
# # print(student1.score)


# # self -> student1
# # name -> Ada
# # score -> 91

# student2 = Student("Grace", 85)


# print(student1.name)
# print(student2.name)


#---------------------------------------
# Parameters vs attributes

# self.name = name


# class Student:

#     def __init__(self, student_name, student_score):
#         self.name = student_name
#         self.score = student_score


# student = Student("Ada", 91)

# print(student.name)
# print(student.score)


#---------------------------------------


# class Student:
#     def __init__(self, name, score=0, active=True):
#         self.name = name
#         self.score = score
#         self.active = active


# student1 = Student("Ada", 91)
# student2 = Student("Bob")

# # print(student1.name, student1.score, student1.active)
# # print(student2.name, student2.score, student2.active)


# # Keyword arguments

# student3 = Student(
#     name="Grace",
#     score=88,
#     active=False
# )

# print(student3.name)
# print(student3.score)
# print(student3.active)


#---------------------------------------


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



#---------------------------------------


# class Student:
#     def __init__(self, name, score):
#         self.name = name
#         self.score = score

#     def get_status(self):
#         if self.score >= 70:
#             return "Pass"

#         return "Fail"


# student1 = Student("Ada", 91)
# student2 = Student("Bob", 62)


# print(student1.get_status())
# print(student2.get_status())


# #---------------------------------------


# class Student:
#     def __init__(self, name, score):
#         self.name = name
#         self.score = score

#     def update_score(self, new_score):
#         self.score = new_score


# student = Student("Ada", 80)

# print(student.score)

# student.update_score(95)  # this method changes the state of the object

# print(student.score)




#---------------------------------------

# Validation

# class Student:
#     def __init__(self, name, score):
#         self.name = name
#         self.score = score

#     def update_score(self, new_score):
#         if new_score < 0 or new_score > 100:
#             raise ValueError(
#                 "Score must be between 0 and 100"
#             )
#         self.score = new_score


# student = Student("Ada", 80)


# student.update_score(150)  

# print(student.score)


#---------------------------------------


# class BankAccount:
#     def __init__(self, owner, balance=0):
#         self.owner = owner
#         self.balance = balance

#     def deposit(self, amount):
#         self.balance += amount

# account = BankAccount("Ada", 1000)

# account.deposit(500)

# print(account.balance)



#---------------------------------------

# instance attributes


# class Student:
#     def __init__(self, name):
#         self.name = name

# student1 = Student("Ada")
# student2 = Student("Grace")


# student1.name = "Ada Lovelace"

# print(student1.name)
# print(student2.name)

#---------------------------------------

# # class attributes

# class Student:

#     school = "Lexicon"      #class attribute

#     def __init__(self, name):
#         self.name = name


# student1 = Student("Ada")
# student2 = Student("Grace")

# # print(student1.school)
# # print(student2.school)

# # print(Student.school)


# Student.school = "AI academy"

# student1.school = "Another school"

# print(student1.school)
# print(student2.school)
# print(Student.school)


# # class attributes -> shared class-level data
# # instance attributes -> data belonging to an individual object



#---------------------------------------


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


#---------------------------------------
# collection of objects


# class Student:

#     def __init__(self, name, score):
#         self.name = name
#         self.score = score

#     def get_status(self):
#         if self.score >= 70:
#             return "Pass"

#         return "Fail"


# students = [
#     Student("Anna", 85),
#     Student("Bob", 62),
#     Student("Charlie", 91),
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
#     if student.score >= 70
# ]


# for student in passed_students:
#     print(student.name)


# #---------------------------------------------



# class Teacher:
#     def __init__(self, name):
#         self.name = name


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


#---------------------------------------------



class Student:
    def __init__(self, name):
        self.name = name


class Course:
    def __init__(self, name):
        self.name = name
        self.students = []

    def add_student(self, student):
        self.students.append(student)


course = Course("Python Foundation")

student1 = Student("Ada")
student2 = Student("Grace")


course.add_student(student1)
course.add_student(student2)


for student in course.students:
    print(student.name)



