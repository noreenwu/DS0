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
print ("num calls ", len(calls))
for ph in calls:
    # print(ph[0])
    uniq_callers.add(ph[0])
    # print("adding receiver as disqualified num ", ph[1])
    disqualified_nums[ph[1]] = 1

print("num disqualified nums after looping thru calls ", len(disqualified_nums))

# create a list/dict of numbers sending texts or receiving texts, from texts.csv
for txt in texts:
    # print(txt[0])
    # print (txt[1])
    disqualified_nums[txt[0]] = 1
    disqualified_nums[txt[1]] = 1


# include in that list/dict numbers that have received calls (from 2nd col, calls.csv)
print("disqualifying nums: ", len(disqualified_nums))

print("uniq callers:", len(uniq_callers))

# iterate through the set of unique numbers and delete anything found in the disqualifying dict
possible_telemarketer = []
for u in uniq_callers:
    if u not in disqualified_nums:
        # print("disqualifying one")
        possible_telemarketer.append(u)


for t in possible_telemarketer:
    print(t)


