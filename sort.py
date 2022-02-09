import os
from datetime import datetime
day = int(datetime.today().strftime('%d'))
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

string = str(datetime.today().strftime('%Y-%m'))
F = string + '-' + week
try:
    os.makedirs(F)
except IOError:
    L = open("SortPy-log.txt", 'a')
    L.write("\nfile already exists '" + F + "' DATE: " + str(datetime.today()))
    L.close()
exit()
