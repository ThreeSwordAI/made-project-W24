#!/bin/bash

echo "Installing required libraries."
pip install -r requirements.txt


if [ $? -ne 0 ]; then
    echo "Failed to install required libraries."
    exit 1
fi

echo "Running pipeline.py file. Datesets are reduced because of the time it takes to run the pipeline."
python3 pipeline.py

if [ $? -ne 0 ]; then
    echo "Failed to run pipeline.py file."
    exit 1
fi

echo "Running tests.py file"
python3 tests.py

if [ $? -eq 0 ]; then
    echo "All tests passed successfully."
    exit 0
else
    echo "All tests did not pass failed."
    exit 1
fi