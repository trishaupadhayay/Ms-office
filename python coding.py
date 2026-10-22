#Rectangle pattern

# for i in range(4):
#     for j in range(6):
#         print("*", end=" ")
#     print()



#Increasing triangle

# for i in range(1, 8):
#     for j in range(i):
#         print("*", end=" ")
#     print()



#Number square
# for i in range(4):
#     for j in range(1, 5):
#         print(j, end=" ")
#     print()



#Multiplication tables
# for i in range(1, 11):
#     print("Table of", i)

#     for j in range(1, 11):
#         print(i, "x", j, "=", i * j)

#     print()



#Classroom seating
# for i in range(1, 6):
#     for j in range(1, 9):
#         print("Row", i, "Seat", j)
#     print()



# #Prime numbers
# for i in range(2, 51):
#     for j in range(2, i):
#         if i % j == 0:
#             break
#     else:
#         print(i, end=" ")


#Pattern challenge
# for i in range(1, 6):
#     for j in range(5 - i):
#         print(" ", end="")
#     for k in range(2 * i - 1):
#         print("*", end="")
#     print()

    


#Greeting function

# def greet(name):
#     print("Welcome", name)

# greet("Trisha")





#Addition function
# def add(a, b):
#     return a + b

# result = add(10, 20)
# print("Sum:", result)





#Even or odd
# def even_odd(num):
#     if num % 2 == 0:
#         return "Even"
#     else:
#         return "Odd"

# print(even_odd(8))
# print(even_odd(5))


#Factorial calculator
# def factorial(n):
#     fact = 1
#     for i in range(1, n + 1):
#         fact = fact * i
#     return fact

# print("Factorial:", factorial(5))
#List statistics
# def total(numbers):
#     return sum(numbers)

# def average(numbers):
#     return sum(numbers) / len(numbers)

# def minimum(numbers):
#     return min(numbers)

# def maximum(numbers):
#     return max(numbers)

# numbers = [10, 20, 30, 40, 50]

# print("Total:", total(numbers))
# print("Average:", average(numbers))
# print("Minimum:", minimum(numbers))
# print("Maximum:", maximum(numbers))



#Banking application
# balance = 1000

# def deposit(amount):
#     global balance
#     balance += amount
#     print("Amount deposited successfully")

# def withdraw(amount):
#     global balance
#     if amount <= balance:
#         balance -= amount
#         print("Amount withdrawn successfully")
#     else:
#         print("Insufficient balance")

# def show_balance():
#     print("Current balance:", balance)

# while True:
#     print("\n1. Deposit")
#     print("2. Withdraw")
#     print("3. Check Balance")
#     print("4. Exit")

#     choice = input("Enter your choice: ")

#     if choice == "1":
#         amount = int(input("Enter amount: "))
#         if amount > 0:
#             deposit(amount)
#         else:
#             print("Enter a valid amount")

#     elif choice == "2":
#         amount = int(input("Enter amount: "))
#         if amount > 0:
#             withdraw(amount)
#         else:
#             print("Enter a valid amount")

#     elif choice == "3":
#         show_balance()

#     elif choice == "4":
#         print("Thank you!")
#         break

#     else:
#         print("Invalid choice")





#9. Student record processor
# students = [
#     {"name": "Rahul", "marks": 80},
#     {"name": "Priya", "marks": 65},
#     {"name": "Aman", "marks": 30},
#     {"name": "Neha", "marks": 90}
# 

# def calculate_average(students):
#     total = 0
#     for student in students:
#         total += student["marks"]
#     return total / len(students)

# def passing_students(students):
#     for student in students:
#         if student["marks"] >= 40:
#             print(student["name"], "Passed")

# print("Class Average:", calculate_average(students))
# print("Passing Students:")
# passing_students(students)



# Directory information
# import os

# print("Current Directory:", os.getcwd())
# print("Files and Folders:")

# for item in os.listdir():
#     print(item)




# File existence
# from pathlib import Path

# filename = input("Enter filename: ")
# file = Path(filename)

# if file.exists():
#     print("File exists.")
# else:
#     print("File does not exist.")



# # Create nested folders
# from pathlib import Path

# folder = Path("College/Students/AIPA")
# folder.mkdir(parents=True, exist_ok=True)

# print("Folders created successfully!")



# # Find file types
# from pathlib import Path

# folder = Path(input("Enter folder path: "))

# for file in folder.iterdir():
#     if file.is_file() and file.suffix in [".csv", ".txt"]:
#         print(file.name)



# # Backup a file       
# import shutil
# from pathlib import Path

# file = Path(input("Enter text filename: "))
# backup = Path("Backup")

# backup.mkdir(exist_ok=True)

# if file.is_file():
#     shutil.copy2(file, backup / file.name)
#     print("Backup created successfully!")
# else:
#     print("File not found.")





# # Move files
# import shutil
# from pathlib import Path

# source = Path("Practice")
# destination = Path("PDF")

# destination.mkdir(exist_ok=True)

# for file in source.glob("*.pdf"):
#     shutil.move(str(file), str(destination / file.name))

# print("PDF files moved successfully!")




# # Directory backup
# import shutil
# from pathlib import Path

# source = Path("Test")
# destination = Path("Test_Backup")

# if source.is_dir():
#     shutil.copytree(source, destination, dirs_exist_ok=True)
#     print("Directory backup created successfully!")
# else:
#     print("Test directory not found.") 



# 1: Safe Division Calculator
# try:
#     num1 = float(input("Enter first number: "))
#     num2 = float(input("Enter second number: "))

#     result = num1 / num2
#     print("Result:", result)

# except ValueError:
#     print("Error: Please enter valid numbers.")

# except ZeroDivisionError:
    # print("Error: Cannot divide by zero.")



# 2: Positive Number Validator
# try:
#     num = int(input("Enter a number: "))

#     if num < 0:
#         raise ValueError("Number cannot be negative.")

#     print("Valid positive number:", num)

# except ValueError as e:
#     print("Error:", e)



# 3: List Index Handling
# numbers = [10, 20, 30, 40, 50]

# try:
#     index = int(input("Enter an index (0-4): "))
#     print("Number:", numbers[index])

# except IndexError:
#     print("Error: Invalid index.")

# except ValueError:
#     print("Error: Please enter an integer.")




#  4: Dictionary Lookup
# student = {
#     "name": "Trisha",
#     "trade": "AIPA",
#     "marks": 85
# }

# try:
#     key = input("Enter a key (name, trade, marks): ")
#     print("Value:", student[key])

# except KeyError:
#     print("Error: Key not found.")



# 5: File Reading
# try:
#     filename = input("Enter filename: ")

#     with open(filename, "r") as file:
#         content = file.read()
#         print("File contents:")
#         print(content)

# except FileNotFoundError:
#     print("Error: File not found.")




# 6: Integer Input Validation
# while True:
#     try:
#         num = int(input("Enter an integer: "))
#         print("Valid integer:", num)
#         break

#     except ValueError:
#         print("Invalid input! Please enter an integer.")




# 7: Custom Exception

# class InsufficientBalanceError(Exception):
#     pass

# balance = 5000

# try:
#     amount = float(input("Enter withdrawal amount: "))

#     if amount > balance:
#         raise InsufficientBalanceError("Insufficient balance!")

#     balance = balance - amount
#     print("Withdrawal successful.")
#     print("Remaining balance:", balance)

# except ValueError:
#     print("Error: Please enter a valid amount.")

# except InsufficientBalanceError as e:
#     print("Error:", e)






# 8: Employee Salary Validation
# try:
#     salary = float(input("Enter employee salary: "))

#     if salary < 0:
#         raise ValueError("Salary cannot be negative.")

#     print("Valid salary:", salary)

# except ValueError as e:
#     print("Error:", e)