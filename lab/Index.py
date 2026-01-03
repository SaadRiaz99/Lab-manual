# print('Name: Saad Bin Riaz | CMS ID : BAI-25F-035 | Department : Mathematics Science and Artificial Intelligence SECTION : AI-1A' )
# food = ["biryani", "pulao", "korma"]
# print("Before adding:", food)
# # Method 1: Append
# food.append("nehari")
# # Method 2: Insert at specific position
# food.insert(1, "haleem")
# print("After adding:", food)
# print('Name: Saad Bin Riaz| CMS ID : BAI-25F-035 | Department : Mathematics Science and Artificial Intelligence SECTION : AI-1A' )
# grocery = ["butter", "soap", "rice"]
# print("All elements in the array:")
# for x in grocery:
#     print(x) 
print('Name: Saad Bin Riaz| CMS ID : BAI-25F-035| Department : Mathematics Science and Artificial Intelligence SECTION : AI-1A' )
# cars = ["Ford", "Volvo", "BMW", "Toyota"]
# # Get the first value
# x = cars[0]
# print("First car:", x)
# # Get the last value
# y = cars[-1]
# print("Last car:", y)

# Function with one argument to print a name
# def print_one_name(name):
#     print(name)
# # Call the function three times with different names
# print_one_name("Ali")
# print_one_name("Zara")
# print_one_name("Ahmed")
# fruits = ["apple", "banana", "cherry", "mango", "peach", "guava",
# "watermelon"]
# taste = ["sour", "bitter", "sweet"]
# for fruit in fruits:
#  for t in taste:
#     print(fruit, "-", t) 
# print('My name is Saad and I study at Sindh Madressatul Islam University')
# print("My name is Saad and I study at Sindh Madressatul Islam University") 
# my_string = "Python is my favourite language"
# sliced_text = my_string[7:15]
# print("Original String:", my_string)
# print("Sliced Text (8th to 15th):", sliced_text)
# laptops = []
# laptops.append("Dell")
# laptops.append("HP")
# laptops.append("Lenovo")
# laptops.append("Apple")
# laptops.append("Asus")
# print ("Laptop Manufacturing Companies:")
# print(laptops)
# Fruits = ["Mango", "Cherry", "Orange", "Kivi"]
# # Get value from 2nd position (index 1)
# selected_Fruits = Fruits[1]
# print("Full List:", Fruits)
# print("Fruits at 2nd position:", selected_Fruits)
# numbers = [10, 20, 30, 40, 50, 60, 70]
# # Get values starting from the 3rd position (index 2)
# result = numbers[2:]
# print("Values from 3rd position:", result)

# from datetime import date
# today = date.today()
# print("Today's date:", today)

# from datetime import date,datetime
# today_date = date.today()
# today_time=datetime.today()
# print("Today's date:", today_date)
# print("Today's time:", today_time)
# class Person:
#     """A class to hold personal information."""

#     species = "Homo Sapiens"  # Class variable

#     def __init__(self, name, age, height):
#         self.name = name
#         self.age = age
#         self.height = height

#     def greet(self):
#         """A simple method to greet the person."""
#         return f"Hello, my name is {self.name}."

#     def get_height_info(self):
#         """Method to return height."""
#         return f"{self.name} is {self.height} cm tall."


# class Employee(Person):
#     """Extends Person to include job-related information."""

#     def __init__(self, name, age, height, employee_id, title):
#         super().__init__(name, age, height)
#         self.employee_id = employee_id
#         self.title = title

#     def get_work_info(self):
#         """New method for the derived class."""
#         return f"{self.name} (ID: {self.employee_id}) works as a {self.title}."


# # Create Employee object
# employee1 = Employee("Saad", 22, 178, "E1054", "Data Analyst")

# print("\nProgram 13: Calling Inherited Methods")

# # 1. Inherited Method (from Person)
# height_call = employee1.get_height_info()
# print(f"Inherited Height Call: {height_call}")

# # 2. Inherited Method (from Person)
# greet_call = employee1.greet()
# print(f"Inherited Greet Call: {greet_call}")

# # 3. Class Variable Access (from Person)
# print(f"Inherited Class Variable: {employee1.species}")

# # 4. Derived Class Method
# print(f"Derived Work Info: {employee1.get_work_info()}")
# class CustomPerson:
#     """A class using 'obj' instead of 'self'."""

#     def __init__(obj, name, age, height):
#         obj.name = name
#         obj.age = age
#         obj.height = height

#     def describe(obj):
#         return f"{obj.name} is {obj.age} years old and {obj.height} cm tall."


# # Create an object using the custom keyword
# person3 = CustomPerson("Sara", 22, 178)

# print("\nProgram 11: Using 'obj' instead of 'self'")
# print(person3.describe())
# my_tuple = (4, 2, 3, [6, 5])
# print("Original:", my_tuple)

# # Convert to list to modify
# temp_list = list(my_tuple)
# # Change value at index 2 (3 → 9)
# temp_list[2] = 9
# my_tuple = tuple(temp_list)
# print("Modified:", my_tuple)
# a = 10 # Integer
# b = 20.5 # Float
# c = 3 + 4j # Complex
# print(f"Value: {a}, Type: {type(a)}")
# print(f"Value: {b}, Type: {type(b)}")
# print(f"Value: {c}, Type: {type(c)}") 
# numbers = [10, 20, 30, 40, 50, 60, 70]
# # Get values starting from the 3rd position (index 2)
# result = numbers[2:]
# print("Values from 3rd position:", result)
# Fruits = ["Mango", "Cherry", "Orange", "Kivi"]
# # Adding two new fruits
# Fruits.append("berry")
# Fruits.append("grapes")
# print("Updated Fruit List:", Fruits)
# my_tuple = (4, 2, 3, [6, 5])
# print("Original:", my_tuple)

# # Convert to list to modify
# temp_list = list(my_tuple)
# # Change value at index 2 (3 → 9)
# temp_list[2] = 9
# my_tuple = tuple(temp_list)
# print("Modified:", my_tuple)

# my_dict = {'Name': 'Zara', 'Age': 7, 'Class': 'First'}
# print("Original:", my_dict)
# # Update values
# my_dict['Name'] = 'Ali'
# print("Updated:", my_dict)
# my_dict = {'Name': 'Zara', 'Age': 7, 'Class': 'First'}
# # Remove 'Age'
# del my_dict['Age']
# print("Dictionary after removing Age:", my_dict)
# a = 200
# b = 33
# print(f"Is a > b? {a > b}")
# print(f"Is a < b? {a < b}")
# # Not Equal To program
# print(f"Is a != b? {a != b}") 
# a = 33
# b = 33
# # Standard If/Elif/Else
# if b > a:
#     print("b is greater than a")
# elif a == b:
#     print("a and b are equal")
# else:
#     print("a is greater than b")
# # Short Hand Version (Ternary Operator)
# print("A and B are equal") if a == b else print("A and B are not equal")
# x = 9
# y = 5
# z = 13
# # AND
# if x > y and z > x:
#     print("Both conditions are True (AND)")
# # OR
# if x > z or x > y:
#     print("At least one condition is True (OR)") 
# num = 33
# if num > 9:
#     print("Number is above 10,")
# if num > 20:
#     print("and also above 20.")
# if num < 98 and num != 57:
#     print("It is also less than 98 and not equal to 57.")
# fruits = ["apple", "banana", "cherry", "mango", "peach"]
# print("--- Example with Break (stops at cherry) ---")
# for x in fruits:
#     if x == "cherry":
#         break
# print(x)
# print("\n--- Example with Continue (skips banana) ---")
# for x in fruits:
#     if x == "banana":
#         continue
# print(x)
# # Using range and len to loop by index
# print("\n--- Looping by index ---")
# for i in range(len(fruits)):
#     print(f"Index {i}: {fruits[i]}")
# fruits = ["apple", "banana", "cherry", "mango", "peach", "guava",
# "watermelon"]
# taste = ["sour", "bitter", "sweet"]
# for fruit in fruits:
#  for t in taste:
#     print(fruit, "-", t) 

# Function with one argument to print a name
# def print_one_name(name):
#     print(name)
# # Call the function three times with different names
# print_one_name("Ali")
# print_one_name("Zara")
# print_one_name("Ahmed")
# grocery = ["butter", "soap", "rice"]
# print("All elements in the array:")
# for x in grocery:
#     print(x)
# cars = ["Ford", "Volvo", "BMW", "Toyota"]
# # Get the first value
# x = cars[0]
# print("First car:", x)
# # Get the last value
# y = cars[-1]
# print("Last car:", y)
# import os

# # Remove folder (only works if folder is empty)
# folder_name = "myfolder"

# if os.path.exists(folder_name):
#     try:
#         os.rmdir(folder_name)
#         print(f"Folder '{folder_name}' removed successfully.")
#     except OSError:
#         print(f"Folder '{folder_name}' is not empty or cannot be removed.")
# else:
#     print(f"Folder '{folder_name}' does not exist.")


# # Lab Exercise 1: File operations
# file_name = "labfile.txt"

# # Writing to a file
# with open(file_name, "w") as f:
#     f.write("This is Lab Exercise 1.\n")
#     f.write("File created and written successfully.\n")

# # Reading from the file
# with open(file_name, "r") as f:
#     print("\nContents of the file:")
#     print(f.read())
# file_name = "example.txt"
# try:
#     with open(file_name, "r") as file:
#         print(file.read())
# except FileNotFoundError:
#     print(f"File '{file_name}' not found.")
# import os
# import shutil

# def delete_file_and_folder(
#     file_name="file_to_delete.txt",
#     folder_name="folder_to_delete"
# ):
#     # --- Part 1: Setup (Create temporary file and folder) ---
#     try:
#         # Create a file
#         with open(file_name, 'w') as f:
#             f.write("I will be deleted.")
#         print(f"Setup: Created file '{file_name}'.")

#         # Create a folder and a file inside it
#         os.makedirs(folder_name, exist_ok=True)
#         with open(os.path.join(folder_name, "temp.txt"), 'w') as f:
#             f.write("Inside folder.")
#         print(f"Setup: Created folder '{folder_name}'.")

#     except Exception as e:
#         print(f"Setup failed: {e}")
#         return

#     # --- Part 2: Delete the File ---
#     try:
#         os.remove(file_name)
#         print(f"\nSUCCESS: File '{file_name}' deleted.")
#     except FileNotFoundError:
#         print(f"\nSKIPPED: File '{file_name}' not found.")
#     except Exception as e:
#         print(f"Error deleting file: {e}")

#     # --- Part 3: Delete the Folder (Directory) ---
#     try:
#         shutil.rmtree(folder_name)
#         print(f"SUCCESS: Folder '{folder_name}' and all its contents deleted.")
#     except FileNotFoundError:
#         print(f"SKIPPED: Folder '{folder_name}' not found.")
#     except Exception as e:
#         print(f"Error deleting folder: {e}")


# # Student: Saad Bin Riaz (pg. 52)
# delete_file_and_folder()
# import csv

# def handle_csv_file(file_name="people.csv"):
#     # --- Data to write ---
#     data_to_write = [
#         ['Name', 'Age', 'City'],
#         ['Quratulain', 21, 'Karachi'],
#         ['Ali', 22, 'Lahore'],
#         ['Zara', 20, 'Islamabad']
#     ]

#     # --- Part 1: Write to CSV ---
#     print(f"--- Writing to '{file_name}' ---")
#     try:
#         # 'w' mode, newline='' prevents extra blank rows
#         with open(file_name, 'w', newline='') as csvfile:
#             csv_writer = csv.writer(csvfile)
#             csv_writer.writerows(data_to_write)
#         print("CSV writing complete.")
#     except Exception as e:
#         print(f"Error writing CSV: {e}")
#         return

#     # --- Part 2: Read from CSV ---
#     print(f"\n--- Reading from '{file_name}' ---")
#     try:
#         with open(file_name, 'r', newline='') as csvfile:
#             csv_reader = csv.reader(csvfile)
#             for row in csv_reader:
#                 print(row)
#         print("CSV reading complete.")
#     except Exception as e:
#         print(f"Error reading CSV: {e}")


# # Student: Saad Bin Riaz (pg. 56)
# handle_csv_file()
# MY_LIST = ["apple", "banana", "cherry", "date"]

# # A dictionary
# MY_DICTIONARY = {
#     "name": "Module Data",
#     "version": 1.0,
#     "source": "data_module.py"
# }

# def display_data():
#     """Prints the contents of the module's data structures."""
#     print("--- Module Data ---")
#     print(f"List: {MY_LIST}")
#     print(f"Dict: {MY_DICTIONARY}")

# if __name__ == "__main__":
#     display_data()
# # Make sure data_module.py is in the same folder
# import data_module

# def import_and_use_module():
#     print("Program 7: Importing and using data_module.")

#     # Access the list and dictionary
#     print(f"List imported: {data_module.MY_LIST[0]}")
#     print(f"Dictionary imported: {data_module.MY_DICTIONARY['name']}")

#     # Call the function from the module
#     data_module.display_data()


# # Call the function
# import_and_use_module()
# class Person:
#     """A class to hold personal information."""

#     def __init__(self, name, age, height):
#         self.name = name
#         self.age = age
#         self.height = height  # Height in cm


# # Create instances
# person1 = Person(name="Alee", age=48, height=105)
# person2 = Person(name="Benazeer", age=32, height=185)

# # Display information
# print("Program 9: Creating Objects")
# print(f"Person 1: {person1.name}, Age: {person1.age}, Height: {person1.height} cm")
# print(f"Person 2: {person2.name}, Age: {person2.age}, Height: {person2.height} cm")
# class Person:
#     """A class to hold personal information."""

#     def __init__(self, name, age, height):
#         self.name = name
#         self.age = age
#         self.height = height  # Height in cm

#     def greet(self):
#         """A simple method to greet the person."""
#         return f"Hello, my name is {self.name}."

#     def get_height_info(self):
#         """Method to return height."""
#         return f"{self.name} is {self.height} cm tall."


# # Create Person objects with new values
# person1 = Person("Sara", 22, 178)
# person2 = Person("Ali", 25, 180)

# print("\nProgram 10: Calling the Height Method")

# # Call the instance method on person1
# height_info = person1.get_height_info()
# print(height_info)

# # Optional: also show greeting
# print(person1.greet())
# class CustomPerson:
#     """A class using 'obj' instead of 'self'."""

#     def __init__(obj, name, age, height):
#         # 'obj' refers to the object being created
#         obj.name = name
#         obj.age = age
#         obj.height = height

#     def describe(obj):
#         # 'obj' refers to the object on which the method is called
#         return f"{obj.name} is {obj.age} years old and {obj.height} cm tall."


# # Create an object using the custom keyword
# person3 = CustomPerson("Sara", 22, 178)

# print("\nProgram 11: Using 'obj' instead of 'self'")
# print(person3.describe())


# class Person:
#     """A class to hold personal information."""

#     def __init__(self, name, age, height):
#         self.name = name
#         self.age = age
#         self.height = height  # Height in cm

#     def get_height_info(self):
#         """Method to return height."""
#         return f"{self.name} is {self.height} cm tall."


# # Derived class
# class Employee(Person):
#     """Extends Person to include job-related information."""

#     def __init__(self, name, age, height, employee_id, title):
#         # Call the parent class's __init__ method
#         super().__init__(name, age, height)
#         # Add new attributes specific to Employee
#         self.employee_id = employee_id
#         self.title = title

#     def get_work_info(self):
#         """New method for the derived class."""
#         return f"{self.name} (ID: {self.employee_id}) works as a {self.title}."


# # Create an object of the extended class
# employee1 = Employee("Saad", 18, 178, "E1054", "Data Analyst")

# print("\nProgram 12: Extended Class (Employee)")
# # Call derived class method
# print(employee1.get_work_info())
# Employee can still use methods from the Person class
# print(employee1.get_height_info())
# class Person:
#     """A class to hold personal information."""
#     def __init__(self, name, age, height):
#         self.name = name
#         self.age = age
#         self.height = height  # Height in cm
# # Create instances
# person1 = Person(name="Saad", age=48, height=105)
# person2 = Person(name="Benazeer", age=32, height=185)
# # Display information
# print("Program 9: Creating Objects")
# print(f"Person 1: {person1.name}, Age: {person1.age}, Height: {person1.height} cm")
# print(f"Person 2: {person2.name}, Age: {person2.age}, Height: {person2.height} cm")
# class Person:
#     """A class to hold personal information."""
#     species = "Homo Sapiens"  # Class variable
#     def __init__(self, name, age, height):
#         self.name = name
#         self.age = age
#         self.height = height
#     def greet(self):
#         """A simple method to greet the person."""
#         return f"Hello, my name is {self.name}."
#     def get_height_info(self):
#         """Method to return height."""
#         return f"{self.name} is {self.height} cm tall."
# class Employee(Person):
#     """Extends Person to include job-related information."""
#     def __init__(self, name, age, height, employee_id, title):
#         super().__init__(name, age, height)
#         self.employee_id = employee_id
#         self.title = title
#     def get_work_info(self):
#         """New method for the derived class."""
#         return f"{self.name} (ID: {self.employee_id}) works as a {self.title}."
# # Create Employee object
# employee1 = Employee("Saad", 22, 178, "E1054", "Data Analyst")
# print("\nProgram 13: Calling Inherited Methods")
# # 1. Inherited Method (from Person): get_height_info()
# height_call = employee1.get_height_info()
# print(f"Inherited Height Call: {height_call}")
# # 2. Inherited Method (from Person): greet()
# greet_call = employee1.greet()
# print(f"Inherited Greet Call: {greet_call}")
# # 3. Class Variable Access (from Person)
# print(f"Inherited Class Variable: {employee1.species}")
# # 4. Derived Class Method
# print(f"Derived Work Info: {employee1.get_work_info()}")

# fruits = ["apple", "banana", "cherry", "mango", "peach", "gauva", 
# "watermelon"] 
# for fruit in fruits: 
#     print(fruit)
 
fruits = ["apple", "banana", "cherry", "mango", "peach", "guava", "watermelon"]
for fruit in fruits:
    print(fruit)
else:
    print("All fruits have been printed.")

