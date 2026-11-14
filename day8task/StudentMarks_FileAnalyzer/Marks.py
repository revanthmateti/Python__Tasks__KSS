# Open file in read mode
f = open("marks.txt", "r")

total = 0
count = 0

print("Student Records:")

for line in f:
    name, marks = line.split()

    marks = int(marks)

    print("Name:", name, "Marks:", marks)

    total = total + marks
    count = count + 1

f.close()

# Calculate average
if count > 0:
    average = total / count
    print("\nAverage Marks:", average)
else:
    print("No student records found")
