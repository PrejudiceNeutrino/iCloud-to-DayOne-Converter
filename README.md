This code converts iCloud notes into a .csv that can be imported into DayOne via iOS.

This is accomplished by iterating through a folder of .txt files, searching for duplicates,
keeping the duplicate with the oldest timestamp, placing the duplicates into a 'Duplicates.csv' file for user review, and outputting the final .csv to be imported into DayOne.
