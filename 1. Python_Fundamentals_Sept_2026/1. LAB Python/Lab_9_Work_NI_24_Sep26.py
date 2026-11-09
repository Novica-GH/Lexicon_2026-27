#********************************************************************************************
#  Novica Ivkovic                                                                           *
#  Cours: System Developer Python and AI                                                    *
#  September 24 2026 - LAB 9                                                                *
#             Today's study goal is:   OOP3                                                  *
#********************************************************************************************


#********************************************************************************************
#  LAB 9                     Part A - Polymorphism                                          *
#********************************************************************************************


# Part A.1. Create three classes: emailNotification, SMSNotification and PushNotification.
#------------------------------------------------------------------------------------------

# class EmailNotification:
#     def __init__(self, email_address):
#         self.recipient = email_address


# class SMSNotification:
#     def __init__(self, phone_number):
#         self.recipient = phone_number


# class PushNotification:
#     def __init__(self, device_token):
#         self.recipient = device_token


# email = EmailNotification("user@lexicon.com")
# sms = SMSNotification("+46731234567")
# push = PushNotification("token_abf123")

# print()
# print(email)
# print(sms)
# print(push)
# print()




# Part A.2. Give all three classes a method called sen(), but make each method return a different message.
#----------------------------------------------------------------
     
# class EmailNotification:
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




# Part A.3 Create one object from each class and store them in the same list.
#-----------------------------------------------------------------

# class EmailNotification:
#     def __init__(self, email_address):
#         self.recipient = email_address

#     def send(self, message):
#         return f"[EMAIL] Sent to {self.recipient} via SMTP server: '{message}'"


# class SMSNotification:
#     def __init__(self, phone_number):
#         self.recipient = phone_number

#     def send(self, message):
#         return f"[SMS] Sent to {self.recipient} via Teia Gateway: '{message}'"


# class PushNotification:
#     def __init__(self, device_token):
#         self.recipient = device_token

#     def send(self, message):
#         return f"[PUSH] Sent to device {self.recipient} via P-Service: '{message}'"



# email_obj = EmailNotification("user@lexicion.com")
# sms_obj = SMSNotification("+46731234567")
# push_obj = PushNotification("token_abf123")


# notifications = [email_obj, sms_obj, push_obj]


# print("\n    ---   Objects stored in the list:   ---")
# for item in notifications:
#     print(type(item), item)




# Part A.4 Loop through the list and call send() on every object.
#---------------------------------------------------------------------

# class EmailNotification:
#     def __init__(self, email_address):
#         self.recipient = email_address

#     def send(self, message):
#         return f"[EMAIL] Sent to {self.recipient} via SMTP server: '{message}'"


# class SMSNotification:
#     def __init__(self, phone_number):
#         self.recipient = phone_number

#     def send(self, message):
#         return f"[SMS] Sent to {self.recipient} via Teia Gateway: '{message}'"


# class PushNotification:
#     def __init__(self, device_token):
#         self.recipient = device_token

#     def send(self, message):
#         return f"[PUSH] Sent to device {self.recipient} via P-Service: '{message}'"


# email_obj = EmailNotification("user@lexicion.com")
# sms_obj = SMSNotification("+46731234567")
# push_obj = PushNotification("token_abf123")


# notifications = [email_obj, sms_obj, push_obj]

# message_text = "System Uppdate at 02:00 UTC."

# print("\n          ---  Sending notifications to all channels  ---\n")

# for notification in notifications:    
    
#     result = notification.send(message_text)
#     print(result)





# Part A.5 In a comment, explain why the loop does not need to know the exact class of each object.
#----------------------------------------------------------------------------------------------------------------

# The loop does not need to know the exact class of each object because of 
# Polymorphism and Python's 'Duck Typing' philosophy. 

# Since all three classes (EmailNotification, SMSNotification, PushNotification) 
# implement a method with the exact same name and signature (`send(message)`), 
# the loop simply calls `notification.send(message_text)` on whatever object 
# it receives. 

# Python evaluates and executes the correct class-specific method dynamically at 
# runtime. As long as the object responds to the `send()` method, the loop will 
# work seamlessly without checking the object's explicit type.

# Exampel:

# for notification in notifications:        
#     print(notification.send(message_text))



#***********************************************************************************************
#  LAB 9               Part B - Polymorphism with inheritance                                  *
#***********************************************************************************************


# Part B.1 Create a base class Document with a title attribute and a method describe().
#--------------------------------------------------------------------------------------

# class Document:
#     def __init__(self, title):
#         self.title = title

#     def describe(self):
#         return f"\nDocument Title: '{self.title}',\n"


# doc = Document("General Specification")
# print(doc.describe())




# Part B.2 Create PDFDocument(Document) and TextDocument(Document).
#------------------------------------------------------------------

# class Document:
#     def __init__(self, title):
#         self.title = title

#     def describe(self):
#         return f"\nDocument Title: '{self.title}'"


# class PDFDocument(Document):
#     def __init__(self, title, line_count):
#         super().__init__(title)
#         self.line_count = line_count


# class TextDocument(Document):
#     def __init__(self, title, word_count):
#         super().__init__(title)
#         self.word_count = word_count


# pdf = PDFDocument("Python Fundamentals", 120)
# txt = TextDocument("Notes", 450)

# print(pdf.describe())
# print(f"Lines: {pdf.line_count}")

# print(txt.describe())
# print(f"Words: {txt.word_count}\n")




# Part B.3 Override describe() in both subclasses so they return different descriptions.
#---------------------------------------------------------------------------------------

# class Document:
#     def __init__(self, title):
#         self.title = title

#     def describe(self):
#         return f"Document Title: '{self.title}'"



# class PDFDocument(Document):       
#     def __init__(self, title, line_count):
#         super().__init__(title)              
#         self.line_count = line_count

#     def describe(self):             # Override describe() - Py subclass
#         return f"\n[PDF] '{self.title}' contains {self.line_count} lines."


# class TextDocument(Document):
#     def __init__(self, title, word_count):
#         super().__init__(title)      
#         self.word_count = word_count

#     def describe(self):             # Override describe() - Text subclass
#         return f"[TXT] '{self.title}' contains {self.word_count} words.\n"


# pdf = PDFDocument("Python OOP Examples", 1500)
# txt = TextDocument("Meeting Notes", 320)

# print(pdf.describe())
# print(txt.describe())



# Part B.4 Create several PDFDocument and TextDocument objects and store them in one list.
#--------------------------------------------------------------------------------------

# class Document:
#     def __init__(self, title):
#         self.title = title

#     def describe(self):
#         return f"Document Title: '{self.title}'"


# class PDFDocument(Document):
#     def __init__(self, title, line_count):
#         super().__init__(title)
#         self.line_count = line_count

#     def describe(self):
#         return f"[PDF] '{self.title}' contains {self.line_count} lines."


# class TextDocument(Document):
#     def __init__(self, title, word_count):
#         super().__init__(title)
#         self.word_count = word_count

#     def describe(self):
#         return f"[TXT] '{self.title}' contains {self.word_count} words."



# pdf1 = PDFDocument("Python OOP Guide", 1500)
# pdf2 = PDFDocument("Data Structures Manual", 2000)

# txt1 = TextDocument("Meeting Notes", 320)
# txt2 = TextDocument("Project Ideas", 150)


# documents = [pdf1, txt1, pdf2, txt2]

# print("\nList of documents successfully created with", len(documents), "items.\n")




# Part B.5 Loop through the list and print each document's title and the result of describe().
#----------------------------------------------------------------------------------------------------

# class Document:
#     def __init__(self, title):
#         self.title = title

#     def describe(self):
#         return f"Document Title: '{self.title}'"


# class PDFDocument(Document):
#     def __init__(self, title, line_count):
#         super().__init__(title)
#         self.line_count = line_count

#     def describe(self):
#         return f"[PDF] '{self.title}' contains {self.line_count} lines."


# class TextDocument(Document):
#     def __init__(self, title, word_count):
#         super().__init__(title)
#         self.word_count = word_count

#     def describe(self):
#         return f"[TXT] '{self.title}' contains {self.word_count} words."


# pdf1 = PDFDocument("Python Fundamentals   ", 3500)
# pdf2 = PDFDocument("Data Structures Manual", 2700)
# txt1 = TextDocument("Meeting Notes         ", 320)
# txt2 = TextDocument("Project Ideas         ", 150)

# documents = [pdf1, txt1, pdf2, txt2]


# print("\n                           ---      Document Descriptions       ---\n")
# for doc in documents:

#     print(f"Title: {doc.title} - Description: {doc.describe()}")
# print()
                  

    


#********************************************************************************************************
#  LAB 9                            PART C - Duck typing                                                *
#********************************************************************************************************


# C.1. Create two unrelated classes, for example Printer and Screen. Do not use inheritance between them.
#--------------------------------------------------------------------------------------------------------


# class Printer:
#     def __init__(self, model_name):
#         self.model_name = model_name


# class Screen:
#     def __init__(self, resolution):
#         self.resolution = resolution


# printer = Printer("HP LaserJet Pro")
# screen = Screen("1920x1080")        # Full HD/1080p

# print(f"\nPrinter model:     {printer.model_name}")
# print(f"Screen resolution: {screen.resolution}\n")


# C.2 Give both classes a method called display_status().
#-----------------------------------------

# class Printer:
#     def __init__(self, model_name):
#         self.model_name = model_name

#     def display_status(self):
#         return f"\n[PRINTER STATUS] Model:      {self.model_name} | Toner:      85% | Paper: Ready"


# class Screen:
#     def __init__(self, resolution):
#         self.resolution = resolution

#     def display_status(self):
#         return f"[SCREEN  STATUS] Resolution: {self.resolution}       | Brightness: 75% | Power: ON\n"



# printer = Printer("HP LaserJet Pro")
# screen = Screen("2560x1440")        # QHD (Quad HD) eller 1440p

# print(printer.display_status())
# print(screen.display_status())


# C.3 Create objects from both classes and store them in the same list.
#------------------------------------------------------------

# class Printer:
#     def __init__(self, model_name):
#         self.model_name = model_name

#     def display_status(self):
#         return f"\n[PRINTER STATUS] Model:      {self.model_name} | Toner:      85% | Paper: Ready"


# class Screen:
#     def __init__(self, resolution):
#         self.resolution = resolution

#     def display_status(self):
#         return f"[SCREEN  STATUS] Resolution: {self.resolution}       | Brightness: 75% | Power: ON\n"



# printer_obj = Printer("HP LaserJet Pro")
# screen_obj  = Screen("2560x1440")

# peripherals = [printer_obj, screen_obj]

# print("\nObjects in peripherals list:\n")
# for item in peripherals:
#     print(type(item), item)
# print()



# C.4 Loop through the list and call dispaly_status() on each object.
#------------------------------------------------------------------------------------------------

# class Printer:
#     def __init__(self, model_name):
#         self.model_name = model_name

#     def display_status(self):
#         return f"[PRINTER STATUS] Model: {self.model_name} | Toner: 85% | Paper: Ready"


# class Screen:
#     def __init__(self, resolution):
#         self.resolution = resolution

#     def display_status(self):
#         return f"[SCREEN STATUS] Resolution: {self.resolution} | Brightness: 75% | Power: ON"


# printer_obj = Printer("HP LaserJet Pro")
# screen_obj = Screen("2560x1440")

# peripherals = [printer_obj, screen_obj]


# print("\n          --- Displaying status for all peripherals ---\n")
# for item in peripherals:                # Duck Typing - here
#     print(item.display_status())
# print()




# C.5 In a comment, explain why this works even though the classes do not share a base class.
#--------------------------------------------------------------------------------------------

# EXPLANATION:

# This works because Python uses dynamic typing and follows the 'Duck Typing' paradigm 
# ("If it walks like a duck and quacks like a duck, it's a duck").

# Python does not require classes to inherit from a common base class or implement an 
# explicit interface to achieve polymorphic behavior. During execution, the loop 
# simply expects the object to have a `display_status()` method. 

# As long as each object in the list provides a `display_status()` method with a matching 
# interface, Python executes it dynamically at runtime regardless of the object's class.
# """

# # Previous exemple:

# for item in peripherals:
#     print(item.display_status())
# Python doesn't care WHAT an object IS (its class), but rather WHAT it CAN DO (its methods).





#************************************************************************************************
#  LAB 9                  PART D -  instance()                                                  *
#************************************************************************************************



# D.1  Create a base class User and a subclass AdminUser(User).
#-------------------------------------------------------------------------

# class User:
#     def __init__(self, username, email):
#         self.username = username
#         self.email = email

#     def get_details(self):
#         return f"User: {self.username} ({self.email})"


# class AdminUser(User):
#     def __init__(self, username, email, admin_level):
#          # Calling the base class constructor with super()
#         super().__init__(username, email)
#         self.admin_level = admin_level

#     def get_details(self):
#         # Calling the base class constructor with super()
#         base_details = super().get_details()
#         return f"[ADMIN] {base_details} | Level: {self.admin_level}\n"


# user1 = User("adaericsson", "ada.ericsson@lexicon.com")
# admin1 = AdminUser("bob_admin", "bob.admin@lexicon.com", "SuperAdmin")
# print()
# print(user1.get_details())
# print(admin1.get_details())



# D.2 Create an AdminUser object.
#-------------------------------------------------------

# class User:
#     def __init__(self, username, email):
#         self.username = username
#         self.email = email

#     def get_details(self):
#         return f"User: {self.username} ({self.email})"


# class AdminUser(User):
#     def __init__(self, username, email, admin_level):
#         # Pozivanje konstruktora bazne klase pomoću super()
#         super().__init__(username, email)
#         self.admin_level = admin_level

#     def get_details(self):
#         # Calling the base class constructor with super()
#         base_details = super().get_details()
#         return f"\n[ADMIN] {base_details} | Level: {self.admin_level}\n"


# admin_user = AdminUser("sys_admin", "admin@lexicon.com", "SuperAdmin")

# print(admin_user.get_details())




# D.3 Use isinstance() to check whether the object is an AdminUser, a User and a string.
#--------------------------------------------------------

# class User:
#     def __init__(self, username, email):
#         self.username = username
#         self.email = email


# class AdminUser(User):
#     def __init__(self, username, email, admin_level):
#         super().__init__(username, email)
#         self.admin_level = admin_level


# admin_user = AdminUser("sys_admin", "admin@company.com", "SuperAdmin")


# is_admin  = isinstance(admin_user, AdminUser)
# is_user   = isinstance(admin_user, User)
# is_string = isinstance(admin_user, str)

# print(f"Is admin_user an instance of AdminUser? {is_admin}")    #True
# print(f"Is admin_user an instance of User?      {is_user}")     #True
# print(f"Is admin_user an instance of str?       {is_string}")   #False




# D.4 Print all three results.
#-----------------------------------------------------------------------

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



# D.5 Ina comment, explain why the AdminUser object is also considered an instance of User.
#-----------------------------------------------------------------

# The AdminUser object is considered an instance of User because of Class Inheritance (IS-A relationship).




#******************************************************************************************************
#  LAB 9                         Part E -     __str__                                                 *
#******************************************************************************************************


# E.1 Create a Product class with name and price.
#--------------------------------------------------------------

# class Product:
#     def __init__(self, name, price):
#         self.name = name
#         self.price = price


# laptop = Product("Laptop", 7500.00)

# print(f"\nProduct name: {laptop.name}")
# print(f"Product price: {laptop.price} kr\n")



# E.2 Create one Product object and print it before defining  __str__. Observe the result. 
#---------------------------------------------------------------------------

# class Product:
#     def __init__(self, name, price):
#         self.name = name
#         self.price = price

# phone = Product("Smartphone", 5000.00)

# print(f"\n{phone}\n")



# E.3 Add __str__ so printing to Product gives a useful human-readable description.
#-------------------------------------------

# class Product:
#     def __init__(self, name, price):
#         self.name = name
#         self.price = price

#     def __str__(self):
#         return f"\nProduct: {self.name} | Price: {self.price:.2f} kr\n"


# phone = Product("Smartphone", 5000.)

# # print() call __str__ method now.
# print(phone)



# E.4 Create at least three Product objects and print them.
#-------------------------------------------------------------------------------------------------

# class Product:
#     def __init__(self, name, price):
#         self.name = name
#         self.price = price

#     def __str__(self):
#         return f"Product: {self.name} | Price: {self.price:.2f} kr"


# product1 = Product("Laptop", 9000.00)
# product2 = Product("Wireless Mouse", 750.00)
# product3 = Product("Keyboard", 400.00)

# print(product1)
# print(product2)
# print(product3)
# print()



# E.5 Use str() on one Product object, store the result in a variable and print its type.
#------------------------------------------------------------------------------

# class Product:
#     def __init__(self, name, price):
#         self.name = name
#         self.price = price

#     def __str__(self):
#         return f"Product: {self.name} | Price: {self.price:.2f} kr"


# laptop = Product("Laptop", 8000.00)

# product_description = str(laptop)

# print(f"Result value: {product_description}")
# print(f"Result type:  {type(product_description)}")
# print()




#*******************************************************************************************************
#  LAB 9                    Part F -   __str__ with inheritance                                        *
#*******************************************************************************************************


# F.1 Create a base class Account with owner and balance.
#----------------------------------------------------------------------------------

# class Account:
#     def __init__(self, owner, balance):
#         self.owner = owner
#         self.balance = balance


# account1 = Account("Ada Ericsson", 35500.00)

# print(f"\nAccount Owner: {account1.owner}")
# print(f"Account Balance: {account1.balance:.2f}\n")



# F.2 Add __str__ to Account.
#-----------------------------------------------------------------------------------------------------

# class Account:
#     def __init__(self, owner, balance):
#         self.owner = owner
#         self.balance = balance

#     def __str__(self):
#         return f"\nAccount Owner: {self.owner} | Balance: {self.balance:.2f}kr\n"


# account1 = Account("Ada Ericsson", 35500.00)

# print(account1)




# F.3 Create SavingsAccount(Account) with an additional interest_rate attribute. Use super() in __init__.
#----------------------------------------

# class Account:
#     def __init__(self, owner, balance):
#         self.owner = owner
#         self.balance = balance

#     def __str__(self):
#         return f"\nAccount Owner: {self.owner} | Balance: {self.balance:.2f} kr\n"


# class SavingsAccount(Account):  # subclass/child
#     def __init__(self, owner, balance, interest_rate):
        
#         super().__init__(owner, balance)
#         self.interest_rate = interest_rate


# savings = SavingsAccount("Bob Doll", 55000.0, 2.5)

# print(f"Owner: {savings.owner}")
# print(f"Balance: {savings.balance:.2f} kr")
# print(f"Interest Rate: {savings.interest_rate}%\n")



# F.4  Override __str__ in SavingsAccount so its output also includes the interest rate.
#---------------------------------------------------



# F.5 Create and print both an Account and a SavingsAccount object.
#---------------------------------------------------------------------------------

# class Account:
#     def __init__(self, owner, balance):
#         self.owner = owner
#         self.balance = balance

#     def __str__(self):
#         return f"Account Owner: {self.owner} | Balance: {self.balance:.2f} kr"


# class SavingsAccount(Account):
#     def __init__(self, owner, balance, interest_rate):
#         super().__init__(owner, balance)
#         self.interest_rate = interest_rate

#     def __str__(self):
#         sav_acc_str = super().__str__()
#         return f"\n[SAVINGS] {sav_acc_str} | Interest Rate: {self.interest_rate}%\n"


# savings = SavingsAccount("Ada Ericsson", 70000.0, 1.5)

# print(savings)




#*******************************************************************************************************
#  LAB 9                        Part G -   Inheritance or composition?                                 *
#*******************************************************************************************************



# G.1 Create CPU with a model attribute.
#----------------------------------------------------------

# class CPU:
#     def __init__(self, model):
#         self.model = model

#     def __str__(self):
#         return f"\nCPU Model: {self.model}\n"


# cpu_component = CPU("Intel Core i7-13700K")
# print(cpu_component)



# G.2 Create Computer with brand and a CPU object. Use composition, not inheritance.
#-----------------------------------------------------------------------------------

# class CPU:
#     def __init__(self, model):
#         self.model = model

#     def __str__(self):
#         return f"CPU Model: {self.model}"


# class Computer:
#     def __init__(self, brand, cpu):
#         self.brand = brand
#         self.cpu = cpu  # Composition: Computer HAS-A CPU object

#     def __str__(self):
#         return f"\nComputer Brand: {self.brand} | {self.cpu}"


# my_cpu = CPU("Intel Core i7-13700K")
# my_computer = Computer("Dell", my_cpu)

# print(my_computer)
# print(f"Direct CPU model access: {my_computer.cpu.model}\n")



# G.3 Create a CPU object and pass it to a Computer object.
#-----------------------------------------------------------

# class CPU:
#     def __init__(self, model):
#         self.model = model

#     def __str__(self):
#         return f"CPU Model: {self.model}"


# class Computer:
#     def __init__(self, brand, cpu):
#         self.brand = brand
#         self.cpu = cpu  # Composition: Receiving a CPU instance

#     def __str__(self):
#         return f"\nComputer Brand: {self.brand} | {self.cpu}\n"


# processor = CPU("AMD Ryzen 9 7950X")
# workstation = Computer("Lenovo", processor)  # Composition: Receiving a CPU instance-"processor"

# print(workstation)



# G.4 Print the computer brand and CPU model through the Computer object.
#------------------------------------------------------------------------


# G.5 In comments, explain why "Computer HAS-A CPU" makes more sense tha "Computer IS-A CPU".
#--------------------------------------------------------------------------------------------

# class CPU:
#     def __init__(self, model):
#         self.model = model

#     def __str__(self):
#         return f"CPU Model: {self.model}"


# class Computer:
#     def __init__(self, brand, cpu):
#         self.brand = brand
#         self.cpu = cpu  # Composition: Stores a CPU object reference

#     def __str__(self):
#         return f"Computer Brand: {self.brand} | {self.cpu}"


# processor = CPU("Intel Core i9-14900K")   # objects istance
# desktop = Computer("ASUS", processor)

# print(f"\nComputer Brand: {desktop.brand}")       # Print brand and CPU model through the Computer object
# print(f"CPU Model:      {desktop.cpu.model}\n")


# G.6 For each pair below, write whether you would most likely use inheritance (IS-A) or composition 
#     (HAS_A): Car/ Engine, Manager/Employee, Course/Teacher, Phone/Device.





#*******************************************************************************************************
#  LAB 9                     Part H -   Applied challenge: Export system                               *
#*******************************************************************************************************


# H.1 Build a small export system using the concepts from today's lesson.
#-------------------------------------------------------------




# H.2 Create a base class Exporter with a method export(data).
#--------------------------------------------



# H.3 Dreate at least three subclasses, for example ConsoleExporter, TextExporter and SummaryExporter.
#----------------------------------------------------------------------------------------


# H.4 Override export(data) in every subclass so each handles the same data differently. You do not need to create real files. 
# ------------------------------------------------------------- 




# H.5 Add a useful __str__ mehtod to the exporter classes.
# ------------------------------------------------------------- 





# H.6 Create several exporter objects and store them in one list.
#-------------------------------------------------------------




# H.7 Loop through the list and eall export() on each object to demonstrate polymorphism
#--------------------------------------------



# H.8 Create one additional class that is not part of the Exporter inheritance hierarchy 
#     but stio provides an expoet(data) method. Show that it can be used by the same calling code.
#----------------------------------------------------------------------------------------


# H.9 Use isinstance() at least once to inspect a meaningful type relationship.
#----------------------------------------------------------------------------------------




# H.10 Add one example of composition to the program and explain the HAS-A relationship in a comment.
#----------------------------------------------------------------------------------------





# **********************************  END of LAB 9  ********************************************************