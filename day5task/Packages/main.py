#This is the main program. We import functions from both modules

from utilities.math_operations import add, multiply
from utilities.string_operations import uppercase, count_characters

# Mathematical operations
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

print("Addition:", add(num1, num2))
print("Multiplication:", multiply(num1, num2))

# String operations
text = input("Enter a string: ")

print("Uppercase:", uppercase(text))
print("Character count:", count_characters(text))
