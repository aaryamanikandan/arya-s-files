# Writing text to the file
with open("code.txt", "w") as file:
    file.write("PROGRAMING IN PYTHON")

# Reading the text from the file
with open("code.txt", "r") as file:
    content = file.read()

# Printing the content to the screen
print(content)
