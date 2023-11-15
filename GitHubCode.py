'''
This code converts iCloud notes into a .csv that can be imported into DayOne via iOS.

This is accomplished by iterating through a folder of .txt files, searching for duplicates,
keeping the duplicate with the oldest timestamp, placing the duplicates into a 'Duplicates.csv' file for user review, and outputting the final .csv to be imported into DayOne.

'''

# Import necessary libraries
import os
import csv
from datetime import datetime, timezone, timedelta
from fuzzywuzzy import fuzz

# Specify the folder containing the .txt files
folder_path = r'C:\Users\DayOne\iCloudNotes'  # Update with your folder path

# Specify the output .csv file
csv_file_path = r'C:\Users\DayOne\FinalOutput.csv'  # Update with your desired output path

# Specify the output .csv file for duplicates
duplicate_file_path = r'C:\Users\DayOne\Duplicates.csv'  # Update with your desired output path for duplicates

# Define the time zone offset for Eastern Standard Time (EST)
est_offset = timedelta(hours=-5)

# Specify the threshold for text similarity
similarity_threshold = 90  # You can adjust this threshold as needed

# Dictionary to keep track of processed entries and their creation dates
processed_entries = {}

# List to store duplicate entries
duplicate_entries = []

# Function to check if text data is a duplicate or near-duplicate
def is_duplicate(text_data):
    return text_data in processed_entries

# Function to compare two ISO formatted date strings
def compare_dates(date1, date2):
    dt1 = datetime.strptime(date1, '%Y-%m-%dT%H:%M:%S.000Z')
    dt2 = datetime.strptime(date2, '%Y-%m-%dT%H:%M:%S.000Z')
    return dt1 < dt2

# Open the .csv file in append mode with explicit newline parameter
with open(csv_file_path, 'a', newline='', encoding='utf-8') as csv_file, \
     open(duplicate_file_path, 'a', newline='', encoding='utf-8') as duplicate_file:
    # Create CSV writer objects for both files
    csv_writer = csv.writer(csv_file)
    duplicate_writer = csv.writer(duplicate_file)

    # Check if the CSV file is empty (no header), and write header if needed
    if csv_file.tell() == 0:
        csv_writer.writerow(['date', 'text'])

    # Check if the duplicate CSV file is empty (no header), and write header if needed
    if duplicate_file.tell() == 0:
        duplicate_writer.writerow(['date', 'text'])

    # Iterate through all .txt files in the folder
    for file_name in os.listdir(folder_path):
        if file_name.endswith('.txt'):
            file_path = os.path.join(folder_path, file_name)

            # Get the modification time of the file
            modification_time = os.path.getmtime(file_path)

            # Convert modification time to Eastern Time
            local_time = datetime.fromtimestamp(modification_time, tz=timezone(est_offset))
            iso_format_creation_time = local_time.strftime('%Y-%m-%dT%H:%M:%S.000Z')

            # Read the text data from the file
            with open(file_path, 'r', encoding='utf-8') as txt_file:
                text_data = txt_file.read()

            # Check for duplicate or near-duplicate entry
            if is_duplicate(text_data):
                # Compare creation dates and keep the older one
                existing_date = processed_entries[text_data]
                if compare_dates(existing_date, iso_format_creation_time):
                    # Add the current duplicate to the list
                    duplicate_entries.append([iso_format_creation_time, text_data.strip()])
                    # Update the processed entry with the older date
                    processed_entries[text_data] = iso_format_creation_time
            else:
                # Write the information to the CSV file
                csv_writer.writerow([iso_format_creation_time, text_data.strip()])
                # Update the processed entry with its creation date
                processed_entries[text_data] = iso_format_creation_time

    # Write the duplicate entries to the duplicate CSV file
    duplicate_writer.writerows(duplicate_entries)

# Print success messages
print(f"CSV file '{csv_file_path}' has been updated successfully.")
print(f"Duplicate entries saved to '{duplicate_file_path}'.")