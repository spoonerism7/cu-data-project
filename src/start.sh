#!/bin/bash

echo "Starting FTP server..."
python ftp_server.py &

sleep 2

echo "Starting application..."
python -m src.main