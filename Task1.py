"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)


"""
TASK 1:
How many different telephone numbers are there in the records?
Print a message:
"There are <count> different telephone numbers in the records."
"""

phonenum_dict = {}
# create or reassign key in dict for each text
for t in texts:
    phonenum_dict[t[0]] = 1
    phonenum_dict[t[1]] = 1


# create or reassign key in dict for each call
for c in calls:
    phonenum_dict[c[0]] = 1
    phonenum_dict[c[1]] = 1


print("There are {} different telephone numbers in the records.".format(len(phonenum_dict)))


