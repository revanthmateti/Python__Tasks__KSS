def find_sum(numbers):
    total = 0

    for num in numbers:
        total = total + num

    return total

my_list = [10, 20, 30, 40]

print("Sum:", find_sum(my_list))
