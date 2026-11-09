#******************************************************************************************
# Novica Ivkovic
# Cours: System Developer Python and AI
# September 17 2026 - Today's study goal is: LAB 2 - Challenge
#                     
#**********************************************************

# Sva predavanja sredjena od Sven Ericsson-a Kolege - PART 1 2026-09-08

## Python Fundamentals

### Introduction
- **Purpose**: The goal of this course is to ensure everyone has a solid foundation in Python before diving into data analysis, AI, and machine learning.
- **Background**: Python was created by Guido van Rossum and was first released in the early 1990s. Its main focus is on readability and simplicity, making it an ideal language for beginners and experts alike.

### Setting Up the Environment
- **Python Installation**: Ensure Python is installed correctly. You can verify by running `python` in the terminal to start the Python interpreter.
- **Interactive Shell**: Use the Python interactive shell to test snippets of code.
    ```python
    >>> print("Hello World")
    Hello World
    ```

### Basic Syntax and Data Types

#### Variables
- **Dynamic Typing**: Python automatically determines the data type of a variable based on its assigned value.
    ```python
    number = 10
    print(type(number))
    ```
- **Variable Naming Conventions**: Follow snake_case (e.g., `snake_case`) and avoid starting with numbers or special characters.

#### Data Types
- **Integer** (`int`)
- **Float** (`float`)
- **String** (`str`)
- **Boolean** (`bool`): True and False are case-sensitive.

### Arithmetic Operators
- **Examples**:
    ```python
    print(5 + 2)   # 7
    print(5 - 2)   # 3
    print(5 * 2)   # 10
    print(5 / 2)   # 2.5
    print(5 ** 2)  # 25
    print(5 // 2)  # 2 (Floor division)
    print(5 % 2)   # 1 (Modulus - remainder)
    ```

### Type Conversion
- **Converting Data Types**:
    ```python
    number_as_text = '10'
    number = int(number_as_text)
    print(number + 5)  # 15
    ```

### Strings
- **Creation and Concatenation**:
    ```python
    first_name = 'Ada'
    last_name = 'Addison'
    full_name = first_name + ' ' + last_name
    print(full_name)  # Ada Addison
    ```
- **Slicing and Indexing**:
    ```python
    text = 'python'
    print(text[0:3])  # pyt
    print(text[-1])   # n
    ```
- **String Methods**:
    ```python
    message = " Hello Python "
    print(message.lower())  # hello python
    print(message.strip())  # Hello Python
    print(message.replace("Python", "Powerful"))  # Hello Powerful
    ```

### Immutability of Strings
- **Changing a String**:
    ```python
    word = 'python'
    word = word[0].replace('p', 'j') + word[1:]
    print(word)  # jython
    ```

### Lists
- **Introduction**: Lists are mutable sequences used to store multiple items. 
- **Creating Lists**:
    ```python
    data = ['apple', 'banana', 'orange']
    print(len(data))  # 3
    ```

### Conclusion
- **Next Steps**: The next lesson will focus on lists and their operations, including slicing, indexing, and mutability.

### Additional Notes
- **AI Usage**: Some examples and labs may have been created or refined using AI tools to enhance clarity and educational value.
- **Lab Instructions**: Labs will be available in a specific folder within the Python Info chat. Follow instructions carefully and complete the lab to reinforce concepts covered in the lecture.


#************************************************************************
# Sva predavanja sredjena od Sven Ericsson-a Kolege - PART 2 2026-09-09
#************************************************************************

## Introduction to Python Collections
### Recap of Previous Lesson
In the previous lesson, we covered the basics of Python variables, data types, and strings. We also explored the `split()` method for strings which splits a string into multiple substrings based on a delimiter and returns them in a list format.

### Understanding Lists
#### Definition and Characteristics
- **Lists** are ordered collections of items that can be of different data types. Lists are mutable, meaning their content can be changed after creation.
- Example:
  ```python
  numbers = [10, 20, 30, 40, 50]
  print(numbers)
  ```
- Lists maintain order and every element has an index starting from 0.
- Example:
  ```python
  print(numbers[1])  # Output: 20
  print(numbers[2])  # Output: 30
  print(numbers[-1]) # Output: 50 (Last element)
  ```

#### Slicing Lists
- Lists can be sliced using indices to extract parts of a list.
- Syntax: `list[start:stop:step]`
- Example:
  ```python
  print(numbers[1:4])  # Output: [20, 30, 40]
  print(numbers[::2])  # Output: [10, 30, 50] (Every second element)
  print(numbers[::-1]) # Output: [50, 40, 30, 20, 10] (Reverse order)
  ```

### List Methods
- **append()**: Adds an element at the end of the list.
  ```python
  languages = ['Python', 'Java', 'C#']
  languages.append('JavaScript')
  print(languages)
  ```
- **insert()**: Adds an element at a specific position.
  ```python
  languages.insert(1, 'Go')
  print(languages)
  ```
- **remove()**: Removes the first occurrence of a specified value.
  ```python
  languages.remove('Go')
  print(languages)
  ```
- **pop()**: Removes and returns the last element or an element at a specified index.
  ```python
  removed = languages.pop(1)
  print(removed)  # Output: Java
  print(languages)
  ```
- **sort()**: Sorts the elements of a list in place.
  ```python
  numbers = [5, 2, 9, 1, 7]
  numbers.sort()
  print(numbers)
  ```
- **reverse()**: Reverses the elements of a list in place.
  ```python
  numbers.reverse()
  print(numbers)
  ```

### Deep Dive into Lists
- **Mutability**: Lists can be modified after creation.
- Example:
  ```python
  names = ['Aladdin', 'Grace', 'Aladdin']
  names[1] = 'Guido'
  print(names)
  ```
- **Shallow Copy**: Using `.copy()` to create a shallow copy of a list.
  ```python
  listA = [1, 2, 3]
  listB = listA.copy()
  listB.append(4)
  print(listA)  # Output: [1, 2, 3]
  print(listB)  # Output: [1, 2, 3, 4]
  ```

### Introduction to Tuples
#### Definition and Characteristics
- **Tuples** are similar to lists but are immutable, meaning their content cannot be changed after creation.
- Example:
  ```python
  coordinates = (10, 20)
  print(coordinates[0])  # Output: 10
  ```
- Tuples can be used for fixed data and are often used for multiple assignments.
- Example:
  ```python
  x, y = coordinates
  print(x, y)  # Output: 10 20
  ```

### Sets
#### Definition and Characteristics
- **Sets** are collections of unique elements.
- Example:
  ```python
  numbers = {1, 2, 2, 3, 4}
  print(numbers)  # Output: {1, 2, 3, 4}
  ```
- Sets can be used to remove duplicates and perform set operations like union, intersection, and difference.
- Example:
  ```python
  backend_langs = {'Python', 'Java', 'C#'}
  data_langs = {'Python', 'R', 'Julia'}
  print(backend_langs & data_langs)  # Output: {'Python'}
  print(backend_langs | data_langs)  # Output: {'Python', 'Java', 'C#', 'R', 'Julia'}
  print(backend_langs - data_langs)  # Output: {'Java', 'C#'}
  ```

### Dictionaries
#### Definition and Characteristics
- **Dictionaries** store data as key-value pairs.
- Example:
  ```python
  person = {'name': 'Ada', 'age': 36, 'city': 'London'}
  print(person['name'])  # Output: Ada
  ```
- Dictionaries allow efficient access to values using keys.
- Example:
  ```python
  person['age'] = 37
  person['language'] = 'Python'
  print(person)
  ```
- Methods like `keys()`, `values()`, and `items()` can be used to access or manipulate dictionary data.
- Example:
  ```python
  print(person.keys())  # Output: dict_keys(['name', 'age', 'city', 'language'])
  print(person.values())  # Output: dict_values(['Ada', 37, 'London', 'Python'])
  print(person.items())  # Output: dict_items([('name', 'Ada'), ('age', 37), ('city', 'London'), ('language', 'Python')])
  ```

### Nested Data Structures
- Dictionaries can contain other dictionaries or lists.
- Example:
  ```python
  students = [
      {'name': 'Anna', 'score': 85},
      {'name': 'Bob', 'score': 72},
      {'name': 'Charlie', 'score': 91}
  ]
  print(students[1]['score'])  # Output: 72
  ```

### Conclusion
- The lesson covered fundamental data structures in Python including lists, tuples, sets, and dictionaries. Each has its unique characteristics and use cases.
- Understanding these data structures is crucial for managing and manipulating data effectively in Python programs.


#************************************************************************
# Sva predavanja sredjena od Sven Ericsson-a Kolege - PART 2 2026-09-10
#************************************************************************

## Python Fundamentals: Control Flow and Loops

### Comparisons and Boolean Expressions

- **Definition**: Comparisons in Python evaluate to a boolean value (True or False).
- **Operators**:
  - `==` Equality
  - `!=` Not equal
  - `>` Greater than
  - `<` Less than
  - `>=` Greater than or equal to
  - `<=` Less than or equal to
- **Example**:
  ```python
  print(5 > 2)  # Output: True
  print(5 < 2)  # Output: False
  print(5 == 2) # Output: False
  print(5 != 2) # Output: True
  print(5 >= 2) # Output: True
  print(5 <= 2) # Output: False
  ```
- **Gotchas**: 
  - Be careful with the use of `=` (assignment) versus `==` (comparison).
  - `1 == '1'` evaluates to `True` in Python due to type coercion, but it's generally a bad practice.

### Conditional Statements

- **Syntax**: 
  - `if condition:`
  - `elif condition:`
  - `else:`
- **Indentation**: 
  - Python uses indentation to define code blocks. A common practice is to use 4 spaces per indentation level.
- **Example**:
  ```python
  age = 18
  if age >= 18:
      print("Adult")
  else:
      print("Under 18")
  ```
- **Logical Operators**:
  - `and` (both conditions must be true)
  - `or` (at least one condition must be true)
  - `not` (reverses a boolean value)
- **Example**:
  ```python
  age = 25
  has_ticket = True
  if age >= 18 and has_ticket:
      print("You may enter")
  else:
      print("Entry denied")
  ```

### Truthiness and Falsiness

- **Definition**: Some values are inherently treated as `True` or `False` in boolean contexts.
- **Falsy Values**:
  - `None`
  - `False`
  - `0` (integer or float)
  - Empty sequences (strings, lists, dictionaries, etc.)
- **Example**:
  ```python
  name = ''
  if name:
      print("Name is not empty")
  else:
      print("Name is empty")
  ```
- **Gotchas**: 
  - `False` is falsy, but `True` is truthy.
  - Strings with spaces (like `' '` or `'    '`) are truthy.

### Loops

#### For Loop

- **Syntax**:
  - `for variable in iterable:`
  - `print(variable)`
- **Example**:
  ```python
  languages = ['Python', 'Java', 'C#']
  for language in languages:
      print(language)
  ```
- **Nested Iteration**:
  - Use `for` loops to iterate over dictionaries and lists.
  - Example:
    ```python
    student = {'name': 'Ada', 'age': 25, 'course': 'AI'}
    for key in student:
        print(key, student[key])
    ```
- **Loop Control Statements**:
  - `enumerate()`: Provides index and value of iterable.
    ```python
    for index, language in enumerate(languages):
        print(index, language)
    ```
  - `range(start, stop, step)`: Creates a sequence of numbers.
    ```python
    for number in range(1, 10, 2):
        print(number)
    ```

#### While Loop

- **Syntax**:
  - `while condition:`
  - `print(something)`
- **Example**:
  ```python
  count = 1
  while count <= 5:
      print(count)
      count += 1
  ```
- **Infinite Loops**:
  - Be cautious of conditions that never become false.
  - Example of an infinite loop:
    ```python
    count = 1
    while count <= 5:
        print(count)
    ```

### Break and Continue Statements

- **Break**:
  - Exits the loop when a condition is met.
  - Example:
    ```python
    numbers = [2, 4, 6, 7, 8, 10]
    for number in numbers:
        if number % 2 != 0:
            print("Found an odd number:", number)
            break
    ```
- **Continue**:
  - Skips the rest of the current iteration and moves to the next one.
  - Example:
    ```python
    numbers = [1, 2, 3, 4, 5]
    for number in numbers:
        if number == 3:
            continue
        print(number)
    ```

### Summary

Today's lesson covered control flow statements, loops, and loop control mechanisms in Python. 
Understanding these concepts is crucial for writing efficient and readable code. Practice these techniques to solidify your understanding.

#************************************************************************
# Sva predavanja sredjena od Sven Ericsson-a Kolege - PART 2 2026-09-11
#************************************************************************


## Introduction to Git and GitHub

### Setting Up a Git Repository
- **Rule**: To manage your Python projects, you will use Git and GitHub. Git is a distributed version control system that allows you to track changes in your codebase, and GitHub is a web-based platform that provides a central repository for your Git projects.

- **Code Example**:
```bash
# Create a new directory for your project
mkdir git-demo

# Navigate into the new directory
cd git-demo

# Initialize a new Git repository
git init

# Create a simple text file
echo "This is a sample text file." > python.txt

# Add all files in the directory to the Git staging area
git add .

# Commit the changes with a message
git commit -m "Initial commit"
```

- **Gotchas**:
  - Always remember to `git add` files before committing.
  - Ensure your commit messages are clear and concise.
  - Avoid making changes directly in the GitHub web interface; it's better to use the command line.

- **Why It Matters**: Git and GitHub are essential tools for tracking changes in your codebase, collaborating with others, and ensuring that your work is backed up and accessible.

### Adding and Committing Changes
- **Rule**: After making changes to your files, you need to add them to the Git staging area and then commit the changes.

- **Code Example**:
```bash
# Make changes to your file
echo "This is an updated line." >> python.txt

# Add the changed file to the staging area
git add python.txt

# Commit the changes with a message
git commit -m "Update file"
```

- **Gotchas**:
  - Remember to add files to the staging area before committing.
  - Use meaningful commit messages that describe what changes were made.

- **Why It Matters**: Properly using Git to track changes allows you to revert to previous versions of your project if needed and helps in collaboration with other developers.

### Pushing to GitHub
- **Rule**: After committing your changes locally, you need to push them to a remote GitHub repository.

- **Code Example**:
```bash
# Link your local repository to a remote GitHub repository
git remote add origin https://github.com/yourusername/git-demo.git

# Push your local commits to the remote repository
git push -u origin main
```

- **Gotchas**:
  - Ensure the remote URL is correctly set up.
  - Always push your changes to the main branch unless otherwise specified.

- **Why It Matters**: Pushing your code to GitHub ensures that your project is backed up and accessible online, making it easier to collaborate and share your work.

### Organizing Your Projects
- **Rule**: It is recommended to create a separate repository for each project or lab to keep your files organized and maintainable.

- **Code Example**:
```bash
# For each lab or project, create a new repository and follow the same steps as above
mkdir lab1
cd lab1
git init
# Add files and commit changes as before
```

- **Gotchas**:
  - Be consistent in naming your repositories and directories.
  - Consider using descriptive names for your repositories and branches.

- **Why It Matters**: Keeping your projects organized helps you and others to understand the structure of your work better, making collaboration and maintenance easier.

### Commit Messages
- **Rule**: Commit messages should be short and descriptive, explaining what changes were made in the commit.

- **Code Example**:
```bash
# Example commit message
git commit -m "Add initial setup for lab1"
```

- **Gotchas**:
  - Avoid overly long or vague commit messages.
  - Use clear and concise language.

- **Why It Matters**: Clear commit messages help in tracking changes and understanding the history of your project, which is crucial for effective version control and collaboration.


#************************************************************************
# Sva predavanja sredjena od Sven Ericsson-a Kolege - PART 2 2026-09-14
#************************************************************************


#************************************************************************
# Sva predavanja sredjena od Sven Ericsson-a Kolege - PART 2 2026-09-15
#************************************************************************


#************************************************************************
# Sva predavanja sredjena od Sven Ericsson-a Kolege - PART 2 2026-09-16
#************************************************************************


#************************************************************************
# Sva predavanja sredjena od Sven Ericsson-a Kolege - PART 2 2026-09-17
#************************************************************************
