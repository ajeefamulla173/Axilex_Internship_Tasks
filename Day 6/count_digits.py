# Program to count digits in a number

num = int(input("Enter a number: "))
count = 0

while num > 0:
    count += 1
    num = num // 10

print("Total digits are:", count)
