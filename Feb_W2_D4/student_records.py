file = open("students.txt", "w")

name = input("Enter student name: ")
usn = input("Enter USN: ")
branch = input("Enter branch: ")

file.write("Name: " + name + "\n")
file.write("USN: " + usn + "\n")
file.write("Branch: " + branch + "\n")

file.close()

print("Student record saved successfully.")