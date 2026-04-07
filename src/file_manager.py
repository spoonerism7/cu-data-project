import csv, os

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