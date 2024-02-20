# a = {"Ironman", "Hulk", "Thor", "Captain"}
# print(a)
# print(type(a))

# for x in a:
#     print(x)

# Functions in sets
# add
# a.add("Spidy")

# pop
# a.pop()

# remove
# a.remove("Thor")

# discard
# a.discard("Hulk")

# b = a.copy()
# print(a)
# print(b)

a = {"Ironman", "Hulk", "Thor", "Captain"}
b = {"Superman", "Batman", "Wonder-Women"}
c = {"Hulk", "Thor"}

# isdisjoint
# print(a.isdisjoint(b))

# issubset
# print(a.issubset(c))
# print(c.issubset(a))

# issuperset
# print(a.issuperset(c))

# update
# a.update(c)
# print(a)

# clear
# print(a.clear())

# union
# print(a.union(b))

# difference
# print(a.difference(c))

# difference update
# a.difference_update(c)
# print(a)

# Intersection
# x = a.intersection(c)
# print(x)

# Intersection_update
# a.intersection_update(c)
# print(a)

# Symmetric Difference
# x = a.symmetric_difference(c)
# print(x)

# Symmetric Difference update
# a.symmetric_difference_update(c)
# print(a)

# -> Problem Solving😊

# 1. Write a program to find max and min in a set

# a = {12, 56, 43, 56, 78, 99, 9, 76}
# print("The minimum value is",min(a))
# print("The maximum value is",max(a))

# 2. Write a program to find common elements in three lists using sets
# a = [1, 5, 6, 8, 2]
# b = [4, 5, 6, 7]
# c = [1, 9, 6, 2, 5]

# print("The common elements in given three lists are",set(a) & set(b) & set(c))

# 3. Write a program to find difference between two sets
# a = {1, 5, 6, 8, 2}
# b = {1, 9, 6, 2, 5}
# print(a.difference(b))

# 4. Write a Python program to remove an item from a set if it is present in the set
# a = {1, 5, 6, 8, 2}
# a.discard(8)
# print(a)

# 5. Write a Python program to check if a set is a subset of another set.

a = {1, 2, 3, 4, 5, 6, 7}
b = {2, 3, 4}

print(b.issubset(a))




