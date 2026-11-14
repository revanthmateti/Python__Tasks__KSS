# Open file in read mode
f = open("article.txt", "r")

# Read all contents
data = f.read()

# Count words, lines and characters
words = len(data.split())
lines = len(data.splitlines())
characters = len(data)

# Display results
print("Total Words:", words)
print("Total Lines:", lines)
print("Total Characters:", characters)

f.close()
