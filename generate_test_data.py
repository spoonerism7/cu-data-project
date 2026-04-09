import csv
import os
import random
from datetime import datetime

OUTPUT_DIR = "ftp_root"  # or "data/source"

def generate_filename(valid=True):
    if valid:
        timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
        return f"MED_DATA_{timestamp}.csv"
    else:
        return "INVALID_NAME.csv"


def generate_valid_row(batch_id):
    timestamp = datetime.now().strftime("%H:%M:%S")
    readings = [round(random.uniform(0, 9.9), 3) for _ in range(10)]
    return [batch_id, timestamp] + readings


def generate_invalid_row():
    timestamp = datetime.now().strftime("%H:%M:%S")
    readings = [round(random.uniform(10, 20), 3) for _ in range(10)]  # invalid (>9.9)
    return [1, timestamp] + readings


def generate_csv(valid=True):
    os.makedirs(OUTPUT_DIR, exist_ok=True)

    file_name = generate_filename(valid)
    file_path = os.path.join(OUTPUT_DIR, file_name)

    with open(file_path, "w", newline="") as file:
        writer = csv.writer(file)

        if valid:
            headers = ["batch_id", "timestamp"] + [f"reading{i}" for i in range(1, 11)]
            writer.writerow(headers)

            for i in range(10):
                writer.writerow(generate_valid_row(i))

        else:
            headers = ["batch", "time"]  # wrong headers
            writer.writerow(headers)

            for _ in range(10):
                writer.writerow(generate_invalid_row())

    print(f"Generated file: {file_path}")


if __name__ == "__main__":
    print("Generating test data...\n")

    # Generate valid files
    for _ in range(2):
        generate_csv(valid=True)

    # Generate invalid files
    for _ in range(2):
        generate_csv(valid=False)

    print("\nDone.")