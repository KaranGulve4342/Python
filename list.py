a = ["Thor", "Captain", "IronMan", "Hulk", "Doctor Strange"]

# print (a)

# print(len(a))

# a.append("Vanda")
# print(a)

# to add to a specifi position
# a.insert(3, "Vision")
# print(a)

# to remove from the list
# a.remove("Hulk")
# print(a)

# to remove from a certain location
# print(a.pop(1))
# print(a)

# to create a copy of list
# b = []
# print(b)
# b = a.copy()
# print(b)

# to access an element
# print(a.index("IronMan"))

# to extent the list
# c = ["vision", "spidy"]
# a.extend(c)
# print(a)

# to reverse a list
# a.reverse()
# print(a)

# to sort the list
# a.sort()
# print(a)

# d = [1, 4, 5, 2, 3, 0]
# d.sort()
# print(d)

# to clear all the data from the list
# a.clear()
# print(a)

# LIST COMPREHENSION

l1 = [30, 40, 50, 10]
l2 = []

# for i in l1:
#     l2.append(i)

# print(l2)

# l3 = [i for i in l1] #list comprehension method
# l4 = [i for i in l1 if i > 30] #list comprehension method
# print(l3)
# print(l4)


# swapping elements in the list
# l1[0], l1[2] = l1[2], l1[0]
# print(l1)

# add a new value at specific position
# l1.insert(3, 99)
# print(l1)

# delete a value from specific position
l1.pop(2)
print(l1)

