

# Open a text file in read mode
with open('sample.txt', 'r') as file:
    # Read the entire content of the file
    content = file.read()
    print(content)


# Writing to a Text File:

# Open a text file in write mode
with open('output.txt', 'w') as file:
    # Write content to the file
    file.write('Hello, world!\n')
    file.write('This is a sample text file.\n')


# Appending to a Text File:

# Open a text file in append mode
with open('output.txt', 'a') as file:
    # Append content to the file
    file.write('Additional content.\n')

# Reading and Writing Binary Files:

# Reading a binary file
with open('binary_input.jpg', 'rb') as file:
    binary_data = file.read()

# Writing binary data to a new file
with open('binary_output.jpg', 'wb') as file:
    file.write(binary_data)


# Reading Line by Line:

# Open a text file in read mode
with open('sample.txt', 'r') as file:
    # Read and process each line in the file
    for line in file:
        print(line.strip())  # Strip removes newline characters


# Using try and except for Error Handling:


try:
    with open('nonexistent_file.txt', 'r') as file:
        content = file.read()
        print(content)
except FileNotFoundError as e:
    print(f"File not found: {e}")

