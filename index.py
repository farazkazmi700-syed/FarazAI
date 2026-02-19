# # name = "faraz"
# # print (name)
##---asignment 01-----***
# education = int (input ("Enter Your Education: "))
# age = int (input ("Enter Your Age: "))
# height = int (input ("Enter Your height: "))

# e=12
# a=18
# h=5.7
# if (a>18 and e>12) or (a>18 and h>5.7) or (h>5.7 and e>12):
#     print("You are eligible")
# else:
#     print("You are not eligible")

# n=int(input("Input Your Number: "))

# for i in range (1,21):
#     print(f"{n} x {i} = {n*i} " )


# n=int(input("Enter Even Number: "))

# for i in range (0,21, 2):
    # print(f"{i} x {i} = {n**i} " )
# Task 01
##---asignment 02-----***

# cities = ["jaranwala", "Lahore", "Fasialabad"]
# cities.extend(["Karachi","Islamabd"])
# print(cities)
# empty=[]
# print(empty)
# del empty
# print(empty)

 ##---asignment 03-----***

# print(len(cities))

 ##---asignment 04-----***

# cities.insert(1,"Mianwali")
# print(cities)

 ##---asignment 05-----***
# numbers= [0,1,2,3,4,5,6,7,8,9]
# print(numbers[-4:])

# x = [2,3,4]
# y = x.copy()
# y.append(5)
# print(x)'

  ##---asignment 06-----***

# cities =["lahore", "islamabad", "karachi", "faisalabad", "mianwali"]
# City = input("Enter Your City : ").lower()
# for i in cities:
#     if City in i:
#      print("Yes")
#      break
#     else:
#      print("No")
#      break
# City==i:
#     print("Clean")
#     break
# else:
#     print("Not Clean")
#  break
# names2 = [i for i in names if  "adam" in i] # list comperhension
# cities = ["lahore", "islamabad", "karachi", "faisalabad", "mianwali"]
# city = input("Enter Your City : ").lower()
# slect = ["clean"  if i in city else "not clean" for i in cities  ]
# #slect = [ print("Cleaned!") if city==i else print("not cleaned")  for i in cities  ]

# print(slect)
# print([city])
 ##---asignment 07-----***

#Loops and ifelse statments

#Task 01 --Even Number Filter
# numbers = [1, 2, 3, 4, 5, 6]

# even_numbers = []
# for num in numbers:
#     if num % 2 == 0:
#         even_numbers.append(num)

# print(even_numbers)

# #Task 02 -- Pass / Fail System

# marks = [35, 67, 90, 45, 30]

# result = []
# for mark in marks:
#     if mark >= 40:
#         result.append("Pass")
#     else:
#         result.append("Fail")

# print(result)

# #Task 03 Positive & Negative Numbers
# numbers = [-5, 10, 0, -2, 8]

# for num in numbers:
#     if num > 0:
#         print(num, "Positive")
#     elif num < 0:
#         print(num, "Negative")
#     else:
#         print(num, "Zero")

# #Task 04 Name Strings Starting with 'A'

# names = ["Alice", "Bob", "Ankit", "John"]

# a_names = []
# for name in names:
#     if name.startswith('A'):
#         a_names.append(name)

# print(a_names)

# #Task 05 Count Even Numbers

# numbers = [1, 2, 4, 7, 8, 10]

# count = 0
# for num in numbers:
#     if num % 2 == 0:
#         count += 1

# print("Even count:", count)

# #Task06 Salary Bonus (10% bonus if salary > 50000)
# salaries = [40000, 60000, 80000]

# new_salaries = []
# for salary in salaries:
#     if salary > 50000:
#         new_salaries.append(salary * 1.10)
#     else:
#         new_salaries.append(salary)

# print(new_salaries)

# #task 07 Remove Empty Strings
# strings = ["Hello", "", "World", "", "Python"]

# cleaned = []
# for s in strings:
#     if s != "":
#         cleaned.append(s)

# print(cleaned)

# #08 Convert to Uppercase
# words = ["hello", "world"]

# upper_words = []
# for word in words:
#     upper_words.append(word.upper())

# print(upper_words)

# #09 Square Only Odd Numbers
# numbers = [1, 2, 3, 4, 5]

# squared_odds = []
# for num in numbers:
#     if num % 2 != 0:
#         squared_odds.append(num ** 2)

# print(squared_odds)
# #10  Check Prime Numbers
# numbers = [2, 3, 4, 5, 10, 13]

# for num in numbers:
#     if num > 1:
#         for i in range(2, num):
#             if num % i == 0:
#                 print(num, "Not Prime")
#                 break
#         else:
#             print(num, "Prime")
#     else:
#         print(num, "Not Prime")


# # List comprehenstion

# #Task 01 --Even Number Filter
# numbers = [1, 2, 3, 4, 5, 6]
# even_numbers = [num for num in numbers if num % 2 == 0]
# print(even_numbers)


# #Task 02 -- Pass / Fail System
# marks = [35, 67, 90, 45, 30]
# result = ["Pass" if mark >= 40 else "Fail" for mark in marks]
# print(result)


# #Task 03 Positive & Negative Numbers
# numbers = [-5, 10, 0, -2, 8]
# result = ["Positive" if n > 0 else "Negative" if n < 0 else "Zero" for n in numbers]
# print(result)


# #Task 04 Name Strings Starting with 'A'
# names = ["Alice", "jhon", "Ankit"]


# a_names = [name for name in names if name.startswith('A')]
# print(a_names)




# #Task 05 Count Even Numbers
# count = len([num for num in numbers if num % 2 == 0])
# print("Even count:", count)


# #Task06 Salary Bonus (10% bonus if salary > 50000)
# new_salaries = [salary * 1.10 if salary > 50000 else salary for salary in salaries]
# print(new_salaries)



# #task 07 Remove Empty Strings
# cleaned = [s for s in strings if s != ""]
# print(cleaned)


# #08 Convert to Uppercase
# upper_words = [word.upper() for word in words]
# print(upper_words)



# #09 Square Only Odd Numbers

# squared_odds = [num ** 2 for num in numbers if num % 2 != 0]
# print(squared_odds)


# #10  Check Prime Numbers

# def is_prime(n):
#     if n <= 1:
#         return False
#     for i in range(2, n):
#         if n % i == 0:
#             return False
#     return True

# result = ["Prime" if is_prime(num) else "Not Prime" for num in numbers]
# print(result)

#virtual enviorment in python

#++++tuples+++#
# cities =["lahore", "islamabad", "karachi", "faisalabad", "mianwali"]
# City = input("Enter Your City : ").lower()
# for i in cities:
#     if City in i:
#      print("Yes")
#      break
#     else:
#      print("No")
#      break
# City==i:
#     print("Clean")
#     break
# else:
#     print("Not Clean")
#  break
# names2 = [i for i in names if  "adam" in i] # list comperhension
# cities = ["lahore", "islamabad", "karachi", "faisalabad", "mianwali"]
# city = input("Enter Your City : ").lower()
# slect = ["clean"  if i in city else "not clean" for i in cities  ]
# #slect = [ print("Cleaned!") if city==i else print("not cleaned")  for i in cities  ]

# print(slect)
# print([city])

#***** Tupple Assignment******

# tup = ("lahore", "karachi", "islamabad", "faisalabad" , "sargodha")
# u=input("Enter your city: ").lower()
# s=("Clean" if u in tup else "Not clean" )
# print(s)

    
M = input("Enter your Math: " )
C = input("Enter your Compter: " )
E = input("Enter your English: " )
I = input("Enter your Islamic Studies: " )
B = input("Enter your Bio: " )
print(f"{M},{C},{E},{I},{B}")
s =[]
s.append(f"{M},{C},{E},{I},{B}")
s=tuple(s)
#print(s)
result=("Fail" if i<70 else "pass" for i in s )
print(result)

 
