"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv, re

with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 3:
(080) is the area code for fixed line telephones in Bangalore.
Fixed line numbers include parentheses, so Bangalore numbers
have the form (080)xxxxxxx.)

Part A: Find all of the area codes and mobile prefixes called by people
in Bangalore.
 - Fixed lines start with an area code enclosed in brackets. The area
   codes vary in length but always begin with 0.
 - Mobile numbers have no parentheses, but have a space in the middle
   of the number to help readability. The prefix of a mobile number
   is its first four digits, and they always start with 7, 8 or 9.
 - Telemarketers' numbers have no parentheses or space, but they start
   with the area code 140.

Print the answer as part of a message:
"The numbers called by people in Bangalore have codes:"
 <list of codes>
The list of codes should be print out one per line in lexicographic order with no duplicates.

Part B: What percentage of calls from fixed lines in Bangalore are made
to fixed lines also in Bangalore? In other words, of all the calls made
from a number starting with "(080)", what percentage of these calls
were made to a number also starting with "(080)"?

Print the answer as a part of a message::
"<percentage> percent of calls from fixed lines in Bangalore are calls
to other fixed lines in Bangalore."
The percentage should have 2 decimal digits
"""

fixedline = []
mobile = []
telemarketer = []   # there are no calls TO a telemarketer

from_080_to_080 = caller_080 = 0

calls_to_080 = set()
mobile_prefix = set()

for i in range(len(calls)):
    if (calls[i][0]).find('(080)') == 0:
        # print (calls[i][0] + " called " + calls[i][1])
        caller_080 += 1
        match = re.search('\(0\d+\)', calls[i][1])
        if match:
            print ("   area code found!", match.group())
            print ("   from ", calls[i][1])
            calls_to_080.add(match.group())
            if re.search('^\(080\)', calls[i][1]):
                from_080_to_080 += 1

            fixedline.append(calls[i][1])
        else:
            match2 = re.search('([789]\d\d\d)\d*\s\d+', calls[i][1])
            if match2:
                print("   mobile number found: ", calls[i][1])
                mobile.append(calls[i][1])
                print("     and prefix was ", match2.group(1))
                mobile_prefix.add(match2.group(1))

print("set collected num area codes ", len(calls_to_080))
print("set collected mobile prefixes ", len(mobile_prefix))

print("The numbers called by people in Bangalore have codes:")

fixedline_sorted = sorted(set(fixedline))
for j in fixedline_sorted:
    print (j)

mobile_sorted = sorted(set(mobile))
for j in mobile_sorted:
    print(j)


percent = (from_080_to_080 / caller_080) * 100
print(round(percent, 2), "percent of calls from fixed lines in Bangalore are calls to other fixed lines in Bangalore.")

