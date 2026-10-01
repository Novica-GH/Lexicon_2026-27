#****************************************************************************
#   Novica Ivkovic                                                          *
#   Cours: System Developer Python and AI                                   *
#   September 14 2026 - Today's study goal is: FUNCTIONS                    * 
#                           - LAB 4 -                                       *
#****************************************************************************


#****************************************************************************
#  LAB 4                  Part A - Function fundamentals                    *          
#****************************************************************************

# Part A.1. Write functions greet(), show_course_name() and print_separator().
#           Call each more then once.
#----------------------------------------------------------------------------

# def greet():
#     print("Hello, World!")

# def show_course_name():
#     print("This is Python course.")


# def print_separator():
#     print("***___________________*** ")

# print_separator()
# greet()
# print_separator()
# show_course_name()
# print_separator()



# Part A.2. Write greet_person(name) and introduce (name, city)
#--------------------------------------------------------------     

# def greet_person(name): # Exempel function with input parameter (name)
#     print("Hello,", name)

# greet_person("Anna")

# def introduce(name, city):
#     print(f"{name} is from {city}.")

# introduce("Tom", "London")



# Part A.3 Write add(a, b), subtract(a,b), multiply(a,b) and divade(a,b).
#          Each must return a value.
#------------------------------------------------------------------------

# def add(a, b):
#     return a + b

# def subtract(a, b):
#     return a - b

# def multiply(a, b):
#     return a * b

# def divade (a, b):
#     if b != 0:
#         return a / b
#     else:
#         print("It is not allowed to divade with 0. Please enter another value for b parameter.")

# print(add(5,25))
# print(subtract(5,25))
# print(multiply(5,25))
# #print(divade(5,0))
# print(divade(5,25))



# Part A.4 Demonstrate parameter vs argument in comments using one of your functions.
#------------------------------------------------------------------------------------
  
# def greet_person(name): # When we define funktion, (name) is parameter
#     print("Hello,", name)

# greet_person("Anna")  # When we use funktion, we call it by argument, ie. "Anna" is an argument here.



# Part A.5 Create calculate_area(width, height) and use its returned value in another calculation.
#-------------------------------------------------------------------------------------------------         

# def calculate_area(width, height):
#     return width * height


# rec_1_w = int (input("Input widh dimensions for first rectangle: "))
# rec_1_h = int (input("Input height dimensions for first rectangle: "))
# rec_2_w = int (input("Input widh dimensions for second rectangle: "))
# rec_2_h = int (input("Input height dimensions for second rectangle: "))


# area_two_rectangles = calculate_area(rec_1_w, rec_1_h) + calculate_area(rec_2_w,rec_2_h)
# print(f"Area fpr two rectangles with dimensions: ({rec_1_w},{rec_1_h}) and ({rec_2_w},{rec_2_h}) is {area_two_rectangles}.")



#******************************************************************************************
#  LAB 4                            Part B - Return values                                *
#******************************************************************************************

# Part B.1 Write is_even(number) returning True/False.
#-----------------------------------------------------

# def is_even(number):
#     return (number % 2 == 0)

# x = int(input("input one number: "))

# if is_even(x): 
#     print(f" Number {x} is even number.")
# else:
#     print(f"Number {x} is odd number.")
 


# Part B.2 Write get_larger(a,b) returning the larger value without max().
#-------------------------------------------------------------------------

# def get_larger(a,b):  

#     if a == b:
#         print("You have entered two same numbers!")
#     elif a < b:
#         c = b
#     else:
#         c = a
#     return c

# def get_smaller(a,b):  # I need also this funktion, because I want to compare these two numbers att the end.
                       
#     if a == b:
#         print("You have entered two same numbers!")
#     elif a < b:
#         c = a
#     else:
#         c = b
#     return c

# a = int(input("Input one number: "))
# b = int(input("Input another number: "))

# print(f"{get_larger(a,b)} is larger than {get_smaller(a,b)}.")




# Part B.3 Write classify_score(score) returning PASS or FAIL.
#-------------------------------------------------------------

# scores = [85, 55, 75, 95, 59, 68]  # OBS - Check one more time
# print(scores[2])
# print(type(scores[2]))

# def classify_score(score):
#     if scores[score] >= 70:      
#         return "PASS"
#     return "FAIL"

# for index in scores:
#     status = classify_score(index)
#     print(scores[index], status)



# Part B.4 Write full_name(first_name, last_name) returning a formatted string.
#------------------------------------------------------------------------------

# def full_name(first_name, last_name):
#     clean_first = first_name.strip()
#     clean_last = last_name.strip()
#     return f"{clean_first} {clean_last}"

# name = full_name("  Adam  ", "Smith   ")
# print(f"Formatted name is: ", {name})



# Part B.5 Write calculate_disciount(price, percent) returning the discounted price.
#-----------------------------------------------------------------------------------

# def calculate_disciount(price, percent):
#     discount = price * (percent / 100)
#     final_price = price - discount
#     return final_price


# Part B.6 Show with a small example why print(result) inside a function is not the same as return result.
#---------------------------------------------------------------------------------------------------------

# def add_with_print(a, b):   
#     print(a+b)                 # Function write 8, byt it doesn't return 8 (value of function)

# result = add_with_print(5,3)
# print("Result: ", r'esult)      # Here we have: Result:  None, because funktion doesn't have return value (Result:  None)
#-------------------------------------

# def add_with_print(a, b):   
#      return a + b                 # Function write returns value here

# result = add_with_print(5,3)
# print("Result: ", result)        # And here we have a value flr result (Result:  8)



#*************************************************************************************
#  LAB 4                 PART C - Defaults and keyword arguments                     *
#***************/*********************************************************************

# C.1. Create greet(name, greeting='Hello'). Test positional and keyword arguments.
#----------------------------------------------------------------------------------

# def greet(name, greeting='Hello'):
#     return f"{greeting}, {name}"

# print(greet("Novica"))
# print(greet("Stefan", "Hello"))
# print(greet(greeting="Ciao", name="Antonio"))
# print(greet("Anastasia", greeting="Wellcome!"))
# print(greet(greeting="Zdravo"))  # OBS - ERROR-TypeError: greet() missing 1 required positional argument: 'name'



# C.2 Create calculate_price(price, quantity=1, discount=0). Return the final total.
#-----------------------------------------------------------------------------------

# def calculate_price(price, quantity=1, discount=0):
#     total = price * quantity
#     dicsount_total = total * (discount / 100)
#     final_total = total - discount_total
#     return final_total


# C.3 Create create_profile(name, city='Unknown', active=True) returning a dictionary.
#-------------------------------------------------------------------------------------

# def  create_profile(name, city='Unknown', active=True):
#     return {
#         "name": name.strip(),
#         "city": city.strip(),
#         "active": active
    # }



# C.4 Call one function using keyworid arguments in a different order from the parameter definition.
#---------------------------------------------------------------------------------------------------

# def  create_profile(name, city='Unknown', active=True):
#     return {
#         "name": name,
#         "city": city,
#         "active": active
#         }

# profile = create_profile(active=False, name="Novica", city="Stockholm")
# print(profile)



# C.5 Write one invalid default-parameter ordering as a comment and explain why it is invalid.
#---------------------------------------------------------------------------------------------

# def greet(greeting='Hello', name):  # SyntaxError: parameter without a default follows parameter with a default
#       return f"{"name":name, "greeting":greeting}



#***************************************************************************************
#   LAB 4                    PART D - Functions and collections                        *
#***************************************************************************************

# D.1 Write calculate_total(numbers) manually using a loop.
#----------------------------------------------------------

# def calculate_total(numbers):
#     total = 0
#     for number in numbers:
#         total += number 
#     return total

# my_numbers = [1,5,27,35,95,7,6]

# print (f"Total sum is: ", calculate_total(my_numbers))


# D.2 Write count_even(numbers).
#-------------------------------

# def count_even(numbers):
#     count = 0
#     for number in numbers:
#         if number % 2 == 0:
#             count += 1     
#     return count

# my_numbers = [1,5,8,15,22,30,2]
# even_count = count_even(my_numbers)
# print(f"Total even numers is: {even_count}")


# D.3 Write get_long_words(words, minimum_length) returning a new list.
#----------------------------------------------------------------------

# def get_long_words(words, minimum_length):
#     long_words = []
#     for word in words:
#         if len(word) >= minimum_length:
#             long_words.append(word)
#     return long_words

# my_words = ["Python", "Java", "Stockholm", "Programming", "Mathematic", "C++", "Yes", "No"]
# mini_len = 5

# long_words = get_long_words(my_words, mini_len)

# print(f"Original list: {my_words}")
# print(f"Long words list: {long_words}")



# D.4 Write find_student(students, name) where students is a list of dictionaries. 
#     Return the matching dictionary or None.
#---------------------------------------------------------------------------------

# def find_student(students, name):
#     wanted_name = name.strip().lower()

#     for student in students:
#         if student.get("name", "").strip().lower() == wanted_name:
#             return student
#     return None


# my_students = [                           
#     {"name": "Anna", "score": 85},     
#     {"name": "Ava", "score": 55},
#     {"name": "Mike", "score": 75},
#     {"name": "Luckas", "score": 95},
# ]

# student_1 = find_student(my_students, "Anna")
# print("Result after searching: ", student_1)

# student_2 = find_student(my_students, "Novica")
# print("Result after searching: ", student_2)



# D.5 Write average_score(students) for a list of dictionaries containing score values.
#--------------------------------------------------------------------------------------

#  def average_score(students):  # I am going to finish this during the weekend, 
                                 # I am going now to the next part E 
#     if not students:
#        return 0

#     total_score = 0
#     count = 0

#     for student in students:
#         if "score" in student and :
#             return student
#     return None


# my_students = [                           
#     {"name": "Anna", "score": 85},     
#     {"name": "Ava", "score": 55},
#     {"name": "Mike", "score": 75},
#     {"name": "Luckas", "score": 95},
# ]

# student_1 = find_student(my_students, "Anna")
# print("Result after searching: ", student_1)
#OBS!



# D.6 Write get_active_users(users) returning only dictionaries where active is True.
#------------------------------------------------------------------------------------




#*************************************************************************************
#    LAB 4                Part E - Decomposition                                     *                  
#*************************************************************************************


# E.1 Build a temperature raport using separate functions for Celsius-to-Fahrenheit 
#     conversion, classification ('cold/warm/hot') and formatting.
#----------------------------------------------------------------------------------

# def celsius_to_fahrenheit(celsius):
#     return round((celsius * 9 / 5) + 32, 1)

# def temperature_klasifikation(celsius):    
#     if celsius < 10:
#         return "cold"
#     elif celsius <= 35:
#         return "warm"
#     else:
#         return "hot"

# import_data = [
#     {"city": "Stockholm", "temperature": 15},     
#     {"city": "Belgrade", "temperature": 25},
#     {"city": "Vaxholm", "temperature": 14},
#     {"city": "Oslo", "temperature": 10},
#     {"city": "London", "temperature": 16}
# ]

# rapport_data = []
#     # Exempel:{"cityR": "Stockholm", "temperatureC": 15, "temperatureF": 59, "klasa": "warm"},

# for item in import_data: 
#     city = item["city"]
#     temperature = item["temperature"]

#     temperatureF = celsius_to_fahrenheit(temperature)
#     klasa = temperature_klasifikation(temperature)

#     row = {
#         "city": city,
#         "temperature_Celsius": temperature,
#         "temperature_Fahrenheit": temperatureF,
#         "status": klasa
#     }   
#     rapport_data.append(row)

# for row in rapport_data:
#     print(row)



# E.2 Build a small order calculation using separate functions for subtotal, discount and final total.
#-----------------------------------------------------------------------------------------------------

# def calculate_subtotal(order_items):
#     subtotal = 0.0
#     for item in order_items:
#         subtotal += item["price"] * item["quantity"]
#     return subtotal


# def calculate_discount(subtotal, discount_percentage):
#     return subtotal * (discount_percentage / 100)


# def calculate_final_total(subtotal, discount_amount, tax_rate=0.10):
#     amount_after_discount = subtotal - discount_amount
#     tax = amount_after_discount * tax_rate
#     return amount_after_discount + tax



# catalog = [
#     {"name": "Laptop", "price": 800.0, "quantity": 3},
#     {"name": "Mouse", "price": 25.0, "quantity": 20},
#     {"name": "Keyboard", "price": 50.0, "quantity": 15}
# ]

# subtotal = calculate_subtotal(catalog)
# discount = calculate_discount(subtotal, discount_percentage=15)  # 25% discount
# final_total = calculate_final_total(subtotal, discount, tax_rate=0.25)  # 25% tax

# print(f"\nSubtotal:     {subtotal:.2f} kr")
# print(f"Discount:    - {discount:.2f} kr")
# print(f"Final Total:  {final_total:.2f} kr\n")



# E.3 Refactor one earlier excersise that contains repeated code into at least three functions.
#---------------------------------------------------------------------------------------------
#    LAB 3              Part G - Applied  challenge: Console study tracker       

# study_sessions = [
#     {"subject": "Python Programming", "minutes": 45},
#     {"subject": "Mathematics", "minutes": 60},
#     {"subject": "Database Systems", "minutes": 30},
#     {"subject": "Python Programming", "minutes": 90},
#     {"subject": "Web Development", "minutes": 50},
#     {"subject": "Mathematics", "minutes": 40},
#     {"subject": "Data Structures", "minutes": 75},
#     {"subject": "Python Programming", "minutes": 60},
#     {"subject": "Operating Systems", "minutes": 45},
#     {"subject": "Web Development", "minutes": 35}
# ]

# def calculate_total_minutes(sessions):
#     return sum(session["minutes"] for session in sessions)


# def calculate_subject_totals(sessions):
#     totals = {}
#     for session in sessions:
#         subject = session["subject"]
#         totals[subject] = totals.get(subject, 0) + session["minutes"]
#     return totals


# def filter_long_sessions(sessions, limit_minutes=45):
#     return [session for session in sessions if session["minutes"] > limit_minutes]


# total_minutes = calculate_total_minutes(study_sessions)
# by_subject = calculate_subject_totals(study_sessions)
# long_sessions = filter_long_sessions(study_sessions, limit_minutes=45)

# # Output results
# print(f"\nTotal Study Time: {total_minutes} minutes")
# print("Total minutes per Subject:", by_subject)
# print(f"Sessions longer than 45 minutes: {len(long_sessions)} found\n")


# E.4 Write a main-like section at the bottom of the file that calls your functions in a clear sequence.
#-------------------------------------------------------------------------------------------------------




#*******************************************************************************************************
#    LAB 4         Part F - Applied challenge: Event registration processor                            *
#*******************************************************************************************************


# F.1 Create functions to normalize a participant name, validate an age range using boolean return values, 
#     calculate a registration fee based on age/student status, and create a participant dictionary.
#--------------------------------------------------------------------------------------------------------- 

# def normalize_name(name):
#     return name.strip().title()


# def validate_age(age, min_age=18, max_age=67):
#     if (type(age) == int) and (min_age <= age <= max_age):
#         return True


# def calculate_fee(age, is_student):
#     if age < 18 or is_student:
#         return 15.0     
#     elif age >= 60:
#         return 10.0     
#     return 25.0         # Standard registration fee


# def create_participant(p_name, age, is_student=False):
#     if not validate_age(age):
#         return None     # Registration invalid if age check fails
        
#     normalized = normalize_name(p_name)
#     fee = calculate_fee(age, is_student)
    
#     return {
#         "name": normalized,
#         "age": age,
#         "is_student": is_student,
#         "fee": fee
#     }


# # A few participants:
# p1 = create_participant("   Anna Lind  ", 45, is_student=False)
# p2 = create_participant("Peter Lundgren ", 21, is_student=True)
# p3 = create_participant("invalid user", 17)  # Fails age check (under 18)
# p4 = create_participant("  Magnus Bergström ", 72, is_student=False)
# p5 = create_participant("  Eva Bergström ", 70, is_student=True) # Test for senior student

# print("Participant 1:", p1)
# print("Participant 2:", p2)
# print("Participant 3:", p3)
# print("Participant 4:", p4)
# print("Participant 5:", p5)



# F.2 Create at least eight participant dictionaries using your functions.
#-------------------------------------------------------------------------




# F.3 Write a function that receives the participant list and returns the total expected registration revenue.
#-------------------------------------------------------------------------------------------------------------
 



# F.4 Write a function that returns only student participants.
#------------------------------------------------------------
 



# F.5 Write a function that returns the oldest participant. 
#----------------------------------------------------------
 



# F.6 Write a function that creates a readable summary string for one participant. 
#---------------------------------------------------------------------------------




# F.7 Keep input/output responsibilities separate from calculation functions as much as possible.
#------------------------------------------------------------------------------------------------




#*******************************************************************************************************
#    LAB 4                       Part G - Stretch challenges                                           *
#*******************************************************************************************************



# G.1 Write a function that returns both minimum and maximum from a list 
#     without min()/max(). Return two values.
#-----------------------------------------------------------------------



# G.2 Write a function that checks whether a worid is a palindrome.
#-------------------------------------------------------------------



# G.3 Write a function that counts character frequencies and returns a dictionary.
#---------------------------------------------------------------------------------
 
 
 
# G.4 Write a function that receives a list of numbers and returns a new dictionary 
#     with keys positive, negative and zero containing counts.
#----------------------------------------------------------------------------------
# G.5 Add light type hints and a short docstring to at least five functions.
#---------------------------------------------------------------------------



#*****************************  END - LAB 4  ****************************************