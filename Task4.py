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
TASK 4:
The telephone company want to identify numbers that might be doing
telephone marketing. Create a set of possible telemarketers:
these are numbers that make outgoing calls but never send texts,
receive texts or receive incoming calls.

Print a message:
"These numbers could be telemarketers: "
<list of numbers>
The list of numbers should be print out one per line in lexicographic order with no duplicates.
"""

# create a dict of unique numbers making phone calls

possible_telemarketer = {}

def check_number(num):
    if possible_telemarketer.get(num) is not None:
        del possible_telemarketer[num]


for c in calls:
    possible_telemarketer[c[0]] = True


# loop through and eliminate numbers that received calls
for c in calls:
    check_number(c[1])


# loop through and eliminate numbers that sent or received texts
for t in texts:
    check_number(t[0])
    check_number(t[1])


# print result
sorted_telemarketers = sorted(possible_telemarketer.keys())

print ("These numbers could be telemarketers:")
print("\n".join(sorted_telemarketers))




