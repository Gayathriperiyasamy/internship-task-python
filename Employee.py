class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

employee = Employee("Bob", 50000)
print(f"Employee: {employee.name}, Salary: {employee.salary}")
