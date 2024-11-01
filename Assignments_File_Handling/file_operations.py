import os

def create_mock_files():
    mock_files = {
        'file1.txt': "Hello, this is File 1.\nDon't change this line.\nThis is another line.",
        'file2.txt': "Welcome to File 2.\nDon't change this line.\nYet another line here.",
        'file3.txt': "File 3 contents here.\nDon't change this line.\nMore text in file 3."
    }
    
    for filename, content in mock_files.items():
        try:
            if not os.path.exists(filename):
                with open(filename, 'w') as f:
                    f.write(content)
        except OSError as e:
            print(f"Error: Could not create file {filename}. {e}")

def read_file(filename):
    try:
        if not filename.endswith('.txt'):
            print("Error: Please enter a valid .txt filename.")
            return
        with open(filename, 'r') as f:
            print(f"\nContents of {filename}:\n")
            print(f.read())
    except FileNotFoundError:
        print("Error: File not found.")
    except PermissionError:
        print("Error: Permission denied when trying to read the file.")
    except OSError as e:
        print(f"Error: An unexpected error occurred while reading the file. {e}")

def edit_file(filename):
    try:
        if not filename.endswith('.txt'):
            print("Error: Please enter a valid .txt filename.")
            return
        with open(filename, 'r') as f:
            lines = f.readlines()
        
        # Display current contents
        print(f"\nCurrent contents of {filename}:\n")
        for i, line in enumerate(lines):
            print(f"{i + 1}: {line.strip()}")
        
        while True:
            try:
                # Ask user which line to edit
                line_number = int(input("\nEnter the line number you want to edit: "))
                if line_number < 1 or line_number > len(lines):
                    print("Invalid line number. Please enter a number between 1 and {}.".format(len(lines)))
                else:
                    break
            except ValueError:
                print("Error: Please enter a valid number.")
                
        # Check if the line is restricted
        if "Don't change this line." in lines[line_number - 1]:
            print("You are not allowed to change this line.")
            return
        
        # Get new content for the line
        new_content = input("Enter the new content for the line: ")
        confirm = input(f"Are you sure you want to change line {line_number} to: '{new_content}'? (yes/no): ").lower()
        if confirm != 'yes':
            print("Edit cancelled.")
            return
        
        lines[line_number - 1] = new_content + "\n"
        
        # Write changes back to the file
        with open(filename, 'w') as f:
            f.writelines(lines)
        print(f"\n{filename} has been updated successfully.")
    except FileNotFoundError:
        print("Error: File not found.")
    except PermissionError:
        print("Error: Permission denied when trying to edit the file.")
    except OSError as e:
        print(f"Error: An unexpected error occurred while editing the file. {e}")

def add_file():
    try:
        filename = input("\nEnter the name of the new file (e.g., newfile.txt): ")
        if not filename.endswith('.txt'):
            print("Error: Please enter a valid .txt filename.")
            return
        if os.path.exists(filename):
            print("Error: A file with this name already exists.")
            return
        
        content = input("Enter the content for the new file: ")
        with open(filename, 'w') as f:
            f.write(content)
        print(f"\n{filename} has been created successfully.")
    except PermissionError:
        print("Error: Permission denied when trying to create the file.")
    except OSError as e:
        print(f"Error: An unexpected error occurred while creating the file. {e}")