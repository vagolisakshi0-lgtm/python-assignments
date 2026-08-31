while True:
    name = input("Enter student name: ")
    age = input("Enter age: ")
    course = input("Enter course: ")

    file = open("student.txt", "a")

    file.write("Student: " + name + "\n")
    file.write("Age: " + age + "\n")
    file.write("Course: " + course + "\n")
    file.write("------------------\n")

    file.close()

    choice = input("Do you want to enter another student? (yes/no): ")

    if choice.lower() == "no":
        break

print("Student details saved successfully!")
