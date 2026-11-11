students = {
    "Rahul": 85,
    "Amit": 90,
    "Priya": 78
}

students["Sneha"] = 95

students["Rahul"] = 92

for name, marks in students.items():
    print(name, ":", marks)
