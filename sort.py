import os
print("Hello SortPy (on line 2)")
print("Second 'Hello Sortpy' (on line 3)")
print("Importing datetime from datetime (line 4)")
from datetime import datetime
print("Imported datetime(line 6)")
day = int(datetime.today().strftime('%d'))
print("Getting today's date (line 8)")
print("Finding out which week of the month it is (line 9)")
if day > 7:
    if day > 14:
        if day > 21:
            week = "4"
        else:
            week = "3"
    else:
        week = "2"
else:
    week = "1"
print("Found out which week of the month it is (line 20)")
print("Creating a new string that holds information of today's year and month (line 21)")
string = str(datetime.today().strftime('%Y-%m'))
print("Created a new string that holds information about today's year and month (line 23)")
F = string + '-' + week
try:
    os.makedirs(F)
except IOError:
    L = open("SortPy-log.txt", 'a')
    L.write("\nfile already exists '" + F + "' DATE: " + str(datetime.today()))
    L.close()
exit()
