while True:
    name = input("Enter name: ")
    age = input("Enter age: ")
    course = input("Enter course: ")

    f1 = open("name.txt", "a")
    f1.write(name + "\n")
    f1.close()

    f2 = open("name.txt", "a")
    f2.write(age + "\n")
    f2.close()

    f3 = open("name.txt", "a")
    f3.write(course + "\n")
    f3.close()

    choice = input("Do you want to continue? (yes/no): ")

    if choice == "no":
        break
