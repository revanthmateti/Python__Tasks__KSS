# Open file in read mode
f = open("employees.txt", "r")

highest_salary = 0
highest_employee = ""

print("Employee Details:")

for line in f:
    name, salary = line.split()

    salary = int(salary)

    print("Name:", name, "Salary:", salary)

    if salary > highest_salary:
        highest_salary = salary
        highest_employee = name

f.close()

# Display highest salary employee
print("\nHighest Salary Employee:")
print("Name:", highest_employee)
print("Salary:", highest_salary)

# Add new employee
name = input("\nEnter new employee name: ")
salary = int(input("Enter employee salary: "))

# Append new employee record
f = open("employees.txt", "a")
f.write(name + " " + str(salary) + "\n")
f.close()

print("New employee added successfully!")
