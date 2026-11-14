# Student Marks Management System

# 1. Tuple - Store subject names
subjects = ("Math", "Science", "English")

# 2. Set - Store unique student names
students = set()

# 3. Dictionary - Store student names and marks
student_marks = {}


# 4. Recursive function to calculate total marks
def total_marks(marks):

    # Base condition
    if len(marks) == 0:
        return 0

    # Recursive call
    return marks[0] + total_marks(marks[1:])


# 5. Function to add a student
def add_student():

    try:
        name = input("Enter student name: ")

        # Check duplicate student name
        if name in students:
            print("Student already exists.")
            return

        marks = []

        # Get marks for three subjects
        for subject in subjects:
            mark = int(input("Enter marks for " + subject + ": "))
            marks.append(mark)

        # Store student name and marks
        students.add(name)
        student_marks[name] = marks

        print("Student added successfully!")

    except ValueError:
        print("Invalid input! Please enter numeric marks.")


# 6. Function to display all students
def display_students():

    if len(student_marks) == 0:
        print("No student records found.")

    else:
        for name, marks in student_marks.items():
            print(name, ":", marks)


# 7. Function to calculate average marks
def calculate_average():

    try:
        name = input("Enter student name to calculate average: ")

        # Check whether student exists
        if name not in student_marks:
            raise NameError

        marks = student_marks[name]

        # Check marks data type
        if not isinstance(marks, list) or not all(isinstance(m, int) for m in marks):
            raise TypeError

        # Calculate total using recursion
        total = total_marks(marks)

        # Calculate average
        average = total / len(marks)

        print("Total Marks:", total)
        print("Average Marks:", average)

    except NameError:
        print("Student name not found.")

    except ZeroDivisionError:
        print("Cannot divide by zero.")

    except TypeError:
        print("Marks data type error.")


# 8. Main menu using while loop
while True:

    print("\n1. Add Student")
    print("2. Display Students")
    print("3. Calculate Average")
    print("4. Exit")

    try:
        choice = int(input("Enter choice: "))

        if choice == 1:
            add_student()

        elif choice == 2:
            display_students()

        elif choice == 3:
            calculate_average()

        elif choice == 4:
            print("Program exited.")
            break

        else:
            print("Invalid choice! Please select 1 to 4.")

    except ValueError:
        print("Please enter a valid menu number.")
