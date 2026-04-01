import csv

def load_csv(file_path):
    try:
        with open(file_path, newline='', encoding='utf-8-sig') as file:
            reader = csv.reader(file)
            return list(reader)
    except FileNotFoundError:
        print("File not found")
    return []