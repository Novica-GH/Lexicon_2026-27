#****************************************************************************************************
#  Novica Ivkovic                                                                                   *
#  Cours: System Developer Python and AI                                                            *
#  September 9 2026 - LAB 2                                                                         *
#    Today's study goal is: Collections: Lists / Tuples / Sets / Dictionaries /Nested collections   *
#****************************************************************************************************


#****************************************************************************************************
#   LAB 2                             Part A - Lists
#****************************************************************************************************


# A.1. Create a list of at least eight programming languages. Acces the first, last, third 
#      and secont-to-last values.
#-----------------------------------------------------------------------------------------

# prog_languages = [ "Ada", "Basic", "C", "C++", "C#", "Cobol", "Fortran", "Pascal"]
# print(prog_languages)
# print(prog_languages[0])
# print(prog_languages[-1])
# print(prog_languages[2])
# print(prog_languages[-3])

           

# A.2. Print three defferent slices of the list, then print the list in reverse order using slicing.
#---------------------------------------------------------------------------------------------------

# prog_languages = [ "Ada", "Basic", "C", "C++", "C#", "Cobol", "Fortran", "Pascal"]

# print(prog_languages[:5])
# print(prog_languages[1:4])
# print(prog_languages[6:])
# print(prog_languages[::-1])



# A.3. Use append, insert, remove and pop. After each operation, print the list so the change is visible.
#-------------------------------------------------------------------------------------------------------

# prog_languages = [ "Ada", "Basic", "C", "C++", "C#", "Cobol", "Fortran", "Pascal"]

# prog_languages.append("PL/1")
# print(prog_languages)

# prog_languages.insert(1,"Visual Basic")
# print(prog_languages)

# prog_languages.remove("Basic")
# print(prog_languages)

# prog_languages.pop()
# print(prog_languages)

# prog_languages.pop()
# print(prog_languages)



# A.4. Create a numerical list. Calculate its length, minimum, maximum and sum using built-in functions.
#-------------------------------------------------------------------------------------------------------

# numbers = [1, 3, 5, 7, 9, 11]
# print(numbers)
# length = len(numbers)
# minimum = min(numbers)
# maximum = max(numbers)
# summa = sum(numbers)
# print(length, minimum, maximum, summa)



# A.5. Sort one list ascending and another descending. Explain in a comment the difference between 
#       chnanging a list with. sort() and creating a sorted result with sorted().
#-------------------------------------------------------------------------------------------------

# list_1 = [1, 4, 2, 7, 9, 5]
# list_1.sort()
# print (f"Ascending (list_1): {list_1}")

# list_2 = [11,33,52,95,14,8,65]
# desc_list_2 = sorted(list_2, reverse=True)
# print(f"Descending (list_2): {desc_list_2}")
# print(f"Original list_2 remain unchanged: {list_2}")

# Explanation of the difference between .sort() and sorted():
# .sort() method modifies the original list, while sorted() leaves the origina list completely unchanged.



# A.6. Demonstrate the reference/copy issue using list_b = list_a. Then fix it with .copy().
#-------------------------------------------------------------------------------------------

#Reference
# list_a = [1, 4, 2, 7, 9, 5]
# print("Reference method:")
# print(f"Original list_a: {list_a}")
# list_b = list_a  # in this moment both lists points to the same list in memory

# list_b.append(10)
# print (f"list_a after append in reference version: {list_a}")
# print(f"list_b after append in reference version: {list_b}")
# print()

# #Copy
# list_a = [1, 2, 6, 3, 5]
# print("Copy method:")
# print(f"Original list_a: {list_a}")
# list_b = list_a.copy()  # in this moment list_b take a new place in memory

# list_b.append(20)
# print (f"list_a after append in copy version: {list_a}")
# print(f"list_b after append in copy version: {list_b}")



#*************************************************************************************************
#   LAB 2                       Part B - Tuples and unpacking                                    *
#*************************************************************************************************

# B.1 Create a tuple representing RGB values. Unpack it into three variables and print them.
#-------------------------------------------------------------------------------------------

# rgb = ("red", "green", "blue")

# r, g, b = rgb

# print(r)
# print(g)
# print(b)



# B.2 Create a tuple containting a person's name, age and city. Unpack and use the values in a formatted sentence.
#-----------------------------------------------------------------------------------------------------------------

# person = ("Adam", 33, "Stockholm")

# name, age, city = person

# print(f"Citizen {name} {age} years old, lives in {city}.")



# B.3 Attempt to reason about changing one tuple element. Explain in a comment why tuples are useful
#      when values should not be changed.
#---------------------------------------------------------------------------------------------------

# person = ("Adam", 33, "Stockholm")
# person[0] = "Tom"  # => TypeError: 'tuple' object does not support item assignment

# Why tuples are useful when values should not be changed?

# 1. Data protection - Immutability helps with data integrity.
# 2. System performance - Because we alreadu know that tuples are immutable, that means that Python
#                         is going to allocate a fixed memory size for them(tuples)
# 3. Wery clear code - Like Alladin said - tuples are very Pythonic - I translate this like user friendly.



# B.4 Create a list containing at least four coordinate tuples such as (10, 20). 
#      Access iondividual x and y values.
#-------------------------------------------------------------------------------

# list_of_pairs = [(10, 20), (30, 40), (50, 60), (70, 80)]

# first_pair = list_of_pairs[0]  # This is first tuple in the list
# print(f"This is the first pair in the list: {first_pair}")
# print()

# x1 = list_of_pairs[0][0]       # This is the first coordinate from the first tuple in the list.
# y1 = list_of_pairs[0][1]       # This is the second coordinate from the first tuple in the list.

# print(f"The first point in the list has coordinates: x = {x1} and y = {y1}.")
 
# x2, y2 = list_of_pairs[1]  # This is the other way how we can reach the individual x and y values.

# print(f"The second point in the list has coordinates: x = {x2} and y = {y2}.") 

# print(f"\n--- All coordinates in the list ---")
# for index, (x,y) in enumerate(list_of_pairs, start=1):
#     print(f"The point {index}: x-axis = {x}, y-axis ={y}")




#********************************************************************************************************
#   LAB 2                               Part C - Sets                                                   *
#********************************************************************************************************

# C.1 Create a list containing duplicate course names. Convert it to a set and compare the lengths before and after.
#-------------------------------------------------------------------------------------------------------------------

# courses = [
#     "Python Programming",
#     "AI",
#     "Python Programming",
#     "Machine Learning",
#     "SQL",
#     "Machine Learning",
#     "SQL"
# ]

# print(courses)

# unique_courses = set(courses)
# print(unique_courses)

# list_length = len(courses)
# set_length = len(unique_courses)
# duplicates_removed = list_length - set_length

# print(f"Original list length: {list_length}")
# print(f"Unique set length   : {set_length}")
# print(f"Duplicates removed  : {duplicates_removed}")



# C.2 Create two sets representing skills of two developers. Find skills they share, 
#       skills only the first has, and all skills represented by either person.
#-----------------------------------------------------------------------------------

# developer1_skills = {"Python", "SQL", "Git", "Java", "Machine Learning"}
# developer2_skills = {"Java", "SQL", "C", "C#", "Linux", "C++"}

# shared_skills = developer1_skills.intersection(developer2_skills)  # Or d1 & d2 - both have the samme skills
# print(f"Shared skils: {shared_skills}")

# developer1_diff2 = developer1_skills.difference(developer2_skills) # Or d1 - d2 (Just d1 has this skills)
# print(f"Skils that just developer 1 has: {developer1_diff2}")

# all_skils = developer1_skills.union(developer2_skills) # Or d1|d2 - Unija skupova
# print(f"All skills for both developers: {all_skils}")


# C.3. Create a set and practice add, remove/discard and membership testing.
#---------------------------------------------------------------------------

# bas_set = {"Python", "SQL", "Git", "Java", "Machine Learning"}
# print(f"Original set: {bas_set}")


# C.4 Explain in comments why a set is a better shoice than a list for one real-world uniqueness problem.
#-------------------------------------------------------------------------------------------------------



#****************************************************************************************************
#  LAB 2                            Part D - Dictionaries                                           *
#****************************************************************************************************

# D.1 Create a dictionary for a laptop with brand, RAM, storage and price. 
#     Read every value by key.
#-------------------------------------------------------------------------

# laptop = {
#     "Brand": "Lenovo",
#     "RAM": "16GB",
#     "Storage": "512GB SSD",
#     "Price": 7000
# }

# brand = laptop["Brand"]
# ram = laptop["RAM"]
# storage = laptop["Storage"]
# price = laptop["Price"]

# print(f"Brand  : {brand}")
# print(f"RAM    : {ram}")
# print(f"Storage: {storage}")
# print(f"Price  : {price} kr")

# D.2 Uppdate the price , add an operating_system key and remove one key.
#-----------------------------------------------------------------------

# laptop = {
#     "Brand": "Lenovo",
#     "RAM": "16GB",
#     "Storage": "512GB SSD",
#     "Price": 7000
# }

# laptop["Price"] = 8500  # change of price

# laptop["Operating_system"] = "Windows 11" # Adding new key

# del laptop["Storage"] # Or laptop.pop("Storage") - deleting one key in dictionary

# print(laptop)


# D.3 Use .get() for both en existing and a missing key. 
#     Compare it conecepyually with direct indexing.
#--------------------------------------------------------

# laptop = {
#     "Brand": "Lenovo",
#     "RAM": "16GB",
#     "Storage": "512GB SSD",
#     "Price": 7000
# }

# brand = laptop.get("Brand")
# print(brand) # => Lenovo

# operating_sys = laptop.get("Operating_system")
# print(operating_sys) # => None


# D.4  Print keys, values and items separately.
#----------------------------------------------

# laptop = {
#     "Brand": "Lenovo",
#     "RAM": "16GB",
#     "Storage": "512GB SSD",
#     "Price": 7000
# }

# print("\n*****  KEYS  *****")
# for key in laptop.keys():
#     print(key)

# print("\n*****  VALUES  *****")
# for value in laptop.values():
#     print(value)

# print("\n*****  ITEMS  *****")
# for key, value in laptop.items():
#     print(f"{key}: {value}")


# D.5. Create a dictionary mapping five course names to number of study hours. 
#      Calculate the total hours using the dictionaty values.
#----------------------------------------------------------------------------





#****************************************************************************************************
#   LAB 2                       Part E - Nested collections                                         *
#****************************************************************************************************

# E.1 Create a list of at least five dictionaries representing books with 
#     title, author, pages and available.
#--------------------------------------------------------------------------

# books = [
#     {
#         "title": "The Bridge Over the Drina",
#         "author": "Ivo Andric",
#         "pages": 450,
#         "available": True
#     },
#     {
#         "title": "1984",
#         "author": "George Orwell",
#         "pages": 328,
#         "available": False
#     },
#     {
#         "title": "All Quiet on the Western Front",
#         "author": "Erih Marija Remark",
#         "pages": 227,
#         "available": True
#     },
#     {
#         "title": "War and Peace",
#         "author": "Leo Tolstoy",
#         "pages": 1300,
#         "available": True
#     },
#     {
#         "title": "Sanning med modifikation",
#         "author": "Sara Lövestam",
#         "pages": 256,
#         "available": False
#     }
# ]
# # E.2  Access the title of the third book and the availability of the last book.
# #-------------------------------------------------------------------------------

# third_book_title = books[2]["title"]
# last_book_availability = books[-1]["available"]

# print(f"\nTitle of the 3rd book    : {third_book_title}\n")
# print(f"Availability of last book: {last_book_availability}\n")



# # E.3 Change one nested value and add a new key to one book.
# #-----------------------------------------------------------

# # Change a nested value: For exempel - set availability of 4th book ('War and Peace') to False
# books[3]["available"] = False

# books[0]["published year"] = 1945

# print("Updated 4th book:", books[3])
# print(f"\nUpdated 1st book: {books[0]}\n")



# # E.4 Create a dictionary where each key is a department and 
# #     each value is a list of employee names.
# #-------------------------------------------------------------

# statistical_departments_ikt = {
#     "System Programming": ["Nada", "Tanja", "Voja", "Ksenija", "Novica"],  # Voja and Tanja, the best, always!!!
#     "Data Base": ["Mira", "Sanja", "Natasha", "Milan", "Gavrilo"],
#     "Project and Analys": ["Nada", "Olivera", "Ljiljana","Snezana"],
#     "Web Programming": ["Jelena", "Olja", "Aleksandar","Rastko", "Ivana"],
#     "System and Technical Support": ["Misha", "Milan", "Dusan", "Dusanka"],
#     "Print and Publication": ["Aleksandra", "Ivana", "Gordana", "Branislav", "Gaja", "Vladan", "Petar"]
# }

# print("\n=== STATISTICAL IKT  DEPARTMENTS ===\n")
# for depart, employees in statistical_departments_ikt.items():
#     names = ", ".join(employees)
#     print(f"{depart:<30}: {names}")
# print()



# # E.5 Create a structure for  three courses where each course contains a name,
# #     teacher and list o topics. Print one specific topis using chainded indexing.
# #-------------------------------------------------------------------------

# courses = [
#     {
#         "name": "Python Programming",
#         "teacher": "Aladdin",
#         "topics": ["Variables & Types", "Data Structures", "OOP", "File I/O"]
#     },
#     {
#         "name": "Machine Learning Fundamentals",
#         "teacher": "Haitem",
#         "topics": ["Supervised Learning", "Regression", "Clasification", "Data Cleaning"]
#     },
#     {
#         "name": "Database Systems",
#         "teacher": "Aladdin and Haitem",
#         "topics": ["SQL Queries", "SQL View", "Rational Databases"]
#     }
# ]

# course_topics = courses[2]["topics"]

# print(f"\nOne specific topis using chainded indexing: {course_topics}\n")




#************************************************************************************************
#   LAB 2                       Part F - Nested collections                                     *
#************************************************************************************************

# F.1 Create a catalogue containing at least eight movies, games or books. 
#     Each item must be a dictionary with at least four useful fields.
#------------------------------------------------------------------------

# catalogue = [
#     {
#         "title": "The Bridge Over the Drina",  # High school
#         "author": "Ivo Andric",
#         "pages": 450,
#         "available": True
#     },
#     {
#         "title": "1984",                # During the studies
#         "author": "George Orwell",
#         "pages": 328,
#         "available": False
#     },
#     {
#         "title": "All Quiet on the Western Front", # During the studies
#         "author": "Erih Marija Remark",
#         "pages": 227,
#         "available": True
#     },
#     {
#         "title": "War and Peace",           # High school
#         "author": "Leo Tolstoy",
#         "pages": 1300,
#         "available": True
#     },
#     {
#         "title": "Sanning med modifikation", # SFI memories...
#         "author": "Sara Lövestam",
#         "pages": 256,
#         "available": False
#     },
#     {
#         "title": "The Great Gatsby",        # SAS3 memories...
#         "author": "F. Scott Fitzgerald",
#         "pages": 180,
#         "available": True
#     },
#     {
#         "title": "Crime and Punishment",    # High school
#         "author": "Fyodor Dostoevsky",
#         "pages": 671,
#         "available": False
#     },
#     {
#         "title": "The Count of Monte Cristo",  # Primary school
#         "author": "Alexandre Dumas",
#         "pages": 1276,
#         "available": True
#     }
# ]


# # F.2 Store all item dictionaries in one list.
#-----------------------------------------------

# book1 = {"title": "The Bridge Over the Drina", "author": "Ivo Andric", "pages": 450, "available": True}
# book2 = {"title": "1984", "author": "George Orwell", "pages": 328, "available": False}
# book3 = {"title": "All Quiet on the Western Front", "author": "Erih Marija Remark", "pages": 227, "available": True}
# book4 = {"title": "War and Peace", "author": "Leo Tolstoy", "pages": 1300, "available": True }
# book5 = {"title": "Sanning med modifikation", "author": "Sara Lövestam", "pages": 256, "available": False}
# book6 = {"title": "The Great Gatsby", "author": "F. Scott Fitzgerald", "pages": 180, "available": True}
# book7 = {"title": "Crime and Punishment", "author": "Fyodor Dostoevsky", "pages": 671, "available": False}
# book8 = {"title": "The Count of Monte Cristo", "author": "Alexandre Dumas", "pages": 1276, "available": True}

# list_books = [book1, book2, book3, book4, book5, book6, book7, book8]


# # F.3 Create a set containing all unique categories/genres represented in the catalogue.
#-----------------------------------------------------------------------------------------

# set_of_unique_genres = {item["author"] for item in list_books if "author" in item }
# print(set_of_unique_genres)



# # F.4 Create a tuple for each item's immutable identifier plus release year,
# #     and include or associate it sensibly in your design.
#-------------------------------------------------------------------------------

# release_years = [1945, 1949, 1929, 1869, 2015, 1925, 1866, 1844]

# for i, book in enumerate(list_books):
#     book["id_and_year"] = (book["title"], release_years[i])
# # test
# print(f"\n{list_books[0]}\n")



# # F.5 Perform at least ten manual retrieval/update operations that demonstrate 
# #     nested indexing, membership and collection methods.
#-------------------------------------------------------------------------------

# list_books_manualy =[
#     {"title": "The Bridge Over the Drina", "author": "Ivo Andric", "pages": 450, "available": True},
#     {"title": "1984", "author": "George Orwell", "pages": 328, "available": False},
#     {"title": "All Quiet on the Western Front", "author": "Erih Marija Remark", "pages": 227, "available": True},
#     {"title": "War and Peace", "author": "Leo Tolstoy", "pages": 1300, "available": True },
#     {"title": "Sanning med modifikation", "author": "Sara Lövestam", "pages": 256, "available": False},
#     {"title": "The Great Gatsby", "author": "F. Scott Fitzgerald", "pages": 180, "available": True},
#     {"title": "Crime and Punishment", "author": "Fyodor Dostoevsky", "pages": 671, "available": False},
#     {"title": "The Count of Monte Cristo", "author": "Alexandre Dumas", "pages": 1276, "available": True},
#     {"title": "The Count of Monte Cristo2", "author": "Alexandre Dumas", "pages": 276, "available": False},
#     {"title": "The Count of Monte Cristo3", "author": "Alexandre Dumas", "pages": 76, "available": True}
# ]

# number_of_pages = list_books_manualy[3]["pages"] # take number of pages from the first book (first dictionary)
# print(f"\n1. The first edition has:, {number_of_pages} pages.") 

# list_books_manualy[0].update({"publisher": "Plato", "language": "Serbian"})
# print(f"2. Uppdated 4th book with .update() - Publisher is: {list_books_manualy[0]["publisher"]} and language: {list_books_manualy[0]["language"]}\n")
# print("3.")
# print("4.")
# print("5.")
# print("...")
# print("10.")
# print()



# # F.6 Print a clean summary of the catalogue without using loops yet. Repetition is 
# #     acceptable here because loops come next lesson.
#------------------------------------------------------------------------------------


# print("=" * 80)
# print("                              CATALOGUE SUMMARY               ")
# print("=" * 80)

# b1 = list_books_manualy[0]
# print(f"1. {b1['title']} by {b1['author']} ({b1['pages']} pages) - Available: {b1['available']}")

# b2 = list_books_manualy[1]
# print(f"2. {b2['title']} by {b2['author']} ({b2['pages']} pages) - Available: {b2['available']}")

# b3 = list_books_manualy[2]
# print(f"3. {b3['title']} by {b3['author']} ({b3['pages']} pages) - Available: {b3['available']}")

# b4 = list_books_manualy[3]
# print(f"4. {b4['title']} by {b4['author']} ({b4['pages']} pages) - Available: {b4['available']}")

# b5 = list_books_manualy[4]
# print(f"5. {b5['title']} by {b5['author']} ({b5['pages']} pages) - Available: {b5['available']}")

# b6 = list_books_manualy[5]
# print(f"6. {b6['title']} by {b6['author']} ({b6['pages']} pages) - Available: {b6['available']}")

# b7 = list_books_manualy[6]
# print(f"7. {b7['title']} by {b7['author']} ({b7['pages']} pages) - Available: {b7['available']}")

# b8 = list_books_manualy[7]
# print(f"8. {b8['title']} by {b8['author']} ({b8['pages']} pages) - Available: {b8['available']}")

# b9 = list_books_manualy[8]
# print(f"9. {b8['title']} by {b9['author']} ({b9['pages']} pages) - Available: {b9['available']}")

# b10 = list_books_manualy[9]
# print(f"10. {b10['title']} by {b10['author']} ({b10['pages']} pages) - Available: {b10['available']}")

# print("=" * 80)



#******************************************************************************************************
#   LAB 2                           Part G - Nested collections                                       *
#******************************************************************************************************

# G.1 Given two lists of usernames, determine duplicates and unique usernames using sets.
#----------------------------------------------------------------------------------------

# list1 = ["anna", "bob", "charlie", "david", "grace"]
# list2 = ["charlie", "eva", "frank", "grace", "anna"]

# # Convert lists to sets
# set1 = set(list1)
# set2 = set(list2)

# duplicates = set1.intersection(set2)

# all_unique = set1.union(set2)

# print(f"Duplicates (in both sets) : {duplicates}")
# print(f"All Unique Usernames      : {all_unique}")



# G.2 Design a nested collection for a small online course platform: 
#     courses, teacher, students and topics. Do not write classes.
#------------------------------------------------------------------

# course_platform = [
#     {
#         "course_id": "DATR1000X",
#         "title": "Dator- och kommunikationsteknik, Nivå 1",
#         "teacher": "Dr. Mileva Maric",
#         "topics": ["Architecture and computer hardware", "OS", "Software", "Installation and configuration"],
#         "students": ["vilma", "adam", "nelly", "sofia"]
#     },
#     {
#         "course_id": "AUTM1000X",
#         "title": "Automationsteknik, Nivå 1",
#         "teacher": "Prof. Pavle Savic",
#         "topics": ["Ellära", "Styrsystem", "Logiska funktioner","Pneumatik", "Mekanik"],
#         "students": ["kean", "mahdi", "orhan", "tage"]
#     },
#     {
#         "course_id": "NATV1000X",
#         "title": "Nätverksteknologier",
#         "teacher": "Dr. Marcus Pizdis",
#         "topics": ["Networks models", "Nätverkskompnenter", "Nätverkstopologier","Nätverkssäkerhet"],
#         "students": ["gabriel", "lucas", "ali", "leo", "ahmed", "markus"]
#     }
# ]

# print("\n ***  COURSE OVERVIEW  ***\n")
# for course in course_platform:
#     print(f"Course: {course['title']} ({course['course_id']}) | Teacher: {course['teacher']}")
#     print(f" Topics: {', '.join(course['topics'])}")
#     print(f" Number of students: {len(course['students'])}\n")



# G.3 Create a dictionary-based inventory for five products. Update stock values manually 
#     and calculate total units using values.
#---------------------------------------------------------------------------------------

# inventory = {
#     "Laptop": 15,
#     "Mouse": 50,
#     "Keyboard": 30,
#     "Monitor": 20,
#     "Printer": 45
# }

# print(f"Start position - inventory: {inventory}")


# inventory["Mouse"] = 35          # 15 items sold
# inventory["Monitor"] += 20       # New items have arrived in stock (20)
# inventory["Webcam"] = 25         # The new item has been added to inventory

# print(f"Uppdatet inventory: {inventory}")



# G.4 Write a short comparison in comments: list vs tuple vs set vs dictionary.
#     Give one situation where each is the best fit. 
#------------------------------------------------------------------------------

# List: to order sequence, that can be changed over time.
# Situation: inventory/stacks

# Tuple: Best for fixed, immutable groups of data. Good system performance (fixed memory)
# Situation: Data protection / database records

# Set: Best for storing unique values
# Situation: finding duplicates

# Dictionary: Best for key-value lookups, structured data, or fast search by key.
# Suituation: user profiles/catalog items/inventory



# **********************************  END of LAB 2  *****************************************
