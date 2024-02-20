Employee_Data = {"name" : "John", "age" : 24, "gender":"male"}
# print(Employee_Data["gender"])

# Iteration in Dictionary
# using value function
# for x in Employee_Data.values():
#     print(x)

# printing all the value name one by one
# for x in Employee_Data:
#     print(Employee_Data[x])


# using items function
# for x,y in Employee_Data.items():
#     print(x,"->",y)


#- Iteration in dictionaries
# Student = {"name":"John", "class":"6th", "roll_no":23}

# setdefault
# x = Student.setdefault("roll_no", 24)
# print(x)

# Nested Dictionaries
# Employees = {1 : {"Name":"John", "Age":"23", "Gender" : "male"},
#              2 : {"Name" : "Lisa", "Age" : "24", "Gender" : "female"},
#              3 : {"Name" : "peter", "Age" : "25", "Gender" : "male"}}

# print(Employees[2]["Gender"])

#?- Problem Solving

# 1. sort a dictionary by value
# a = {"a" : 12,"b" : 17,"c" : 11,"d" : 9,"e" : 43}
# a = sorted(a.values())
# print(a)

# 2. write a python script to print a dictionary where the keys are numbers between 1 ans 15 ans the values are square of keys

# a = {}
# for i in range(1, 16):
#     a[i] = i**2

# print(a)

# 3.Write a program to multiply all the items in a dictionary
# a = {"a" : 1, "b" : 2, "c" : 3, "d" : 4, "e" : 5}
# product = 1
# for i in a:
#     product *= a[i]
# print(product)

# 4. Write a python program to sort a dictionary by key
# a = {12 : "a", 56 : "b", 23 : "c", 48 : "d", 91 : "e"}

# a = sorted(a.keys())
# print(a)
