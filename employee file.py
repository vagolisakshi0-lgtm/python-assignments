def add_employee():
    emp_id = input("Enter Employee ID: ")
    name = input("Enter Employee Name: ")
    department = input("Enter Department: ")
    salary = input("Enter Salary: ")

    with open("employees.txt", "a") as file:
        file.write(emp_id + "," + name + "," + department + "," + salary + "\n")

    print("Employee added successfully!")


def view_employees():
    try:
        with open("employees.txt", "r") as file:
            records = file.readlines()

            if len(records) == 0:
                print("No employee records found.")
            else:
                print("\nEmployee Records")
                print("----------------")
                for record in records:
                    data = record.strip().split(",")
                    print("ID:", data[0])
                    print("Name:", data[1])
                    print("Department:", data[2])
                    print("Salary:", data[3])
                    print("----------------")

    except FileNotFoundError:
        print("No employee records found.")


def search_employee():
    search_id = input("Enter Employee ID to search: ")
    found = False

    try:
        with open("employees.txt", "r") as file:
            for record in file:
                data = record.strip().split(",")

                if data[0] == search_id:
                    print("\nEmployee Found")
                    print("ID:", data[0])
                    print("Name:", data[1])
                    print("Department:", data[2])
                    print("Salary:", data[3])
                    found = True
                    break

        if not found:
            print("Employee not found.")

    except FileNotFoundError:
        print("No employee records found.")


def update_employee():
    update_id = input("Enter Employee ID to update: ")
    found = False

    try:
        with open("employees.txt", "r") as file:
            records = file.readlines()

        with open("employees.txt", "w") as file:
            for record in records:
                data = record.strip().split(",")

                if data[0] == update_id:
                    print("Employee found.")

                    department = input("Enter new Department: ")
                    salary = input("Enter new Salary: ")

                    file.write(data[0] + "," + data[1] + "," +
                               department + "," + salary + "\n")

                    found = True
                else:
                    file.write(record)

        if found:
            print("Employee updated successfully!")
        else:
            print("Employee not found.")

    except FileNotFoundError:
        print("No employee records found.")


def delete_employee():
    delete_id = input("Enter Employee ID to delete: ")
    found = False

    try:
        with open("employees.txt", "r") as file:
            records = file.readlines()

        with open("employees.txt", "w") as file:
            for record in records:
                data = record.strip().split(",")

                if data[0] == delete_id:
                    found = True
                else:
                    file.write(record)

        if found:
            print("Employee deleted successfully!")
        else:
            print("Employee not found.")

    except FileNotFoundError:
        print("No employee records found.")
while True:
    print("\n===== Employee Record Management System =====")
    print("1. Add Employee")
    print("2. View Employees")
    print("3. Search Employee")
    print("4. Update Employee")
    print("5. Delete Employee")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_employee()

    elif choice == "2":
        view_employees()

    elif choice == "3":
        search_employee()

    elif choice == "4":
        update_employee()

    elif choice == "5":
        delete_employee()

    elif choice == "6":
        print("Program closed.")
        break

    else:
        print("Invalid choice! Please try again.")
