students = {
    "Rahul": 85,
    "Ravi": 90,
    "Arjun": 78
}

highest_student = max(students, key=students.get)

print("Highest marks student:", highest_student)
print("Marks:", students[highest_student])
