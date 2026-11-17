class Result:

    def calculate(self, m1, m2, m3=0):

        if m3 == 0:
            total = m1 + m2
            print("Total Marks:", total)
        else:
            total = m1 + m2 + m3
            print("Total Marks:", total)


r = Result()

# Two subjects
r.calculate(80, 90)

# Three subjects
r.calculate(80, 90, 85)
