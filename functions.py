# def hello():
#     print("Hello World")
# hello()

# def add(a, b):
#     print("Addition", a+b)
# add(45, 54)

# Recursive functions

def fact(n):
    if n <= 1:
        return 1
    else:
        return (n * fact(n-1))
    
print(fact(7))
    