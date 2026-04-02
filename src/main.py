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

if __name__ == "__main__":
    file_path = "data/valid/sample.csv" # change to test
    process_file(file_path)