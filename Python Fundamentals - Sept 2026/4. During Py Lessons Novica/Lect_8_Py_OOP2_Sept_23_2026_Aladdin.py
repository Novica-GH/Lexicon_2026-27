#********************************************************************************************
#  Novica Ivkovic                                                                           *
#  Cours: System Developer Python and AI                                                    *
#  September 23 2026 - LAB N CHALLENGE                                                      *
#             Today's study goal is:  We continue with OOP 
#********************************************************************************************



#********************************************************************************************
#  Part 0 - From yesterday
#********************************************************************************************

# class Student:
#     def __init__(self,name):
#         self.name= name

# class Course: 
#     def __init__(self, name):
#         self.name = name
#         self.student =[]

#     def add_student(self, student):
#         self.student.append(student)

# course = Course("Python Foundation")

# student1 = Student("Ada")
# student2 = Student("Grace")

# course.add_student(student1)
# course.add_student(student2)

# for student in course.students:
#     print(student.name)


#***********************************************************************************************
#  Part 1            Problem definisanja argumenata u __init__           *
#***********************************************************************************************

# class Course: 
#     def __init__(self, name, student=[]):  # Default arguments 
#         self.name = name
#         self.student = student

             
# Bad pattern    
#------------------

# class BadCourse:
#     def __init__(self, name, students=[]):
#         self.name = name
#         self.students = students


#     def add_student(self, student):
#         self.students.append(student)

# course1 = BadCourse("Python")
# course2 = BadCourse("AI")

# course1.add_student("Ada")

# print(course1.students)    #  ['Ada'] 
# print(course2.students)    #  ['Ada']

# Comon sollution is to use NONE


#****************************************************************************************************
# Part 2:   Correct pattern                      *
#****************************************************************************************************

# class Course:
#     def __init__(self, name, students=None):
#         self.name = name

#         if students is None:
#             students=[]
#         self.students = students

#     def add_student(self, student):
#         self.students.append(student)

# course1 = Course("Python")
# course2 = Course("AI")

# course1.add_student("Ada")

# print(course1.students)   #  ['Ada']
# print(course2.students)   #  []




#************************************************************************************************
#  Part 3    Dict VS Class
#************************************************************************************************

# Dict
# ''
# student_dict = {
#     "name" : "Ada",
#     "score": 91 
# }

# #class

# class Student: 
#     def __init__(self, name, score):
#         self.name = name
#         self.score = score

# student_object = Student("Ada", 91)''



#******************************************************************************************************
#  Part X                           OOP PART II  - INHERETENCE
#******************************************************************************************************

# How one class can use another class  - Ingeretance

# class Dog:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     def eat(self):
#         print(self.name, "is eating.")

# class Cat:
#     def __init__(self, name, age):
#         self.name = self
#         self.age = age

#      def eat(self):
#             print(self.name, "is eating.")

# dog = Dog("Rex", 5)
# cat = Cat("Luna", 3)

# dog.eat()
# cat.eat()

#-------------------------------------------------

# class Animal:       # Animal is the base 
#     def __init__(self, name, age):
#         self.name = self
#         self.age = age

#     def eat(self):
#         print(self.name, "is eating")

# class Dog(Animal):   # Dog is subclass of clas Animal
#     pass

# class Cat(Animal):
#     pass

# dog = Dog("Rex", 5)
# cat = Cat("Luna", 3)

# print(dog.name)
# print(cat.name)

# dog.eat()
# cat.eat()

# Terminology:

# Animal: parent class / basse class / superclass

# Dog:  a child class / derived class / subclass

# The "IS-A" test



#*******************************************************************************************************
#  PART  - Inheretance methods                          *
#*******************************************************************************************************

# class Animal:
#     def __init__(self, name):
#         self.name = name 

#     def eat(self):
#         return f"{self.name} is eating"

#     def sleep(self):
#         return f"{self.name} is sleeping"

# class Dog(Animal):
#     pass

#     print(dog.eat())
#     print(dog.sleep())





#---------------------------------------------------------------
# class Animal:
#     def __init__(self, name):
#         self.name = name 

#     def eat(self):
#         return f"{self.name} is eating"


# class Dog(Animal):
#     def bark(self):
#         return f"{self.name} says woof!"

# dog = Dog("Rex")

# print(dog.eat())
# print(dog.bark())


#----------- Pozivanje bark is Animal?

# class Animal:
#     def __init__(self, name):
#         self.name = name 

#     def eat(self):
#         return f"{self.name} is eating"


# class Dog(Animal):
#     def bark(self):
#         return f"{self.name} says woof!"

# dog = Dog("Rex")

# print(dog.eat())
# print(dog.bark())



# animal = Animal("Unknown")  #AttributeError: 'Animal' object has no attribute 'bark'   -- NO NO
# print(animal.bark())        # Parent doesn't take över def/method from childe by default (directly)!!!



#*******************************************************************************************************
#  10:17 Nastavljamo dalje drugi deo casa.                                        *
#*******************************************************************************************************

# class Animal:                                  # Instead of repet the same method from parent
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age 


# class Dog(Animal):                              # We use super()
#     def __init__(self, name, age, breed):
#         self.name = name
#         self.age = age 
#         self.breed = breed


# dog = Dog("Rex", 5, "Labrador")

# print(dog.name)
# print(dog.age)
# print(dog.breed)

# super()

# class Animal:                                  # Instead of repet the same method from parent
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age 

#         self.is_alive = True

#         if age < 0:
#             raise ValueError("age cannot be negative!")


# class Dog(Animal):                              # We use super()
#     def __init__(self, name, age, breed):
#         super().__init__(name,age)

#         self.breed = breed


# dog = Dog("Rex", 5, "Labrador")

# print(dog.name)
# print(dog.age)
# print(dog.breed)
# print(dog.is_alive)


#----------------------------------------------------------
#  OBS puno problema ovde - pogledaj ponovo video

# class Animal:                                  # Instead of repet the same method from parent
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age 

#         self.is_alive = True

#         if age < 0:
#             raise ValueError("age cannot be negative!")


# class Dog(Animal):                              # We use super()
#     def __init__(self, name, age, breed):
#         self.name = name
#         self.age = age
#         self.is_alive = True

#         if age < 0:
#             raise ValueError("age cannot be negative!")
    

# dog = Dog("Rex", 5, "Labrador")

# print(dog.name)
# print(dog.age)
# print(dog.breed)
# print(dog.is_alive)


#-------------------------------------------------------

# Method Overriding
#---------------------------------------

# class Animal:

#     def __init__(self, name):
#         self.name = name

#     def make_sound(self):
#         return("Some animal sound")

# class Dog(Animal):
#     def make_sound(self):
#         return "Woof!"

# class Cat(Animal):
#     def make_sound(self):
#         return "Meow!"

# animal = Animal("Animal")
# dog = Dog("Rex")
# cat = Cat("Luna")

# print(animal.make_sound())
# print(dog.make_sound())
# print(cat.make_sound())



#*******************************************************************************************************
#  Challenge: LAB N                   - Part 8 -                                          *
#*******************************************************************************************************

class Employee:

    def get_information(self):
        return "Employee information"


class Developer(Employee):

    def get_information(self):
        base_information = super().get_information()

        return(base_information + "-Role: Developer")

developer = Developer()

print(developer.get_information)













#*******************************************************************************************************
#  Challenge: LAB N                   - Part 9 -                                          *
#*******************************************************************************************************


#*******************************************************************************************************
#  Challenge: LAB N               - Final Challenge -                                           *
#*******************************************************************************************************





# **********************************  END of LAB 6  ********************************************************