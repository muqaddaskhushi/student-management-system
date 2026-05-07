# Student Management System

students = []

while True:
    print("\n--- Student Management System ---")
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Delete Student")
    print("5. Exit")

    choice = input("Enter your choice: ")

    # Add Student
    if choice == "1":
        name = input("Enter student name: ")
        roll = input("Enter roll number: ")
        department = input("Enter department: ")

        student = {
            "Name": name,
            "Roll No": roll,
            "Department": department
        }

        students.append(student)
        print("Student added successfully!")

    # View Students
    elif choice == "2":
        if len(students) == 0:
            print("No students found.")
        else:
            print("\nStudent Records:")
            for s in students:
                print(s)

    # Search Student
    elif choice == "3":
        search = input("Enter student name to search: ")

        found = False
        for s in students:
            if s["Name"].lower() == search.lower():
                print("Student Found:")
                print(s)
                found = True

        if not found:
            print("Student not found.")

    # Delete Student
    elif choice == "4":
        delete_name = input("Enter student name to delete: ")

        found = False
        for s in students:
            if s["Name"].lower() == delete_name.lower():
                students.remove(s)
                print("Student deleted successfully!")
                found = True
                break

        if not found:
            print("Student not found.")

    # Exit
    elif choice == "5":
        print("Program exited.")
        break

    else:
        print("Invalid choice. Try again.")
