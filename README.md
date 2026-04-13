# CU Data Processing System

## Overview
The CU Data Processing System is a Python-based application designed to process CSV files containing medical data. The system validates file structure and data, logs errors, prevents duplicate processing, and organises files into valid and invalid directories.

---

## Features

- CSV file validation:
  - Header validation
  - Row length validation
  - Reading range validation (0 – 9.9)
  - Duplicate batch ID detection

- File handling:
  - Valid files stored by date
  - Invalid files stored separately
  - Duplicate files skipped

- Logging:
  - All events logged to `logs/app.log`
  - Each log entry includes a unique GUID (via API)

- FTP Integration:
  - Download files from FTP server
  - Automatically process downloaded files

- Automation:
  - Script to generate test CSV files

- Testing:
  - Unit tests implemented using `pytest`

---

## Project Structure


cu_data_project/
│
├── src/ # Main application code
├── data/ # Input and output data
├── logs/ # Log files
├── tests/ # Unit tests
├── ftp_root/ # Simulated FTP server folder
├── Dockerfile # Container configuration
├── requirements.txt # Dependencies
├── generate_test_data.py # Automation script
├── ftp_server.py # FTP server script
└── README.md


---

## Requirements

- Python 3.13 (for local execution)
- Docker

---

## How to Run (Docker)

### 1. Build the Docker image

docker build -t cu-data-project .


### 2. Run the application

docker run -it cu-data-project


---

## How to Run (Locally)

### 1. Install dependencies

pip install -r requirements.txt


---

### 2. Start the FTP Server (Required for Option 3)

In a terminal:

python -m ftp_server.py


Expected output:

FTP server running on 127.0.0.1:2121

Keep this terminal open.

---

### 3. Open a New Terminal (if using vscode)

Shortcut:

ctrl + shift + ` or ctrl + shift + 5


---

### 4. Run the Application

python -m src.main


---

## Application Menu (How to Use)

When the program starts, you will see:


=== CU Data Processing System ===

Process a file
Process all local files
Download and process FTP files
View logs
Exit

---

## Option 1: Process a File (manual Input)

When prompted:

Enter file path:


Example (relative path):

data/source/sample.csv


Example (full path):

C:\Users\YourName...\cu_data_project\data\source\sample.csv


What happens:
- File is validated
- Moved to:
  - `data/valid/` if valid
  - `data/invalid/` if invalid
- Logged in `logs/app.log`

---

## Option 2: Process All Local Files

Select:

2


What it does:
- Processes all `.csv` files in:

data/source/


Example files:

data/source/MED_DATA_20230603140104.csv
data/source/sample.csv


---

## Option 3: Download and Process FTP Files

Make sure FTP server is running first.

Select:

3


What happens:
- Files are downloaded from:

ftp_root/


- Saved to:

data/source/


- Automatically validated and sorted

---

## Option 4: View Logs

Select:

4


Displays:

logs/app.log


Includes:
- Errors
- Warnings
- Info messages
- GUID for each log entry

---

## Option 5: Exit

Select:

5


Closes the application.

---

## Running Tests (TDD)

Run tests using:

pytest


Tests include:
- Header validation
- Empty file detection
- Row length validation
- Duplicate batch ID detection
- Reading validation

---

## Generate Test Data (Automation)

Run:

python generate_test_data.py


This will:
- Create valid CSV files
- Create invalid CSV files
- Save them into:

ftp_root/


---

## Logging System

Log file location:

logs/app.log


Includes:
- Timestamp
- Log level (INFO, ERROR, WARNING)
- Unique GUID (via API)

Example:

2026-04-09 - ERROR - [GUID] Invalid filename format


---

## CI/CD Pipeline

- Implemented using GitHub Actions
- Runs automatically on push
- Pipeline stages:
  - Checkout code
  - Install dependencies
  - Run tests

---

## Docker Notes

- Application runs inside a container
- No local setup required beyond Docker

---

## Example Full Workflow

1. Start FTP server:

python ftp_server.py


2. Open new terminal:

Ctrl + Shift + `


3. Run program:

python -m src.main


4. Select:

3

Files will be downloaded, validated, and sorted automatically.

---

## Author

Aldrin Dumas