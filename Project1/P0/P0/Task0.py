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
TASK 0:
What is the first record of texts and what is the last record of calls?
Print messages:
"First record of texts, <incoming number> texts <answering number> at time <time>"
"Last record of calls, <incoming number> calls <answering number> at time <time>, lasting <during> seconds"
"""

text = texts[0]
call = calls[-1]

print("First record of texts, "+ str(text[0]) + " texts " + str(text[1]) + " at time " + text[2])
print("Last record of calls, " + str(call[0]) + " calls " + str(call[1]) + " at time " + str(call[2]) + ", lasting " + str(call[3]) + " seconds")