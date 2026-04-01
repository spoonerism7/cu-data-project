import csv

def load_csv(file_path):
    with open(file_path, newline='', encoding='utf-8-sig') as file:
        reader = csv.reader(file)
        data = list(reader)
    return data