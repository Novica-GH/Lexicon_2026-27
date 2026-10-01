#********************************************************************************************
#  Novica Ivkovic                                                                           *
#  Cours: System Developer Python and AI                                                    *
#  September 23 2026 - LAB 8                                                                *
#             Today's study goal is:           OOP - Part II                                *
#********************************************************************************************


#********************************************************************************************
#  LAB 8                  Part A -  OOP Part2 Mutable default arguments
#********************************************************************************************

# Part A.1. Create a BadTeam class with name and a default parameter member=[]. Add an add_member() method.
#------------------------------------------------------------------------------------------

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






# Part A.2. Create two BadTeam objects without providing a members list. Add a member to only one team and 
#           print both lists. Explain in a comment what happend.
#----------------------------------------------------------------
     
# class BadTeam:
    
#     def __init__(self, members=[]):
#         self.members = members


# team1 = BadTeam()  # two objects
# team2 = BadTeam()


# team1.members.append("Ada")


# print(f"Team 1 members: {team1.members}")   #  Team 1 members: ['Ada']
# print(f"Team 2 members: {team2.members}")   #  Team 2 members: ['Ada'] !!!





# Part A.3 Create a corrected Team class using None as the default value and create a new list inside __init__.
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
#---------------------------------------------------------------------


class Team:
    def __init__(self, members=None):
        
        if members is None:
            self.members = []
        else:
            self.members = members


team1 = Team()
team2 = Team()

team1.members.append("Ada")


print("Team 1 members:", team1.members)  # Team 1 members: ['Grace']
print("Team 2 members:", team2.members)  # Team 2 members: []

if team1.members is team2.members:
    print("Object team1 and object team2 shares common list.")
else:
    print("Objects team1 and team2 has its own lists.")






#***********************************************************************************************
#  LAB 8             Part B -  Dictionary or class?                      *
#***********************************************************************************************


# Part B.1 Represent a movie using a dictionary with title, director and rating.
#--------------------------------------------------------------------




# Part B.2 Represent the same information using a Movie class.
#----------------------------------------------------------------------------------------------------------



# Part B.3. Add a method to Movie that returns whether the movie is highly rated. Choose a sensible rating threshold.
#--------------------------------------------------------------------------------------




# Part B.4 In comments, briefly explain one situatio where you would choose a dictionary and one where you would choose a class.
#----------------------------------------------------------------------------------------------------




    
#****************************************************************************************************
#  LAB 8                  PART C -   Inheritance fundamentals                                       *
#****************************************************************************************************


# C.1. Create a base class Account with owner and balance.
#--------------------------------------------------------------------



# C.2 Create SavingsAccount(Account) with an additional interest_rate attribute.
#-----------------------------------------




# C.3 Use super() so SavingSccount reuses the initialization from Account.
#------------------------------------------------------------



# C.4 Create at least two objects and print their attributes.
#------------------------------------------------------------------------------------------------


# C.5 Write hte "is-s" statement that explains why this inheritance relationship makes sense.





#************************************************************************************************
#  LAB 8                PART D -  Inherited and subclass-specific behaviour                     *
#************************************************************************************************

# D.1 Create a base class Employee with name and a method get_information().
#-------------------------------------------------------------------------



# D.2 Create Developer(Employee) and add a method that only Developer has.
#-------------------------------------------------------



# D.3 Create another Employee subclass of your choice and give it its own subclass-specific method.
#--------------------------------------------------------



# D.4 Demonstrate that both subclasses can use inherited behaviour from Emplyee. 
#-----------------------------------------------------------------




# D.5 Demonstrate that en Employee object cannot automatically use a method that only exists in one of its subclasses.
#-----------------------------------------------------------------------





#******************************************************************************************************
#  LAB 8              Part E -            super() and shared initialization                           *
#******************************************************************************************************


# E.1 Create a base class Device with brand and year.
#--------------------------------------------------------------



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