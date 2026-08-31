def add_student():
    name=input("enter student name:")
    age=input("enter student age:")
    course=input("enter course:")
    marks=input("enter marks:")
    with open("students.txt","a")as file:
        file.write(f"{name},{age},{course},{marks}\n")
        print("student record added successfully!")
def view_students():
    try:
        with open("student.txt","r")as file:
            data=file.read()
            if data:
                print("\n---student records---")
                print(data)
            else:
                print("no students records found")
    except FileNotFoundError:
        print("no file found.Add a student first.")
def search_student():
    search_name=input("enter student name to search:")
    try:
        with open("students.txt","r")as file:
            found=False
            for line in file:
                data=line.strip().split(",")
                if data[0].lower()==search_name.lower():
                    print("\nstudent found!")
                    print("Name:",data[0])
                    print("Age:",data[1])
                    print("Course:",data[2])
                    print("Marks:",data[3])
                    found=True
                    break
                if not found:
                    print("student not found.")
    except FileNotFoundError:
        print("No student records found.")
while True:
    print("\n=====student record manager====")
    print("1.add student")
    print("2.view student")
    print("3.search student")
    print("4.Exit")
    choice=input("enter your choice:")
    if choice=="1":
        add_student()
    elif choice=="2":
        view_students()
    elif choice=="3":
        search_student()
    elif choice=="4":
        print("program ended.")
        break
    else:
        print("invalid choice!")
                
