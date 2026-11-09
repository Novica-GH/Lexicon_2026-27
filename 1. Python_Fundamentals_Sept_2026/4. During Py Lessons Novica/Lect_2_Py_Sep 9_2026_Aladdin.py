#******************************************************************************************
# Novica Ivkovic
# Cours: System Developer Python and AI
# September 9 2026 - Vezbanja tokom predavanja od 9-12h - Aladdin
#
#*******************************************************************************************
#   - LISTE -  List {}  []   - cls ili clear za brisanje ekrana
#*********************************************
#
#  List is Mutable
#
# ['apple', 'banana','orange']  # <- Mutable
#
# numbers = [10, 20, 30, 40, 50]
# print(numbers)
# print(numbers[0])
# print(numbers[-5])
# print(numbers[-1])
#print(numbers[4]) 
#print(numbers[1:4])
# print(numbers[:3]) # Od pocetka do treceg clana, bez cetvrtog
# print(numbers[2:]) # od drugog clana pa do kraja
# print(numbers[::2]) # stampa svaki drugi clan
# print(numbers[::-1])  # Ispisace sve clanve liste u obrnutom poretku - reverse
#[{}}}}}}}}}}}}}{{{{{{[[[[[]]]]]}}}}}}]
 
# mixed = [10,"python",True, 3.14]
# print (mixed)

# matrix_like = [        # Matrica se ovako definise
#     [1, 2, 3], 
#     [4, 5, 6],
#     [7, 8, 9]
# ]

# print(matrix_like)

# print(matrix_like[1][1])  # pristupa se korak po korak [bira se lista u matrici] i [bira se clan u toj listi]



# names = ["Aladdin", "Grace", "Alan"] 
# names[1] ="Guido"
# print (names)

# languages = ["Python", "Java", "C#"]
# print (languages)

# # APPEND - append - sta znaci append

# languages.append("JavaScript")
# print(languages)

# #insert   Insertuje element na poziciju naznacenog indeksa i pomera ostale clanove u desno

# languages.insert(1, "Go")
# print (languages)

# remove - Uklanja imenovani element liste
# languages.remove("Java")
# print(languages)

#pop  - 
# Razkuja izmedju remove i pop - ...
# I takodje pop vraca uklonjeni element
# removed_languages = languages.pop(-1)
# print(languages)
# print(removed_languages)

# languages = ["Python", "Java", "C#", "JavaScript"]
# print(len(languages))
# print("Python" in languages)  # daje boolean vrednos da li je element u listi ili ne
# print("Rust" in languages)    # znaci ovo je provera / check

#numbers =  [5, 2, 9, 1, 7]
# print(numbers)
# print.reverse()    # Print in revers order
# numbers.sort()     # Sort and change original list
# print(numbers)

# numbers.reverse()
# print(numbers)

#sorted vd sort
# new_numbers = sorted(numbers)  # sorted does'n change original list!!!
# print(numbers)
# print(new_numbers)

# list_a =  [1, 2, 3]
# list_b list_a.copy

#*******************************************************************

# Tuples -> immutable   (Parovi - n-torke) - Koordinate
#------------------------------------------------------

# - also ordered collections 
# - also supporting indexing with some diff 
# - and the main diff is that tuples are immutable
# Why we need tuples? 
# Tuples doesn't support item assignment (dodeljivanja, dodavanja), since they are immutable
# We can mix data types
# Tuple style unpacking is wery Pythonic...

# Exempel - coordinates
#--------------------------
# coordinates = (10, 20)
#print(coordinates)
# print(coordinates[0])
# print(coordinates[1])
#---------------------

# x, y = coordinates

# print(x)  # it works
# print(y)  # it works
#--------------------
# We can mix data types
# person = ("Ada", 36, "London", False)

# name, age, city, student = person
# person.append("Djoka") # Ovo nece raditi, jer torke se ne mogu menjati (imutable)-nepromenljivi

# print(name)
# print(age)
# print(city)
# print(student)
#-----------------------------
# Tuple style unpacking is wery Pythonic...
# a = 10
# b = 20

# a, b = b, a

# print(a)
# print(b)
#----------------------------

#*******************************************************************

# Sets - That is a collection where every value is unique  
#-------
# Exempel:  numbers = {1, 2, 3, 4}
#           print(numbers)    
#------------------------------------------------------

# numbers = {1, 2, 2, 2, 2, 3, 3, 4}
# print(numbers)
# users = {"anna", "bob", "anna", "charlie", "bob"}

# But, if we use a list, and want to take unique value from the list
# Then we are going to use a set to help us with it:

# users = ["anna", "bob", "anna", "charlie", "bob"]

# unique_users = set(users)

# print(unique_users)

languages = {"Python", "Java", "C#"}
print(languages)

languages.add("Go")
print(languages)
