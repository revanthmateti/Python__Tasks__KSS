employees = [
    {"name": "John", "age": 25, "salary": 30000},
    {"name": "Alice", "age": 30, "salary": 50000},
    {"name": "Bob", "age": 28, "salary": 40000},
    {"name": "David", "age": 35, "salary": 60000}
]

# 1. Highest salary employee

highest = max(employees, key=lambda x: x["salary"])

print("Highest salary employee:", highest)


# 2. Salary greater than 35000

print("Employees with salary greater than 35000:")

for emp in employees:
    if emp["salary"] > 35000:
        print(emp)


# 3. Average salary

total = 0

for emp in employees:
    total += emp["salary"]

average = total / len(employees)

print("Average salary:", average)


# 4. Employee names only

names = []

for emp in employees:
    names.append(emp["name"])

print("Employee names:", names)
