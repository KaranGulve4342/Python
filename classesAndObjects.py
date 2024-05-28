# Classes and Objects in Python

class MyClass:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    x = 5
    
name = input("Enter your name: ")
age = int(input("Enter your age: "))
    
p1 = MyClass(name, age)
print(p1.name)
print(p1.age)  