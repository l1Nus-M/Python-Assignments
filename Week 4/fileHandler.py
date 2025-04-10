def read_and_write_file():
    try:
        # Ask the user for the filename
        filename = input("Enter the filename to read: ")

        # Open and read the file
        with open(filename, "r") as file:
            content = file.read()

        # Modify content (example: convert to uppercase)
        modified_content = content.upper()

        # Create a new filename
        new_filename = "modified_" + filename

        # Write the modified content to the new file
        with open(new_filename, "w") as new_file:
            new_file.write(modified_content)

        print(f"Successfully created '{new_filename}' with modified content!")

    except FileNotFoundError:
        print("Error: The file does not exist. Please check the filename and try again.")
    except PermissionError:
        print("Error: Permission denied. You may not have access to this file.")
    except Exception as e:
        print(f"❌ An unexpected error occurred: {e}")

# Run the function
read_and_write_file()
