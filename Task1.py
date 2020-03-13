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
ph_numbers = {}
ph_ary = []
# print(ph_numbers.get(texts[0][0]))

def register_num(ph_num):
    if ph_numbers.get(ph_num) is None:
        ph_numbers[ph_num] = 1
    else:
        ph_numbers[ph_num] += 1


for i in range(len(texts)):
    print (texts[i][0])
    print (texts[i][1])
    ph_ary.append(texts[i][0])
    ph_ary.append(texts[i][1])
    register_num(texts[i][0])
    register_num(texts[i][1])

ph_set = set(ph_ary)


print("length of set", len(ph_set))

for k in ph_numbers.keys():
    print (k)

print ("length of dict ", len(ph_numbers))



# print ("ary length", len(ph_ary)
    # register_num(texts[i][1])

# counter = 0
# for k in ph_numbers.keys():
#     counter += 1

# print (counter)
# repeat for calls

# for j in range(len(calls)):
#     print (calls[j])