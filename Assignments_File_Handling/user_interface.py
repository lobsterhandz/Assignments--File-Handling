import file_operations

def display_file_list():
    files = ['file1.txt', 'file2.txt', 'file3.txt']
    print("\nAvailable files:")
    for file in files:
        print(f"- {file}")

def main():
    while True:
        print("\nWhat would you like to do?")
        print("1. View file list")
        print("2. Read a file")
        print("3. Edit a file")
        print("4. Add a new file")
        print("5. Exit")
        
        choice = input("\nEnter your choice (1-5): ")
        
        try:
            if choice == '1':
                display_file_list()
            elif choice == '2':
                display_file_list()
                filename = input("\nEnter the filename to read: ")
                file_operations.read_file(filename)
            elif choice == '3':
                display_file_list()
                filename = input("\nEnter the filename to edit: ")
                file_operations.edit_file(filename)
            elif choice == '4':
                file_operations.add_file()
            elif choice == '5':
                print("\nGoodbye!")
                break
            else:
                print("\nInvalid choice. Please enter a number between 1 and 5.")
        except Exception as e:
            print(f"Error: An unexpected error occurred. {e}")