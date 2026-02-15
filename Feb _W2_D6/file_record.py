file = open("records.txt", "a")

name = input("Enter name: ")
age = input("Enter age: ")

file.write("Name: " + name + ", Age: " + age + "\n")
file.close()

print("Record saved.")
