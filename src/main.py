import os,csv,sys
from src.validator import validate_file, validate_filename
from src.file_manager import load_csv, get_processed_files, mark_file_processed, mark_file_processed, get_all_files_in_folder
from src.logger import setup_logger
from src.ftp_client import download_files_from_ftp

logger = setup_logger()

def process_file(file_path):

    file_name = os.path.basename(file_path)

    if not validate_filename(file_name):
        message = "Invalid filename format"
        print(message)
        logger.error(f"Invalid filename format: {file_name}")
        return False
    
    processed_files = get_processed_files()

    if file_name in processed_files:
        message = "File has already been processed"
        print(message)
        logger.warning(f"Duplicate file skipped: {file_name}")
        return False
    
    data = load_csv(file_path)

    is_valid, message = validate_file(data)

    print(message)

    if is_valid:
        logger.info(message)
    else:
        logger.error(message)
    
    mark_file_processed(file_name)

    return is_valid

def process_all_files(folder_path="data/source"):
    files = get_all_files_in_folder(folder_path)

    if not files:
        print("No files found in source folder")
        return

    print(f"\nProcessing {len(files)} file(s)...\n")

    for file_path in files:
        print(f"Processing: {file_path}")
        process_file(file_path)
        print()

def process_files_from_ftp():
    host = "127.0.0.1"
    username = "user"
    password = "12345"
    remote_dir = "/"
    local_dir = "data/source"

    print("\nConnecting to FTP server...\n")

    files = download_files_from_ftp(host, username, password, remote_dir, local_dir)

    if not files:
        print("No files downloaded")
        return

    print(f"Downloaded {len(files)} file(s)\n")

    for file_path in files:
        print(f"Processing: {file_path}")
        process_file(file_path)
        print()

def show_menu():
    print("\n=== CU Data Processing System ===")
    print("1. Process a file")
    print("2. Process all local files")
    print("3. Download and process FTP files")
    print("4. View logs")
    print("5. Exit")

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
            process_all_files()

        elif choice == "3":
            process_files_from_ftp()

        elif choice == "4":
            view_logs()

        elif choice == "5":
            print("Exiting program...")
            break

        else:
            print("Invalid option, please try again.")