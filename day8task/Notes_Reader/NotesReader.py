# Open file in read mode
f = open("notes.txt", "r")

# Read all contents
data = f.read()

# Display contents
print("Daily Notes:")
print(data)

f.close()
