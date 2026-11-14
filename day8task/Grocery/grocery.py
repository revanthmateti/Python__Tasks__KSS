# Open file in write mode
f = open("grocery.txt", "w")

n = int(input("How many items do you want to add? "))

for i in range(n):
    item = input("Enter grocery item: ")
    f.write(item + "\n")

f.close()

# Display grocery items
f = open("grocery.txt", "r")

print("\nGrocery List:")
print(f.read())

f.close()
