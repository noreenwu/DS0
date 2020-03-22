"""
Read file into texts and calls.
It's ok if you don't understand how to read files
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 2: Which telephone number spent the longest time on the phone
during the period? Don't forget that time spent answering a call is
also time spent on the phone.
Print a message:
"<telephone number> spent the longest time, <total time> seconds, on the phone during
September 2016.".
"""

# calls only (not texts)
phone_time = {}

#------------------------------------------------------
# register_phone_call: add the provided duration to the
#   specified number's tally
#------------------------------------------------------
def register_phone_call(ph, dur):
    phone_time[ph] = phone_time.get(ph, 0) + dur


#------------------------------------------------------
# print_longest_message: given the phone number and
#   duration, output the informational message
#------------------------------------------------------
def print_longest_message(phone_str, dur):
    print ("{} spent the longest time, {} seconds, on the phone during September 2016.".format(phone_str, dur))


## loop through calls
for i in range(len(calls)):
    date_time = calls[i][2]
    date = date_time.split(" ")
    date_pieces = date[0].split("-")

    if date_pieces[1] == '09' and date_pieces[2] == '2016': # confirm Sept 2016
        register_phone_call(calls[i][0], int(calls[i][3]))
        register_phone_call(calls[i][1], int(calls[i][3]))



max_key = max(phone_time, key=phone_time.get)
max_val = phone_time[max_key]

maxes = []    # often the maxes occur in pairs, since both the caller and callee are counted
for key, value in phone_time.items():
    if value == max_val:
        maxes.append(key)

# print the message: which number(s) spent the longest time
if len(maxes) == 1:
    print_longest_message(str(maxes[0]), max_val)

elif len(maxes) > 1:
    tot = len(maxes)
    while tot > 2:
        print (maxes[tot-1], ", ")
        tot -= 1

    print_longest_message(str(maxes[1]) + " and " + str(maxes[0]), max_val)

