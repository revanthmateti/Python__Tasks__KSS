def generate_numbers(n):

    for i in range(1, n + 1):
        yield i


# Calling generator
result = generate_numbers(5)

for num in result:
    print(num)
