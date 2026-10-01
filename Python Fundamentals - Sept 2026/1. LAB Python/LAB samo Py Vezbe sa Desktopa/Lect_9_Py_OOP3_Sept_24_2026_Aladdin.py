#******************************************************************************************
# Novica Ivkovic
# Cours: System Developer Python and AI
# September 24 2026 - Today's study goal is:
#                     
#
#*******************************************************************************************
# Part A - OOP3 - Polymorphism
#*********************************************


# class  Dog: 
#     def make_sound(self):
#         return "Woof!"

# class Cat: 
#     def make_sound(self):
#         return "Meow!"

# class Cow:
#     def make_sound(self):
#         return "Moo!"

# animals =[
#     Dog(),
#     Cat(),
#     Cow()
# ]

# for animal in animals:
#     print(animal.make_sound())

# svaki objekat provides sopstveno bihejvijor
# Osnovna ideja polimorfizma je upravo ovo? (KOJE ?)

# Mozemo kombinovati polimorfisam sa inheritance
# -----------------------------------------
# class Animal: 
#     def __init__(self, name):
#         self.name = name

#     def make_sound():    # OBS Fali


# class  Dog(Animal): 
#     def make_sound(self):
#         return "Woof!"

# class Cat(Animal): 
#     def make_sound(self):
#         return "Meow!"


# animals =[
#     Dog("Rex"),
#     Cat("Luna")
# ]

# for animal in animals:
#     print(
#         animal.name,
#         animal.make_sound()
#     )

#------------------------------------------------
# #----------------fali naslov
# class Robot:
#     def make_sound(self):
#         return "Beep!"


# class  Dog: 
#     def make_sound(self):
#         return "Woof!"

# things = [
#     Robot(),
#     Dog()
# ]

# for thing in things:
#     print(thing.make_sound())  # Ovde robot i dog ne dele istu klasu, ali se petlja for moze koristiti na isti nacin

# #If an object probide behevior - 




#******************************************************************************************
# # istance()
#*************************************************

# class Animal:
#     pass

# class Dog(Animal):
#     pass

# dog = Dog()

# print(isinstance(dog,Dog))  # OK True
# print(isinstance(dog,Animal))  # OK True

# print(isinstance(dog, str))   # OBS! False - dog nije objekat od stringa...

# # if isinstance(......) - Ovo je korisna struktura da li je nesto istanca od neke klase / slicno kao tip za...

# # elif isinstance (....):
# # elifif isinstance (...)

#------------------------------------------

# class Student:
#     def __init__(self, name, score):
#         self.name = name 
#         self.score = score

# student = Student("Ada", 91)     # <__main__.Student object at 0x0000020358299D00>
# print(student)                   # Ovde vidimo informaciju o strukturi...


#----------------------------------------------------

# class Student:
#     def __init__(self, name, score):
#         self.name = name 
#         self.score = score

#     def __str__(self):
#         return f"{self.name} - Score: {self.score}"

# student = Student("Ada", 85)

# print(student)

# text = str(student)

# print(text)
# print(type(text))

# # Vazno pravilo je da se ne sme pisati u stringu ???? vec se moramo vratiti ????




#*************************************************************************************************
#    __str:: with inheritance
#************************************************************


# class Employee:
#     def __init__(self, name, salary):
#         self.name = name
#         self.salary = salary

#     def __str__(self):
#         return(
#             f"{self.name}-"
#             f"Salary:{self.salary}"
#         )

# class Developer(Employee):
#     def __init__(self, name, salary, language):
#         super().__init__(name, salary)

#         self.langugae = language

#     def __str__(self):
#         return (
#             f"{self.name} - Developer -"
#             f"{self.langugae}"
#         )

# employee = Employee("Grace", 45000)

# developer = Developer("Ada", 55000,"Python")

# print(employee)
# print(developer)



#************************************************************************************************
# Composiotion
##**********************************************************************************

#  Objekti takodje sadrze drube objekte - Klase sadrze klase...???


# IS-A ( Inheritance)

# HAS-A ( Composition)



class Engine: 
    def __init__(self, horsepower):
        self.horsepower = horsepower

class Car:
    def __init__(self, brand, engine):
        self.brand = brand
        self.engine = engine

engine = Engine(200)

car = Car("Volvo", engine) # engine je objekat druge klase (kompozicija)

print(car.brand)
print(car.engine.horsepower)

# Kratka lekcija za danas - sledi LAB...



















#******************************************************************************************************
# Part E - While loops
#******************************************************************************************************







#*******************************************************************************************************
# Part F - Break and continue
#*******************************************************************************************************




#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
#*******************************************************************************************************
# Part G - Applied  challenge: Console study tracker
#*******************************************************************************************************







#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
#*******************************************************************************************************
# Part H - Stretch challenges
#*******************************************************************************************************




# *******************************************************************************************************