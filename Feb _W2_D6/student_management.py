students = {}

while True:
    print("\n1. Add Student")
    print("2. View Students")
    print("3. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        name = input("Enter name: ")
        marks = input("Enter marks: ")
        students[name] = marks
        print("Student added.")

    elif choice == "2":
        print("Student Records:", students)

    elif choice == "3":
        break

    else:
        print("Invalid choice.")
