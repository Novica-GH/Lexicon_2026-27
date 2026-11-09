#********************************************************************************************
#  Novica Ivkovic                                                                           *
#  Cours: System Developer Python and AI                                                    *
#  September 23 2026 - LAB 8                                                                *
#             Today's study goal is:           OOP - Part II                                *
#********************************************************************************************


#********************************************************************************************
#  LAB 8             Part A -  OOP Part2 Mutable default arguments
#********************************************************************************************

# Part A.1. Create a BadTeam class with name and a default parameter member=[]. 
#           Add an add_member() method.
#------------------------------------------------------------------------------

# class BadTeam:
    
#     def __init__(self, name, members=[]):
#         self.name = name
#         self.members = members


#     def add_member(self, member_name):
#         self.members.append(member_name)


# team1 = BadTeam("Ada")
# team2 = BadTeam("Bob")

# team1.add_member("Grace")
# team2.add_member("Charlie")

# print(f"Team 1 members: {team1.members}")
# print(f"Team 2 members: {team2.members}")





# Part A.2. Create two BadTeam objects without providing a members list. 
#           Add a member to only one team and print both lists. 
#           Explain in a comment what happend.
#------------------------------------------------------------------------
     
# class BadTeam:
    
#     def __init__(self, members=[]):
#         self.members = members

# team1 = BadTeam()  # two objects
# team2 = BadTeam()

# team1.members.append("Ada")

# print(f"Team 1 members: {team1.members}")   #  Team 1 members: ['Ada']
# print(f"Team 2 members: {team2.members}")   #  Team 2 members: ['Ada'] !!!





# Part A.3 Create a corrected Team class using None as the default value 
#           and create a new list inside __init__.
#-----------------------------------------------------------------

# class Team:
#     def __init__(self, members=None):
        
#         if members is None:
#             self.members = []
#         else:
#             self.members = members

# team1 = Team()   # two Team objects
# team2 = Team()

# team1.members.append("Grace")   # adding a member just in team1

# # Test
# print("Team 1 members:", team1.members)  # Team 1 members: ['Grace']
# print("Team 2 members:", team2.members)  # Team 2 members: []





# Part A.4 Repeat the test with two Team objects and show that each object now has its own list.
#-----------------------------------------------------------------------------------------------


# class Team:
#     def __init__(self, members=None):
        
#         if members is None:
#             self.members = []
#         else:
#             self.members = members


# team1 = Team()
# team2 = Team()

# team1.members.append("Ada")

# print("Team 1 members:", team1.members)  # Team 1 members: ['Grace']
# print("Team 2 members:", team2.members)  # Team 2 members: []

# if team1.members is team2.members:
#     print("Object team1 and object team2 shares common list.")
# else:
#     print("Objects team1 and team2 has its own lists.")






#***********************************************************************************************
#  LAB 8             Part B -  Dictionary or class?                      *
#***********************************************************************************************


# Part B.1 Represent a movie using a dictionary with title, director and rating.
#-------------------------------------------------------------------------------

# movie = {
#     "title": "Tango & Cash",
#     "director": "Andrei Konchalovsky",
#     "rating": 7.2
# }

# print(f"Title: {movie['title']}")
# print(f"Director: {movie['director']}")
# print(f"Rating: {movie['rating']}")




# Part B.2 Represent the same information using a Movie class.
#-------------------------------------------------------------

# class Movie:
#     def __init__(self, title, director, rating):
#         self.title = title
#         self.director = director
#         self.rating = rating


# movie = Movie("Tango & Cash", "Andrei Konchalovsky", 7.2)

# print(f"Title: {movie.title}")
# print(f"Director: {movie.director}")
# print(f"Rating: {movie.rating}")




# Part B.3. Add a method to Movie that returns whether the movie is highly rated. 
#           Choose a sensible rating threshold.
#--------------------------------------------------------------------------------

# class Movie:
#     def __init__(self, title, director, rating):
#         self.title = title
#         self.director = director
#         self.rating = rating

#     def is_highly_rated(self):
       
#         return self.rating >= 8.0



# movie1 = Movie("Gladiator", "Ridley Scott", 8.8)
# movie2 = Movie("Tango & Cash", "Andrei Konchalovsky", 7.2)


# print(f"Is '{movie1.title}' highly rated? {movie1.is_highly_rated()}")  # True
# print(f"Is '{movie2.title}' highly rated? {movie2.is_highly_rated()}")  # False


# Part B.4 In comments, briefly explain one situatio where you would choose a dictionary 
#           and one where you would choose a class.
#---------------------------------------------------------------------------------------



    
#****************************************************************************************************
#  LAB 8                  PART C -   Inheritance fundamentals                                       *
#****************************************************************************************************


# C.1. Create a base class Account with owner and balance.
#-----------------------------------------------------------

# class Account:
#     def __init__(self, owner, balance):
#         self.owner = owner
#         self.balance = balance

  
# account = Account("Ada", 1000.0)
# print(f"Owner: {account.owner} | Balance: {account.balance}")





# C.2 Create SavingsAccount(Account) with an additional interest_rate attribute.
#--------------------------------------------------------------------------------

# class Account:
#     def __init__(self, owner, balance):
#         self.owner = owner
#         self.balance = balance


# class SavingsAccount(Account):
#     def __init__(self, owner, balance, interest_rate):
        
#         super().__init__(owner, balance)
        
#         self.interest_rate = interest_rate

#     def add_interest(self):
       
#         interest = self.balance * self.interest_rate
#         self.balance += interest
#         return interest



# spar = SavingsAccount("Ada", 1000.0, 0.05)
# print(f"Owner: {spar.owner} | Balance: {spar.balance} | Interest rate: {spar.interest_rate * 100}%")






# C.3 Use super() so SavingsAccount reuses the initialization from Account.
#-------------------------------------------------------------------------

# class Account:
#     def __init__(self, owner, balance=0.0):
#         self.owner = owner
#         self.balance = balance



# class SavingsAccount(Account):
#     def __init__(self, owner, balance=0.0, interest_rate=0.02):
       
#         super().__init__(owner, balance)
        
#         self.interest_rate = interest_rate


# savings = SavingsAccount("Ada", 1000.0, 0.05)

# print("\n --- Savings Account  ---\n")
# print(f"Owner: {savings.owner}")
# print(f"Status: {savings.balance}")
# print(f"Interest rate: {savings.interest_rate * 100}%\n")




# C.4 Create at least two objects and print their attributes.
#------------------------------------------------------------------------------------------------


# class Account:
#     def __init__(self, owner, balance=0.0):
#         self.owner = owner
#         self.balance = balance



# class SavingsAccount(Account):
#     def __init__(self, owner, balance=0.0, interest_rate=0.02):
       
#         super().__init__(owner, balance)
#         self.interest_rate = interest_rate


# savings1 = SavingsAccount("Ada", 11000.0, 0.05)
# savings2 = SavingsAccount("Bob", 50000.0, 0.03)


# print("--- Savings Account 1 ---   ")
# print(f"\nOwner: {savings1.owner}")
# print(f"Status: {savings1.balance} kr")
# print(f"Interest rate: {savings1.interest_rate * 100}%\n")


# print("--- Savings Account 2 ---")
# print(f"Owner: {savings2.owner}")
# print(f"Balance: {savings2.balance} kr")
# print(f"Interest rate: {savings2.interest_rate * 100}%\n")




# C.5 Write the "is-a" statement that explains why this inheritance relationship makes sense.


# class Account:
#     def __init__(self, owner, balance=0.0):
#         self.owner = owner
#         self.balance = balance


# class SavingsAccount(Account):
#     def __init__(self, owner, balance=0.0, interest_rate=0.02):
       
#         super().__init__(owner, balance)
#         self.interest_rate = interest_rate



# savings1 = SavingsAccount("Ada", 1000.0, 0.05)
# savings2 = SavingsAccount("Grace", 2500.0)  

# print("\n--- Savings Account 1 ---")
# print(f"Owner: {savings1.owner}")
# print(f"Balance: {savings1.balance}")
# print(f"Interest rate: {savings1.interest_rate * 100}%\n")

# print("--- Savings Account 2 ---")
# print(f"Owner: {savings2.owner}")
# print(f"Balance: {savings2.balance}")
# print(f"Interest rate: {savings2.interest_rate * 100}%\n")



#************************************************************************************************
#  LAB 8                PART D -  Inherited and subclass-specific behaviour                     *
#************************************************************************************************

# D.1 Create a base class Employee with name and a method get_information().
#-------------------------------------------------------------------------

# class Employee:
#     def __init__(self, name):
#         self.name = name

#     def get_information(self):
#         return f"\nEmployee: {self.name}\n"


# # Testiranje D.1 klase
# emp = Employee("Alice")
# print(emp.get_information())


# D.2 Create Developer(Employee) and add a method that only Developer has.
#-------------------------------------------------------------------------


# class Employee:
#     def __init__(self, name):
#         self.name = name

#     def get_information(self):
#         return f"Employee: {self.name}"



# class Developer(Employee):
#     def __init__(self, name, programming_language="Python"):
       
#         super().__init__(name)
#         self.programming_language = programming_language

    
#     def write_code(self):
#         return f"{self.name} is writing {self.programming_language} code."


# dev = Developer("Bob", "Python")

# print()
# print(dev.get_information())
# print(dev.write_code())
# print()



# D.3 Create another Employee subclass of your choice and give it its own subclass-specific method.
#--------------------------------------------------------


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



# D.4 Demonstrate that both subclasses can use inherited behaviour from Emplyee. 
#-----------------------------------------------------------------


# class Employee:         # Parent Class (Base Class)
#     def __init__(self, name, salary):
#         self.name = name
#         self.salary = salary

    
#     def get_details(self):          # Here we use inherited behaviour from Emplyee. 
#          return f"Employee: {self.name} | Salary: {self.salary:,.0f} kr"



# class Developer(Employee):   # subclass / Child Class
#     def __init__(self, name, salary, programming_language):
        
#         super().__init__(name, salary)   # Here we call constructor of Parent Class (Employee)
#         self.programming_language = programming_language



# class Manager(Employee):      # subclass / Child Class
#     def __init__(self, name, salary, department):
    
#         super().__init__(name, salary)  # Here, we call also constructor of Parent Class (Employee)
#         self.department = department



# dev = Developer("Ada", 55000, "Python")      # subclass object1
# mgr = Manager("Bob", 75000, "Engineering")   # subclass object2

# print()
# print(dev.get_details())  # Output: Employee: Ada | Salary: 75,000 kr
# print(mgr.get_details())  # Output: Employee: Bob | Salary:  95,000 kr


# print(f"\nDeveloper Language: {dev.programming_language}")
# print(f"Manager Department: {mgr.department}\n")


# D.5 Demonstrate that en Employee object cannot automatically use a method that only exists in one of its subclasses.
#-----------------------------------------------------------------------





#******************************************************************************************************
#  LAB 8              Part E -            super() and shared initialization                           *
#******************************************************************************************************


# E.1 Create a base class Device with brand and year.
#--------------------------------------------------------------

# class Device:
#     def __init__(self, brand, year):
#         self.brand = brand
#         self.year = year


# device = Device("Dell", 2023)
# print(f"Brand: {device.brand}, Year: {device.year}")





# E.2 Add useful shared initialization logic inside Device, for example validation that year cannot be 
#     negative and an attribute such as is_active =True.
#---------------------------------------------------------------------------




# E.3 Create Laptop(Device) with one additional attribute such as ram_gb. Use super().
#-------------------------------------------



# E.4 Create another Device subclass with its own additional attribute and use super() again.
#-------------------------------------------------------------------------------------------------


# E.5 Demonstrate that both subclasses receive the shared initialization logic from Device without duplicationg it.
#------------------------------------------------------------------------------




#*******************************************************************************************************
#  LAB 8                       Part F -  Method overriding                                             *
#*******************************************************************************************************


# F.1 Create a base class Notification with a method send() that returns a general message.
#----------------------------------------------------------------------------------



# F.2 Create EmailNotification(Notification) and SMSNotification(Notification).
#-----------------------------------------------------------------------------------------------------



# F.3 Override send() in both subclasses so each returns a different message.
#----------------------------------------



# F.4  Create one object from each class and call send() on all of them
#---------------------------------------------------



# F.5 Explain in a comment wich method is used when send() is called on each object.
#---------------------------------------------------------------------------------






#*******************************************************************************************************
#  LAB 8           Part G -  Override and still use the base method                                    *
#*******************************************************************************************************

# G.1 Create a base class Report with a mehod get_summary() that returns a general report summary.
#----------------------------------------------------------


# G.2 Create Salesreport(Report) and override get_summary().
#----------------------------------------------------------------------------------------


# G.3 Inside the overridden mehod, call the base inplementation using super() and add SalesReport-specifid information.
#----------------------------------------------------------------------------------------------------


# G.4 Create a Salesreport object and print the final result.
#------------------------------------------------------------------------------------------------------------





#*******************************************************************************************************
#  LAB 8           Part H -  Applied challenge: User accounts
#*******************************************************************************************************

# H.1 Build a small user account system using inheritance. 
#----------------------------------------------------------


# H.2 Create a base class User with at least username and email.
#----------------------------------------------------------------------------------------


# H.3 Add a useful method to User that all user types should ingerit.
#----------------------------------------------------------------------------------------------------


# H.4 Create AdminUser(User) and PremiumUser(User). Give each subclass at least one additional attribute and one subclass-specific method.
#------------------------------------------------------------------------------------------------------------




# H.5 Use super() in both subclasses instead of duplication User's initialization.
#---------------------------------------------------------------------------------------------



# H.6 Add one method to User and override it differently in Admin User and PremiumUser.
#-------------------------------------------------------------




# H.7 In one overridden method, use super() to reuse the base implementation and then extend it. )
#--------------------------------------------



# H.8 Create several objects and demonstrate inherited methods, subclass-specific methods and overridden methods.
#----------------------------------------------------------------------------------------


# H.9 Add at least one sensible validation using ValueError.
#----------------------------------------------------------------------------------------


# H.10 In comments, explain why AdminUser and PremiumUser have an "is-a" relationship with User.
#----------------------------------------------------------------------------------------





# **********************************  END of LAB 8  ********************************************************