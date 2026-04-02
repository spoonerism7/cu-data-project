import csv
import sys
from src.validator import validate_file
from src.file_manager import load_csv
from src.logger import setup_logger

logger = setup_logger()

def process_file(file_path):
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
    print("2. Exit")


if __name__ == "__main__":
    while True:
        show_menu()
        choice = input("Select an option: ")

        if choice == "1":
            file_path = input("Enter file path: ")
            process_file(file_path)

        elif choice == "2":
            print("Exiting program...")
            break

        else:
            print("Invalid option, please try again.")