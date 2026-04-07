import os,csv,sys
from src.validator import validate_file, validate_filename
from src.file_manager import load_csv
from src.logger import setup_logger

logger = setup_logger()

def process_file(file_path):
    file_name = os.path.basename(file_path)

    if not validate_filename(file_name):
        message = "Invalid filename format"
        print(message)
        logger.error(f"Invalid filename format: {file_name}")
        return False
    
    data = load_csv(file_path)

    is_valid, message = validate_file(data)

    print(message)

    if is_valid:
        logger.info(message)
    else:
        logger.error(message)
    
    return is_valid

def show_menu():
    print("\n=== CU Data Processing System ===")
    print("1. Process a file")
    print("2. View logs")
    print("3. Exit")

def view_logs():
    try:
        with open("logs/app.log", "r") as file:
            content = file.read()
            if content:
                print("\n--- Log File ---")
                print(content)
            else:
                print("Log file is empty")
    except FileNotFoundError:
        print("No log file found")

if __name__ == "__main__":
    while True:
        show_menu()
        choice = input("Select an option: ")

        if choice == "1":
            file_path = input("Enter file path: ")
            process_file(file_path)
            print()

        elif choice == "2":
            view_logs()

        elif choice == "3":
            print("Exiting program...")
            break

        else:
            print("Invalid option, please try again.")