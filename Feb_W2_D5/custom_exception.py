class NegativeNumberError(Exception):
    pass

try:
    num = int(input("Enter a positive number: "))

    if num < 0:
        raise NegativeNumberError

    print("You entered:", num)

except NegativeNumberError:
    print("Error: Negative numbers are not allowed.")

except ValueError:
    print("Error: Please enter a valid number.")