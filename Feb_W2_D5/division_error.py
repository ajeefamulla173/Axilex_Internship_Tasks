
try:
    a = int(input("Enter numerator: "))
    b = int(input("Enter denominator: "))

    result = a / b
    print("Result is:", result)

except ZeroDivisionError:
    print("Error: Cannot divide by zero.")

except ValueError:
    print("Error: Please enter valid numbers.")
