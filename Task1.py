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

text_ary = []


for i in range(len(texts)):
    text_ary.append(texts[i][0])
    text_ary.append(texts[i][1])


text_set = set(text_ary)
text_set_num = len(text_set)
# print("length of set", text_set_num)


call_ary = []
for j in range(len(calls)):
    call_ary.append(calls[j][0])
    call_ary.append(calls[j][1])


call_set = set(call_ary)
call_set_num = len(call_set)
# print("length of second set", call_set_num)

total_num = text_set_num + call_set_num
print("There are " + str(total_num) + " different telephone numbers in the records")


