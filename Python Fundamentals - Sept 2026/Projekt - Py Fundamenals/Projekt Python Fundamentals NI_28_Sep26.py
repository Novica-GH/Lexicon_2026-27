#********************************************************************************************
#  Novica Ivkovic                                                                           *
#  Cours: System Developer Python and AI                                                    *
#  September 28 2026 -                                                                      *
#                              P R O J E C T - Python Fundamentals                          *
#                                                                                           *
#            Python Fundamentals - slut PROJECT - Option 3 - Booking System (HOTEL)         *
#                                                                                           *
#                                                                                           *
#********************************************************************************************


#********************************************************************************************
# 
#   OPTION 3 - Booking System
# 
#    -  Build a Python program for managing bookings.
#    -  You decide what kind of booking system you want to create. 
#    -  It could be used for (hotel rooms), sports facilities, meeting rooms, activities, 
#       appointments or another type of resource or service. 
#    -  The system should contain different types of objects that interact with each other
#    -  For example, a booking could connect a customer with something that can be bokat.
#    -  Bookings should have meaningful behaviour. They might be created, cancelled, changed
#       or checked in different ways. 
#    -  The system should keep track of its current state while the program is running. 
#    -  You decide how bookings, customers, resources and other parts of your system 
#       should be represented and how they relate to each other.
#
#    -  No database or permanent data storage is required. The data only needs to exists  
#       while program is running.
#
#       Possible ideas
#
#       - diferent types of bookable resources or services
#       - customers
#       - availability
#       - booking status
#       - cancellation
#       - preventing conflicting bookings
#       - prices or costs
#       - different booking rules
#       - searching and filtering bookings
#       - statistics
#       - summaries of available and booked resources
#
#
#*******************************************************************************************



#***********************************************************************************************
#
#                                   CORE EXPECTATIONS
#
#   1.  Build a Complete and Connected Program  
#   2.  Use Object-Oriented Programming 
#   3.  Create Relationships and Interactions Between Objects  
#   4.  Actions Should Affect the State of Your System  
#   5.  Work With Collections of Data or Objects
#   6.  Include Meaningful Program Logic
#   7.  Handle Invalid or Unreasonable Actions   
#   8.  Organize the Project Into Multiple Python Modules    
#   9.  Make the Program Runnable and Demonstrable   
#   10. Use Git Throughout the Project 
#
#       -   Add basic booking functionality
#       -   Prevent conflicting bookings  
#       -   Add visitor interactions  
#       -   Implement character  health system          
#       -   Refactor shared behaviour       
#       -   Fix negative enery bug   
#
#***********************************************************************************************

         

#************************************************************************************************
#                                  HOTEL - ASTORIA - Managing booking Project (Reception++)
#************************************************************************************************

# For the begining I need just: 
#
#   -   Customer (Standard/VIP or [Business/Leisure (Turists) or Tour Groups/Leisure Groups/Transit guests)]
#   -   Room (Standard room/Suite )
#   -   Booking ()
#   - ... next steps ....


#               +++++++++++++++++++++   CLASES   ++++++++++++++++++++++

class Customer:
    def __init__(self, customer_id: int, name: str, email: str):
        self.customer_id = customer_id
        self.name = name  
        self.email = email

    def get_discount_rate(self):
        return 0.0  # For standard customers there isn't any discount

    def __str__(self):
        return f"Customer: [ID: {self.customer_id}], name: {self.name}, e-mail: ({self.email})"


class VIPCustomer(Customer):  # subclass/child
    def __init__(self, customer_id: int, name: str, email: str, discount_rate: float = 0.15):
        super().__init__(customer_id, name, email)
        self.discount_rate = discount_rate

    def get_discount_rate(self):
        return self.discount_rate

    def __str__(self):
        base_info = super().__str__()
        return f"[VIP] {base_info}, Discount: {int(self.discount_rate * 100)}%"


customer1 = Customer(1212, "Ada","ada.ericsson@az.se")
customer2 = Customer(1313, "Bob", "bob@bob.se") 
customer3 = Customer(1414, "Grace", "grace@grace.net")

customerV = VIPCustomer(5155, "Mr.Been", "rowanatkinson@mr_been.com",0.15)
customerV_2 = VIPCustomer(5255, "Mrs Foley", "mf@foley.org")

print()
print(customer1)   # Customer [ID: 1212] Ada (ada.ericsson@az.com)
print(customerV)   # [VIP] Customer: [ID: 5155], name: Mr.Been, e-mail: (rowanatkinson@mr_been.com), Discount: 15% 
print()

   
#------------------------------------------------


class Room:
    def __init__(self, room_number: int, base_price_per_night: float):
        self.room_number = room_number
        self.base_price_per_night = base_price_per_night
        self.is_clean = True

    def calculate_price(self, nights: int):  #float
        return self.base_price_per_night * nights

    def get_room_type(self):
        return " Room in Hotel Astoria"

    def __str__(self):   # def for print / method - return always string
        return f"Room {self.room_number} ({self.get_room_type()}) - {self.base_price_per_night:.2f} kr/night "

print()
rum1 = Room(4,2000)
rum2 = Room(5, 2200)
rum3 = Room(6,2400)

price_rum1 = rum1.calculate_price(5)
print(price_rum1)               # 10000  (for 5 nights)
print(rum1)                     # Room 4 ( Room in Hotel Astoria) - 2000.00 kr/night
print()



class StandardRoom(Room):       # subclass/child
    def __init__(self, room_number: int, base_price_per_night: float, sea_view: bool = False):
        super().__init__(room_number, base_price_per_night)
        self.sea_view = sea_view

    def get_room_type(self):
        return "Standard Room"

    def __str__(self):
        sea_view_str = "with Sea view" if self.sea_view else "Park view"
        return f"{super().__str__()} [{self.sea_view}]"


rum_standard_1 = StandardRoom(7, 1000)
rum_standard_2 = StandardRoom(8, 1200)
rum_standard_3 = StandardRoom(9, 1300)

price_rum_standard_1 = rum_standard_1.calculate_price(11)
print(price_rum_standard_1)         # 11000  ( 11 nights x 1000 kr)
print(rum_standard_1)               # Room 7 (Standard Room) - 1000.00 kr/night  [False]
print()


class SuiteRoom(Room):      # subclass/child
    def __init__(self, room_number: int, base_price_per_night: float, includes_jacuzzi: bool = True):
        super().__init__(room_number, base_price_per_night)
        self.includes_jacuzzi = includes_jacuzzi

    def get_room_type(self):
        return "Suite Room"

    def calculate_price(self, nights: int):
        luxury_tax = 1000.0   # Suites include a luxury charge
        return (self.base_price_per_night + luxury_tax) * nights

    def __str__(self):
        jacuzzi_str = "with Jacuzzi" if self.includes_jacuzzi else "no Jacuzzi"
        return f"{super().__str__()} [{jacuzzi_str}]"


suite_1 = SuiteRoom(1, 5000)
suite_2 = SuiteRoom(2, 6000)
suite_3 = SuiteRoom(3, 7000)

price_suite_1 = suite_1.calculate_price(7) # 7 nights
print(price_suite_1)            # 42000.0   [7 nights * (price+lux_tax)]
print(suite_1)                  # Room 1 (Suite Room) - 5000.00 kr/night  [with Jacuzzi]
print()
#-----------------------------------------



class Booking:
    STATUS_CONFIRMED = "Confirmed"
    STATUS_CHECKED_IN = "Checked In"
    STATUS_CANCELLED = "Cancelled"

    def __init__(self, booking_id: int, customer: Customer, room: Room, nights: int):
        if nights <= 0:
            raise ValueError("Booking nights must be greater than zero.")  # Varning - ValueError

        self.booking_id = booking_id
        self.customer = customer
        self.room = room
        self.nights = nights
        self.status = self.STATUS_CONFIRMED
        self.total_cost = self._calculate_total()

    def _calculate_total(self):   # internal/Protected method (begining with _) and it is used just by this Class. We don't call it outside of this Class. 
        raw_price = self.room.calculate_price(self.nights)                  # Standard convetion in Python
        discount = self.customer.get_discount_rate()            # This method uses constructor __init__ like help method (not by user)
        return raw_price * (1.0 - discount)

    def check_in(self):
        if self.status != self.STATUS_CONFIRMED:
            raise ValueError(f"Cannot check in a booking with status '{self.status}'.")
        self.status = self.STATUS_CHECKED_IN

    def cancel(self):
        if self.status == self.STATUS_CHECKED_IN:
            raise ValueError("Cannot cancel a booking that is already checked in.")
        self.status = self.STATUS_CANCELLED

    def __str__(self):
        return (
            f"Booking #{self.booking_id} [{self.status}] | "
            f"{self.customer.name} -> Room {self.room.room_number} | "
            f"Nights: {self.nights} | Total: {self.total_cost:.2f} kr"
        )



booking1 = Booking(2609291, customer1, rum1, 3)             # Booking #2609291 [Confirmed] | Ada -> Room 4 | Nights: 3 | Total: 6000.00 kr
booking2 = Booking(2609292, customerV, suite_1, 7 )         # Booking #2609292 [Confirmed] | Mr.Been -> Room 1 | Nights: 7 | Total: 35700.00 kr
booking3 = Booking(2609293, customer2, rum_standard_2, 4)   # Booking #2609293 [Confirmed] | Bob -> Room 8 | Nights: 4 | Total: 4800.00 kr
booking4 = Booking(2609294, customerV_2, suite_3, 21)       # Booking #2609294 [Confirmed] | Mrs Foley -> Room 3 | Nights: 21 | Total: 142800.00 kr

bookings = [booking1,booking2, booking3, booking4]


for boking in bookings:
    print(boking)

print()









#****************************************************************************************************
#  
#   FURTHER DEVELOPMENT
# 
#   ..........
# 
# 
# 
# f
#****************************************************************************************************



#************************************************************************************************
#                                  HOTEL - ASTORIA - parts - all att one place:
#************************************************************************************************


#*************************************
#     PART 1 - PERSONS: - for Very, very big PROJECT... but I need now just a part of all this to begin...
#**********************************

#    1. Employies:  Reception / Manager / Stuff / Service / Waiter / Lichen-chef / Lift boy / Garage personal

#    2. Users:      Simple / Pairs / Groups ( business groups, athletes and coaches, students (with techers or without)

#    3. Places by level of impotance: 1. Reception/Room(floor);  2. Apartman/ Restaurang  3. Kitchen/Elevator/Pool/Gym/Pool/Garage
 
#   4. states and behaviors:    


#PART 3 - Places   - for VERY VERY BIG PROJECT.....
#*******************************************************************************************************

# Reception     - base level
# Room          - base level
# Floor         - base level

# Apartman      - level 2
# Restaurang    - level 2

# Elevator(Hiss)- level 3
# Pool          - level 3
# Jim           - level 3
# Garage        - level 3
# Kitchen       - level 3




#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# PARTS FROM EX CODE, that can be useful here.... / for idea / for brandstorm...
#********************************************************************************

# I need to develope this class for all employies in the hotel.

# class Employee:
#     def __init__(self, name):
#         self.name = name

#     def get_information(self):
#         return f"\nEmployee: {self.name}"


# class Developer(Employee):
#     def __init__(self, name, programming_language="Python"):
#         super().__init__(name)
#         self.programming_language = programming_language

#     def write_code(self):
#         return f"{self.name} is writing {self.programming_language} code."


# class Manager(Employee):
#     def __init__(self, name, department="IT"):
#         super().__init__(name)
#         self.department = department

  
#     def conduct_meeting(self):
#         return f"{self.name} is conducting a meeting for the {self.department} department.\n"


# mngr = Manager("Charlie", "Engineering")

# print(mngr.get_information())
# print(mngr.conduct_meeting())
#-------------------------------------------------


# - Simple user

# class User:   
#     def __init__(self, username, email):
#         self.username = username
#         self.email = email


# class AdminUser(User):
#     def __init__(self, username, email, admin_level):
#         super().__init__(username, email)
#         self.admin_level = admin_level


# admin_user = AdminUser("sys_admin", "admin@company.com", "SuperAdmin")


# is_admin = isinstance(admin_user, AdminUser)
# is_user = isinstance(admin_user, User)
# is_string = isinstance(admin_user, str)

# print("\n--- isinstance() Check Results ---\n")
# print(f"Is AdminUser: {is_admin}")
# print(f"Is User:      {is_user}")
# print(f"Is string:    {is_string}")
# print()
#-----------------------------------------------------
     



# Primer kada trener/direktor/sef/techer dovodi grupno zaposlene/igrace/studente...
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
#----------------------------------------------------



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
#----------------------------------------------------------


# Nastavak:  Ispis onih studenata koji su prosli....
# passing_students = course.get_passing_students()

# print(f"\nTotal students: {course.get_student_count()}")
# print(f"Students who passed ({len(passing_students)}):")

# for student in passing_students:
#     print(f"- {student.name}: {student.score} points")
# print()
#---------
# 
# ---------------------------------------------------------------------------

#   Add validation somewhere in your program using ValueError. Chose a validation that makes sense.

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
#------------------------------------------------------------------------------





#******************************************************************************************************
#  PART 2 - THINGS AND STAF...
#******************************************************************************************************






# EmailNotification:
#     def __init__(self, email_address):
#         self.recipient = email_address

#     def get_channel(self):
#         return f"Channel: Email ({self.recipient})"

#     def send(self, message):
#         return f"[EMAIL] Sent to {self.recipient} via SMTP server: '{message}'"


# class SMSNotification:
#     def __init__(self, phone_number):
#         self.recipient = phone_number

#     def get_channel(self):
#         return f"Channel: SMS ({self.recipient})"

#     def send(self, message):
#         return f"[SMS]   Sent to {self.recipient} via Telia Gateway: '{message}'"


# class PushNotification:
#     def __init__(self, device_token):
#         self.recipient = device_token

#     def get_channel(self):
#         return f"Channel: Push Notification ({self.recipient})"

#     def send(self, message):
#         return f"[PUSH]  Sent to device {self.recipient} via P-Service: '{message}'\n"


# # Testiranje Part A.2
# email = EmailNotification("user@lexicon.com")
# sms = SMSNotification("+46731234567")
# push = PushNotification("token_abf123")

# print("\n               --- Testing send() methods --- \n")
# print(email.send("Your LAB for September is ready."))
# print(sms.send("Your security code is 1245."))
# print(push.send("You have a new direct message!"))
#------------------------------------------------------------------



# class Document:
#     def __init__(self, title):
#         self.title = title

#     def describe(self):
#         return f"\nDocument Title: '{self.title}',\n"


# doc = Document("General Specification")
# print(doc.describe())
#-----------------------------------------------------



# class Device:
#     def __init__(self, brand, year):
#         self.brand = brand
#         self.year = year


# device = Device("Dell", 2023)
# print(f"Brand: {device.brand}, Year: {device.year}")
#--------------------------------------------------------------



# class Account:
#     def __init__(self, owner, balance):
#         self.owner = owner
#         self.balance = balance

  
# account = Account("Ada", 1000.0)
# print(f"Owner: {account.owner} | Balance: {account.balance}")
#----------------------------------------------------------




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
#-----------------------------------------------------------------------------------------------------------------



# class Product:
#     def __init__(self, name, price):
#         self.name = name    
#         self.price = price  


# product1 = Product("Laptop", 10000.0)  #  Objekt - instance -  classe Product
# product2 = Product("Mouse", 250.0)


# print(f"\nProduct 1: {product1.name} | Price: {product1.price} SEK")
# print(f"Product 2: {product2.name}  | Price:   {product2.price} SEK\n")
#--------------------------------------------------------------------------------



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
#-----------------------------------------------------------------------


#*******************************************************************************************************
# PART 3 - Places   - for VERY VERY BIG PROJECT.....
#*******************************************************************************************************

# Reception     - base level
# Room          - base level
# Floor         - base level

# Apartman      - level 2
# Restaurang    - level 2

# Elevator(Hiss)- level 3
# Pool          - level 3
# Jim           - level 3
# Garage        - level 3
# Kitchen       - level 3









#*******************************************************************************************************
#  LAB N                         Part G -                                           *
#*******************************************************************************************************




# **********************************  END of PROJECT ********************************************************