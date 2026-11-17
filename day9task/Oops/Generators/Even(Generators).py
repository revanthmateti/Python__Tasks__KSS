def even_numbers():

    num = 2

    while True:
        yield num
        num = num + 2


# Creating generator
result = even_numbers()

# Printing first 5 even numbers
for i in range(5):
    print(next(result))
