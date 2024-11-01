import file_operations
import user_interface

def main_script():
    try:
        file_operations.create_mock_files()
        user_interface.main()
    except Exception as e:
        print(f"Error: An unexpected error occurred in the main script. {e}")

if __name__ == "__main__":
    main_script()
