# Must have exactly one of create/read/write/append mode and at the
import os.path

# Write into a file
with open("../MockData/testdata.txt", "w") as file:
    file.write("Hello World")


# Store file path with name in a variable
file_name = "../MockData/EgCreated.txt"

# Create file and handle it if it already exists
try:
    with open(file_name, "x") as file:
        file.write("This file is created using 'x' keyword\n")
        file.write("Using x keyword it creates and opens file to write into it")
except Exception as e:
    print("File already exists use different file name or path to store")

# Try block to read a file and handle it if it does not exist
try:
    # Read the file content
    with open(file_name, "r") as file:
        content = file.read()
        print(content)
# Except block will execute if any error occurred while running try block
except Exception as e:
    print(e)

# Finally block will always execute even if try or except any block executed
finally:
    if os.path.exists(file_name):
        os.remove(file_name)  # Will delete the file
        print("File Deleted successfully....!")
    else:
        print("File not found...!")
