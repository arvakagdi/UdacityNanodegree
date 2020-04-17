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
CalledNumbers = []

for i in calls:
    if i[0].find('(080)') == 0:
        CalledNumbers.append(i[1])


CalledNumbers.sort()
NumberCodes = []

for i in CalledNumbers:
    if i.find('(') == 0:
        newnum = i.split(')')
        newnum[0] += ')'
        if newnum[0] not in NumberCodes:
            NumberCodes.append(newnum[0])

    elif i.find('7') == 0 or i.find('8') == 0 or i.find('9') == 0:
        newnum = i.split(' ')
        slicy = slice(4)
        mynum = newnum[0]
        x = mynum[slicy]
        if x not in NumberCodes:
            NumberCodes.append(x)

    else:
        if '140' not in NumberCodes:
            NumberCodes.append('140')


for i in NumberCodes:
    print(i)

Total = len(CalledNumbers)
bangcalls = 0

for i in CalledNumbers:
    if i.find('(080)') == 0:
        bangcalls += 1


percentage = (100.0*bangcalls)/Total
print('%.2f'%percentage,"percent of calls from fixed lines in Bangalore are calls to other fixed lines in Bangalore.")