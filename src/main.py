import csv
from src.validator import (
    validate_headers,
    validate_not_empty,
    validate_row_length,
    validate_unique_batch_ids,
    validate_readings
)
from src.file_manager import load_csv
from src.logger import setup_logger

logger = setup_logger()

def process_file(file_path):
    data = load_csv(file_path)

    # check empty file
    if not validate_not_empty(data):
        print("File is empty")
        return False
    
    headers = data[0]
    rows = data[1:]

    # header validation
    if not validate_headers(headers):
        print("Invalid headers")
        logger.error("Invalid headers")
        return False

    # row length validation
    for row in rows:
        if not validate_row_length(row):
            print("Invalid row length")
            return False
        
    # convert rows to dict for batch_id validation
    dict_rows = [
        {"batch_id": row[0]}
        for row in rows
    ]

    if not validate_unique_batch_ids(dict_rows):
        print("Duplicate batch IDs found")
        return False
    
    # reading validation
    for row in rows:
        readings = row[2:]
        if not validate_readings(readings):
            print("Invalid reading values")
            return False
        
    print("File is valid")
    logger.info("File is valid")
    return True

if __name__ == "__main__":
    file_path = "data/valid/sample.csv" # change to test
    process_file(file_path)

