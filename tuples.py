# IMMUTABLE

# a = "apple", "mango", "banana"
# b = ("apple", "mango", "banana")
# print(type(a))
# print(type(b))

# c = "Rocky" #belongs to strings
# print(type(c))

# d = "Rocky", #belongs to class tuple
# print(type(d)) 

t = ("OnePlus", "Apple", "Vivo", "Redmi", "Oppo")
# print(t[1:3])
# print(t[:3])
# print(t[3:])

# print(t[::2])

# print(t[::-1]) # reverse the tuple

# print(t[2::-1])
print(t)

# with for loop
# for i in t:
#     print(i)

# along with range and length in for loop
# for i in range(len(t)):
#     print(t[i])

# along with while loop
# i = 0
# while i < len(t):
#     print(t[i])
#     i+=1

# Functions

# print("before conversion ",type(t))

# t = list(t)
# print("After conversion ",type(t))

# t.append("Samsung")
# print(t)

# conversion fro list -> tuple
# t = tuple(t)
# print(t)

print(t.count("Vivo"))

print(t.index("Redmi"))

