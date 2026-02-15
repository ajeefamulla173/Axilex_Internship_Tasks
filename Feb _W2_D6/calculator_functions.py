def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def mul(a, b):
    return a * b

def div(a, b):
    return a / b


x = int(input("Enter first number: "))
y = int(input("Enter second number: "))

print("Addition:", add(x, y))
print("Subtraction:", sub(x, y))
print("Multiplication:", mul(x, y))
print("Division:", div(x, y))
