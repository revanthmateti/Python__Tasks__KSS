class Student:

    def display(self):
        print("Name:", self.name)
        print("Roll Number:", self.rollno)
        print("Marks:", self.marks)


# Creating objects
s1 = Student()
s1.name = "Ramesh"
s1.rollno = 101
s1.marks = 85

s2 = Student()
s2.name = "Sita"
s2.rollno = 102
s2.marks = 90

s3 = Student()
s3.name = "Rahul"
s3.rollno = 103
s3.marks = 78

# Displaying details
s1.display()
s2.display()
s3.display()
