# What does this do?

This code converts iCloud notes into a .csv that can be imported into DayOne via iOS.

This is accomplished by iterating through a folder of .txt files, searching for duplicates,
keeping the duplicate with the oldest timestamp, placing the duplicates into a 'Duplicates.csv' file for user review, and outputting the final .csv to be imported into DayOne.

# How to use this:

First request your notes data from [iCloud.](https://privacy.apple.com/account/archive)

For me it took 3 days for that to get delivered.

You will receive each note as a separate .txt file.

I am on windows and just searched (\*) in file explorer and then pressed Ctrl + X to paste all of them in a single folder.

Then I used ChatGPT to write some code to pull the data created from each of the files and store that in a .csv making sure to follow the [DayOne importing guidelines.](https://dayoneapp.com/guides/settings/importing-data-to-day-one/)

That code is what is in this repo.

To use it all you need to do is change the input folder location, output .csv location, and duplicates .csv location. 

If you get any errors, just feed them back into ChatGPT.

&#x200B;
