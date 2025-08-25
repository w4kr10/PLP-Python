#Error Handling
filename = input("Enter the filename to read-: ")

try:
    with open(filename, 'r') as infile:
        content = infile.read()
except FileNotFoundError:
    print(f"Error: The file '{filename}' does not exist.")
except IOError:
    print(f"Error: The file '{filename}' could not be read.")
else:
    # File Read & Write
    modified_content = content[::-1]
    new_filename = "modified_" + filename
    try:
        with open(new_filename, 'w') as outfile:
            outfile.write(modified_content)
        print(f"Modified file written to '{new_filename}' successfully!")
    except IOError:
        print(f"Error: Could not write to '{new_filename}'.")