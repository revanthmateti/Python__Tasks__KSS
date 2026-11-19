def bonus(func):

    def wrapper(self):
        self.salary = self.salary + 5000
        func(self)

    return wrapper


class Employee:

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    @bonus
    def display(self):
        print("Employee Name:", self.name)
        print("Final Salary:", self.salary)


e1 = Employee("Ramesh", 30000)

e1.display()
