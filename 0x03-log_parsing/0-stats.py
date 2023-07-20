#!/usr/bin/python3

import sys

# Initialize variables to store metrics
total_file_size = 0
status_code_counts = {}

try:
    # Define a function to print metrics
    def print_metrics():
        print("Total file size: File size:", total_file_size)
        for status_code in sorted(status_code_counts.keys()):
            print(f"{status_code}: {status_code_counts[status_code]}")

    # Read stdin line by line and compute metrics
    for line_number, line in enumerate(sys.stdin, start=1):
        # Remove leading/trailing whitespaces and split the line into parts
        parts = line.strip().split()

        # Check if the line format is valid
        if len(parts) != 7 or parts[2] != 'GET' or parts[4] not in status_code_counts:
            continue

        # Extract file size and status code from the line
        file_size = int(parts[5])
        status_code = int(parts[4])

        # Update total file size and status code counts
        total_file_size += file_size
        status_code_counts[status_code] = status_code_counts.get(status_code, 0) + 1

        # Print metrics every 10 lines
        if line_number % 10 == 0:
            print_metrics()

except KeyboardInterrupt:
    # Print metrics on keyboard interruption (CTRL + C)
    print_metrics()

