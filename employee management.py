class Employee:
    def __init__(self, name, emp_id, salary):
        self.name = name
        self.emp_id = emp_id
        self.salary = salary
    def calculate_pay(self):
        return self.salary
    def display(self):
        print("Name:", self.name)
        print("Employee ID:", self.emp_id)
        print("Salary:", self.calculate_pay())
class Manager(Employee):
    def __init__(self, name, emp_id, salary, team_size):
        super().__init__(name, emp_id, salary)
        self.team_size = team_size

    def calculate_pay(self):
        return self.salary + (500 * self.team_size)
class Developer(Employee):
    def __init__(self, name, emp_id, salary, programming_language):
        super().__init__(name, emp_id, salary)
        self.programming_language = programming_language

    def calculate_pay(self):
        return self.salary + 1000
class Intern(Employee):
    def __init__(self, name, emp_id, salary):
        super().__init__(name, emp_id, salary)

    def calculate_pay(self):
        return self.salary
manager = Manager("Sakshi", 101, 60000, 5)
developer = Developer("Vaishu", 102, 50000, "Python")
intern = Intern("Aishu", 103, 15000)
print("Manager Details")
manager.display()
print("\nDeveloper Details")
developer.display()
print("\nIntern Details")
intern.display()
