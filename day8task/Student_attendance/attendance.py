name = input("Enter student name: ")

# Append student name to file
f = open("attendance.txt", "a")
f.write(name + "\n")
f.close()

# Display file contents
f = open("attendance.txt", "r")

print("\nAttendance Records:")
print(f.read())

f.close()
