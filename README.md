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
  - Generate test CSV files directly from the application

- Testing:
  - Unit tests implemented using `pytest`

---

## Project Structure

cu_data_project/  
│  
├── src/                  # Main application code  
├── data/                 # Input and output data  
├── logs/                 # Log files  
├── tests/                # Unit tests  
├── ftp_root/             # Simulated FTP server folder  
├── Dockerfile            # Container configuration  
├── requirements.txt      # Dependencies  
├── generate_test_data.py # Automation script  
├── ftp_server.py         # FTP server script  
└── README.md  

---

## Requirements

- Python 3.13 (for local execution)
- Docker

---

## Windows Users (Docker Requirement)

Docker Desktop uses Linux containers, which require Windows Subsystem for Linux (WSL2).

If prompted, install WSL by running:


wsl --install


Then restart your computer and reopen Docker.

This is required because Docker uses a lightweight Linux environment to run containers on Windows systems.

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

### 2. Start the FTP Server (Required for Option 4)

In a terminal:

python ftp_server.py


Expected output:

FTP server running on 127.0.0.1:2121


Keep this terminal open.

---

### 3. Open a New Terminal (if using VSCode)

Shortcut:

Ctrl + Shift + `

or  

Ctrl + Shift + 5


---

### 4. Run the Application

python -m src.main


---

## Application Menu (How to Use)

When the program starts, you will see:


=== CU Data Processing System ===

Generate test data
Process a file
Process all local files
Download and process FTP files
View logs
Exit

---

## Option 1: Generate Test Data

Select:

1


What it does:
- Generates valid and invalid CSV files
- Saves them into:


ftp_root/


These files can then be processed using other menu options.

---

## Option 2: Process a File (Manual Input)

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

## Option 3: Process All Local Files

Select:

3


What it does:
- Processes all `.csv` files in:

data/source/


Example files:

data/source/MED_DATA_20230603140104.csv
data/source/sample.csv


---

## Option 4: Download and Process FTP Files

Make sure FTP server is running first.

Select:

4


What happens:
- Files are downloaded from:

ftp_root/


- Saved to:

data/source/


- Automatically validated and sorted

---

## Option 5: View Logs

Select:

5


Displays:

logs/app.log


Includes:
- Errors
- Warnings
- Info messages
- GUID for each log entry

---

## Option 6: Exit

Select:

6


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
- FTP server and application run automatically inside the container

---

## Example Full Workflow

1. Generate test data:

1


2. Process FTP files:

4


Files will be downloaded, validated, and sorted automatically.

---

## Author

Aldrin Dumas