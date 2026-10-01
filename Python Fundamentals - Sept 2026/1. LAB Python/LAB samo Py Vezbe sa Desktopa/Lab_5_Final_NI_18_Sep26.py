#********************************************************************************************
#  Novica Ivkovic                                                                           *
#  Cours: System Developer Python and AI                                                    *
#  September 15 2026  -  LAB 5                                                              *
#          Today's study goal is: Scope/local-global variables/*args/**kwargs               *                  
#********************************************************************************************

#*********************************************************************************************
#  LAB 5                         Part A - SCOPE                                              *         
#*********************************************************************************************


# Part A.1. Create a global variable course_name and a function that creates a local variable
#           with the same name.   Print both and explani the result.
#---------------------------------------------------------------------------------------------

# course_name = "System Developer Python and AI"

# def example_a1 (name):
#     course_name = name
#     print(course_name)
#     return course_name

# example_a1("Java")  # a local function
# print(course_name)  # a global function



# Part A.2. Create a function with a local counter and show that it does not remain 
#           available outside the function.
#----------------------------------------------------------------------------------

# def example_a2(number):
#     counter = 0
#     if number > 10:
#         counter += 10
#     else:
#         counter += 1
#     return number * counter

# test1 = example_a2(5)
# print(test1)             # 5 - OK (5*1=5)

# test2 = example_a2(5) + counter  # NameError: name 'counter' is not defined
# print(test2)



# Part A.3 Create a function that attemtpts to modify a global numeric variable without global.
#        Observe/describe the problen, then rewrite the design to return the new value instead.
#----------------------------------------------------------------------------------------------

# numer_global = 100

# def example_a3(number):
#     print(f"Before changing attempt: {numer_global}")
#     numer_global = number * number # UnboundLocalError: cannot access local variable 'numer_global'
#                                    #  where it is not associated with a value
#     print(f"After changing attempt: {numer_global}")
#     return numer_global

# temp = example_a3(1)
# print(f"After executing a function: {temp}")




# Part A.4 Create a nested function and demonstrate a simple enclosing - scope lookup.
#-------------------------------------------------------------------------------------

# def outside_function(name):
#     titel = "Welcome: "

#     def inside_function(surname):
#         return f"{titel} {name} {surname}"

#     return inside_function("Ivkovic")

# sentence = outside_function("Novica")
# print(sentence)




# Part A.5 Create examples that avoid shadowing built-ins such as lisst, str, sum and max.
#-----------------------------------------------------------------------------------------

## Shadowing efect is when we use pre-defined words/ reserved words like variables in our programs.

# my_number_list = [10, 20, 30, 40, 50]
# my_language = "Python"

# print()
# new_list = list(my_language)
# print("New list: ", new_list)

# number_to_string = str(100)
# print("Number transformed to string: ", number_to_string, "has now -", type(number_to_string))
# print()



#******************************************************************************************
#                              Part B - *args                                             *
#******************************************************************************************

# Part B.1 Write add_all(*numbers) returning the sum without sum().
#------------------------------------------------------------------

# def add_all(*numbers):
#     total = 0

#     for number in numbers:
#         total += number

#     return total

# print(add_all(1,2,3,4,5,6,7,8,9,10))


# Part B.2 Write average (*numbers). Decide what should happen when no numbers are supplied.
#-------------------------------------------------------------------------------------------

# def average_num(*numbers):
#     total = 0
#     counter = 0
#     for number in numbers:
#         total += number
#         counter += 1
#     if numbers == None:
#         print("You need to enter a number/numbers to average can be calculated!")
#     else:
#         average = total / counter
#     return average

# print(average_num(1,2,3,4,5,6,7,8,9,10,1000))
#--------------------------------
#

# Part B.3 Write longest_word(*words) returning the longest word.
#----------------------------------------------------------------

# def longest_word(*words):

#     longest_word = ""
  
#     for word in words:
#         longest_word += word 
        
#     return longest_word

# print(longest_word("Anna", " ", "likes", " ", "Bob", ", ", "but", " ", "he ", "doesn't"," care!"))



# Part B.4 Write build_sentence(separator, *words) returning one joined string.
#------------------------------------------------------------------------------

# def build_sentence(separator,*words):

#     sentence = ""
    
#     for word in words:
#         sentence += word
#         sentence += separator

#     #sentence = sentence - separator " TypeError: unsupported operand type(s) for -: 'str' and 'str'"  
#     separator_len = len (separator)           # These two lines remove the last separator
#     sentence = sentence[:-separator_len]
#     return sentence

# print(build_sentence(" ","Anna", "likes", "Bob", "but", "he", "doesn't", "care!"))
# print(build_sentence("*","Anna", "likes", "Bob", "but", "he", "doesn't", "care!"))   
# print(build_sentence("|","Anna", "likes", "Bob", "but", "he", "doesn't", "care!"))
# print(build_sentence("<=>","Anna", "likes", "Bob", "but", "he", "doesn't", "care!")) 
# print(build_sentence(" - ","Anna", "likes", "Bob", "but", "he", "doesn't", "care!"))     


# Part B.5 Write describe_scores(student_name, *scores) returning name, number of scores and average.
#----------------------------------------------------------------------------------------------------

# def describe_scores(student_name,*scores):

#     total = 0
#     counter= 0
#     average =0.0
    
#     for score in scores:
#         total += score
#         counter += 1
        
#     average = total / counter

#     return (student_name, counter, average)

# print(describe_scores("Anna", 5, 8, 6, 7, 3, 2, 9, 10)) # one way for output

# name, count, avg = describe_scores("Anna", 5, 8, 6, 7, 3, 2, 9, 10)

# print(f"Student: {name}")
# print(f"Amount of grades: {count}")
# print(f"Average grade: {avg}")



#***************************************************************************************************
#                           PART C - Positional unpackning                                         *
#***************************************************************************************************

# C.1. Create a list [10, 20, 30] and unpack it into a function expecting three positiona parameters.
#----------------------------------------------------------------------------------------------------

# my_list = [10, 20, 30]

# def print_my_list(a, b, c):
#     print(f"a={a} b={b}, c={c}")

# print_my_list(*my_list)


# C.2 Create a tuple containing first_name, last_name, city and call a function using *tuple.
#--------------------------------------------------------------------------------------------

# def create_persons_info(first_name, last_name, city): # OBS !!! Chek this again!
#     print(f"Name: {first_name}")
#     print(f"Lastname: {last_name}")
#     print(f"City: {city}")

#     person_info = ("Anna", "Ericsson", "Västerås")

#     create_persons_info(*person_info)


# C.3 Use starred assignment: first, *middle, last=values. Test with several list lengths.
#-----------------------------------------------------------------------------------------

# def unpackning(values):
#     first, *middle, last=values

#     print(f" first : {first}")
#     print(f" middle : {middle}")
#     print(f" last : {last}")

# unpackning([10,20,30,40,50])
# unpackning(["A","B", "B","A"])


# C.4 Explain in comments the difference between * in a function definition and * in a function call.
#----------------------------------------------------------------------------------------------------

# In a function definition (*) is in front of a parameter name and it packs multiple positional arguments 
#  passed by the caller into a single tuple.

# In a functional call, (*) precedes an iterable object (list, string, tupple).
# It unpacks the iterable into separate individual positional arbuments.



#************************************************************************************************
#                           PART D - **KWARGS  - **kwargs                                       *
#************************************************************************************************

# D.1 Write show_profile(**info) and iterate over all key/value pairs.
#---------------------------------------------------------------------

# def show_profile(**info):

#     for key, value in info.items():
#         print(key, ":",value)

# show_profile(
#     name = "Adam",
#     age = 27,
#     city = "New York",
#     language = "Python"
#  )



# D.2 Write create_user(username, **details) returning one dictionary containing username plus all supplied details.
#-------------------------------------------------------------------------------------------------------------------

# def create_user(username, **details):
#     print("Username:", username)

#     for key, value in details.items():
#         print(key, ":", value)

# create_user(
#     username = "adam123456",
#     age = 27,
#     city = "New York",
#     language = "Python"
#  )



# D.3 Write build_product(name, price, **metadata) returning a dictionary.
#-------------------------------------------------------------------------

# def build_product(name, price, **metadata):
#     print("name:", name)
#     print("price:", price)

#     for key, value in metadata.items():
#         print(key, ":", value)


# build_product(
#     name = "Tom",
#     price = 47000,
#     product = "car",
#     discount = 10,
#     available = True
# )


# D.4 Write a function that accepts ** settings and returns only settings whose value is not None.
#-------------------------------------------------------------------------------------------------

# def show_profile(**info4):

#     for key, value in info4.items():
#         if value is not None:
#             print(key, ":",value)

# show_profile(
#     name = "Adam",
#     age = 27,
#     city = None,
#     language = "Python"
# )



# D.5 Call a normal named-parameter function using **dictionary unpacking. Ensure dictionary keys match parameter names.
#-----------------------------------------------------------------------------------------------------------------------

# def unpack_profile(name, age, city, language):
#     print("Name: ", name)
#     print("Age: ", age)
#     print("City: ", city)
#     print("Language: ", language)
    
# show_profile = {
#     "name" : "Adam",
#     "age" : 27,
#     "city" : "Vaxholm",
#     "language" : "Python"
# }

# final_profil = unpack_profile(**show_profile)

# print(final_profil)



#****************************************************************************************************
#                           Part E - Combining parameters                                           *
#****************************************************************************************************


# E.1 Create log_event(event_type, *messages, **metadata) returning a structured dictionary.
#-------------------------------------------------------------------------------------------

# def log_event(event_type, *messages, **metadata):
#     print("Event type:", event_type)
#     print("Message: ", messages)
#     print("Metadata: ", metadata)


# log_event(
#     "Party",
#     101,
#     202,
#     404,
#     name = "Ada",
#     age = 25,
#     active = True
# )


# E.2 Create calculate_order(customer, *prices, **options). Support an optional discount and shipping fee in options.
#--------------------------------------------------------------------------------------------------------------------

# def calculate_order(customer, *prices, **options):
#     print("Customer: ", customer)
#     print("Price/discount: ", prices)
#     print("Options: ", options)

    
# calculate_order(
#     "Tom",
#     25000,
#     15,
#     product = "car",
#     shipping_fe = 5,
#     available = True
#     )



# E.3 Create a function where explicit named parameters would be clearer than **kwargs.
#     Write both version and compare readability in comments.
#--------------------------------------------------------------------------------------

# def calculate_order(**options):
#      print("Options: ", options) # Here we know that we are talking about options

# def calculate_order2(**kwargs):
#      print("Options: ", kwargs) # Here we do not know what we are talking about.



# E.4 Create at least three calls to the same flexible function with substantially different numbers of arguments.
#-----------------------------------------------------------------------------------------------------------------

# def calculate_order(customer, *prices, **options):
#     print("Customer: ", customer)
#     print("Price/discount: ", prices)
#     print("Options: ", options)

    
# calculate_order(
#     "Tom",
#     25000,
#     15,
#     product = "car",
#     shipping_fe = 5,
#     available = True
#     )

# calculate_order(
#     "Bob",
#     135000,
#     20,
#     product = "truck",
#     )

# calculate_order(
#     "Mery",
#     2000,
#     None,
#     product = "shoes",
#     available = True
#     )



#*********************************************************************************************
#                       Part F - Applied Challenge: Report builder                           *            
#*********************************************************************************************

# F.1 Build a flexible report system without files. create_raport(title, *sections, **metadata)
#      should return a dictionary.
#----------------------------------------------------------------------------------------------

# def create_raport(title, *sections, **metadata):
#     result = {
#         "Raport title": title,
#         "Sections": sections,
#         "Metadata" : metadata
#     }
#     return result

# raport = create_raport(
#     "Weather report",
#     10,
#     15,
#     20,
#     35,
#     75,
#     cloudy = "10%",
#     sunny = True,
#     raining = False,
#     windy = True     
#     )

# #print(raport)  # Raport is in one line

# # Next code allows to write the raport in multiple lines

# print(f"Report title: {raport['Raport title']}\n")

# print("Sections:")
# for section in raport["Sections"]:
#     print(f"  - {section}")

# print("\nMetadata:")
# for key, value in raport["Metadata"].items():
#     print(f"  - {key}: {value}")



# F.2 Each section can be a string or a small dictionary; chose and document your design.
#----------------------------------------------------------------------------------------

# F.3 Metadata may include author, department, version, confidential and date.
#-----------------------------------------------------------------------------



# F.4 Write summarize_report(report) that returns a readable multi-line string.
#------------------------------------------------------------------------------


 
 
# F.5 Write count_words(*section) that counts words across all supplied textual sections.
#----------------------------------------------------------------------------------------



# F.6 Use dictionary unpacking to create at least two reports from predefined metadata dictionaries.
#---------------------------------------------------------------------------------------------------




# F.7 Demonstrate at least one case where you function deliberately ignores or handles 
#      a missing optional metadata field.
#-------------------------------------------------------------------------------------





#*******************************************************************************************************
# Part G - Stretch challenges
#*******************************************************************************************************

# G.1 Write merge_settings(defaults, **overrides) returning a new dictionary without modifying defaults.
#-------------------------------------------------------------------------------------------------------



# G.2 Write call_summary(function_name, *args, **kwargs) returning a string describing what would be called.
#-----------------------------------------------------------------------------------------------------------




# G.3 Write a flexible statistics function that returns count, total average, min and max for  *numbers.
#     Implement the calculation manually where reasonable.
#-------------------------------------------------------------------------------------------------------
 
 
 
# G.4 Create five 'predict the output' scope questions and verify your predictions.
#----------------------------------------------------------------------------------

# **********************************  END of LAB 5  ********************************************************