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


















#python file handling

# file=open("test.txt","mode")  #syntax

# r-read > read an existing file 
# w-write > create a file or overwirte an existing file 
# a-append > add data to the end
# x-exulsice creation > create a fle only if it it does not exit




# file=open("aipa,txt","w")
# file.write("Hello Student of AIPA")
# file.close()

# with open("aipa2.txt","w") as file:
#     file.write("Hello Student of AIPA NSTI A1d")


#append "a" - add a new line to an existing file

# with open("aipa2.txt","a") as file:
#     file.write("\n Prayagraj ,Utthar Pradesh")
#     file.write("\n India")







# text="""National Skill Training Institute (Women), Allahabad

# Established in 1992 as the Regional Vocational Training Institute,
# Allahabad is one of the premier institutions under the Directorate
# General of Training (DGT), Ministry of Skill Development and
# Entrepreneurship, Government of India, dedicated exclusively
# to the vocational training of women."""

# with open("aipa.txt", "w", encoding="utf-8") as file:
#     file.write(text)

# print("Data written successfully!")

# # Reading text from a file

# with open("aipa.txt", "r", encoding="utf-8") as file:
#     data = file.read()

# print(data)


# # read -"r" read all the content of file 

# with open ("aipa.txt","r") as file:
#     x=file.read()
#     print(x)

#     x=file.read(52)
#     print(x)

#     print(file.readline())
#     print(file.readline())
#     print(file.readline())

#     print(file.readline().strip())
#     print(file.readline().strip())
#     print(file.readline().strip())

#     lines=file.readline()
# print(lines)    


# METHOD 1: read() - Read complete file
# print("\n===== METHOD 1: read() =====")

# with open("aipa.txt", "r", encoding="utf-8") as file:
#     print(file.read())


# # METHOD 2: read(52) - Read 52 characters
# print("\n===== METHOD 2: read(52) =====")

# with open("aipa.txt", "r", encoding="utf-8") as file:
#     print(file.read(52))


# # METHOD 3: readline() - Read one line
# print("\n===== METHOD 3: readline() =====")

# with open("aipa.txt", "r", encoding="utf-8") as file:
#     print(file.readline())


# # METHOD 4: Multiple readline() calls
# print("\n===== METHOD 4: Multiple readline() =====")

# with open("aipa.txt", "r", encoding="utf-8") as file:
#     print(file.readline())
#     print(file.readline())
#     print(file.readline())


# # METHOD 5: readlines() - Read all lines into a list
# print("\n===== METHOD 5: readlines() =====")

# with open("aipa.txt", "r", encoding="utf-8") as file:
#     lines = file.readlines()
#     print(lines)


# # METHOD 6: for loop - Read line by line
# print("\n===== METHOD 6: for loop =====")

# with open("aipa.txt", "r", encoding="utf-8") as file:
#     for line in file:

#         print(line.strip())



import csv
std=[
    =["Shreya","27,"AIPA"],
    ["Ajeet",27,"AIPA"],
    ["Aditya",27,"AIPA"],
    ["Khushi",27,"AIPA"],
    ["Nirupama",27,"AIPA"]]