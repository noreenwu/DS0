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

# create a set of unique numbers making phone calls
uniq_callers = set()
disqualified_nums = {}

for ph in calls:
    uniq_callers.add(ph[0])
    disqualified_nums[ph[1]] = 1   # any number receiving a call is disqualified


# add to dict of disqualified any numbers sending texts or receiving texts, from texts.csv
for txt in texts:
    disqualified_nums[txt[0]] = 1
    disqualified_nums[txt[1]] = 1


# iterate through the set of unique numbers and do not include anything found in the disqualifying dict
possible_telemarketer = []
for u in uniq_callers:
    if u not in disqualified_nums:
        possible_telemarketer.append(u)


possible_telemarketer_sorted = sorted(possible_telemarketer)

print ("These numbers could be telemarketers:")
for t in possible_telemarketer_sorted:
    print(t)


