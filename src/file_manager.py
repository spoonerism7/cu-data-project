import csv, os, shutil
from datetime import datetime

def load_csv(file_path):
    try:
        with open(file_path, newline='', encoding='utf-8-sig') as file:
            reader = csv.reader(file)
            return list(reader)
    except FileNotFoundError:
        print("File not found")
    return []

TRACK_FILE = "data/processed_files.txt"

def get_processed_files():
    if not os.path.exists(TRACK_FILE):
        return set()
    
    with open(TRACK_FILE, "r") as file:
        return set(line.strip() for line in file)

def mark_file_processed(file_name):
    os.makedirs("data", exist_ok=True)
    
    with open(TRACK_FILE, "a") as file:
        file.write(file_name + "\n")

def get_all_files_in_folder(folder_path):
    if not os.path.exists(folder_path):
        return []
    
    files = []
    for file in os.listdir(folder_path):
        if file.endswith(".csv"):
            files.append(os.path.join(folder_path, file))
    
    return files

def move_file(file_path, is_valid):
    file_name = os.path.basename(file_path)

    if is_valid:
        # Create date-based folder
        today = datetime.now().strftime("%Y-%m-%d")
        target_dir = os.path.join("data", "valid", today)
    else:
        target_dir = os.path.join("data", "invalid")

    os.makedirs(target_dir, exist_ok=True)

    new_path = os.path.join(target_dir, file_name)

    shutil.move(file_path, new_path)