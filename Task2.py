"""
Read file into texts and calls.
It's ok if you don't understand how to read files
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls-first-5.csv', 'r') as f:
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

def register_phone_call(ph, dur):
    if phone_time.get(ph) is None:
        phone_time[ph] = 0

    phone_time[ph] += dur


def print_longest_message(phone_str, dur):
    print (phone_str + " spent the longest time, ", dur, "seconds, on the phone during September 2016.")


for i in range(len(calls)):
    # print (calls[i][3])
    register_phone_call(calls[i][0], int(calls[i][3]))
    register_phone_call(calls[i][1], int(calls[i][3]))


print("max:")
max_key = max(phone_time, key=phone_time.get)
print (max_key)
max_val = phone_time[max_key]

print ("max value is ", max_val)
print(max(phone_time, key=phone_time.get))


maxes = []
for key, value in phone_time.items():
    if value == max_val:
        maxes.append(key)

print("the maxes were ", maxes)

if len(maxes) == 1:
    print_longest_message(str(maxes[0]), max_val)

elif len(maxes) > 1:
    tot = len(maxes)
    while tot > 2:
        print (maxes[tot-1], ", ")
        tot -= 1

    print_longest_message(str(maxes[1]) + " and " + str(maxes[0]), max_val)

