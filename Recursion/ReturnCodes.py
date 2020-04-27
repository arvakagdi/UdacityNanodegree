'''
In an encryption system where ASCII lower case letters represent numbers in the pattern a=1, b=2, c=3... and so on,
find out all the codes that are possible for a given input number.

Example 1

number = 123
codes_possible = ["aw", "abc", "lc"]
Explanation: The codes are for the following number:

1 . 23 = "aw"
1 . 2 . 3 = "abc"
12 . 3 = "lc"
Example 2

number = 145
codes_possible = ["ade", "ne"]
Return the codes in a list. The order of codes in the list is not important.
'''


def all_codes(number):
    """
    :param: number - input integer
    Return - list() of all codes possible for this number
    TODO: complete this method and return a list with all possible codes for the input number
    """
    Codes = []
    if number == 0:
        Codes.append('')
    else:
        firstnum = number%10
        substr = all_codes(number//10)

        for character in substr:
            if character != '':
                last = str(ord(character[-1]) - 96)
                join = int(last + str(firstnum))
                if join+96 <= 122:
                    newchar = chr(join + 96)
                    Codes.append(character[:-1] + newchar)
            newnum = character + chr(firstnum + 96)
            Codes.append(newnum)

    return Codes


def test_function(test_case):
    number = test_case[0]
    solution = test_case[1]

    output = all_codes(number)

    output.sort()
    solution.sort()

    if output == solution:
        print("Pass")
    else:
        print("Fail")

number = 123
solution = ['abc', 'aw', 'lc']
test_case = [number, solution]
test_function(test_case)

number = 145
solution =  ['ade', 'ne']
test_case = [number, solution]
test_function(test_case)

number = 1145
solution =  ['aade', 'ane', 'kde']
test_case = [number, solution]
test_function(test_case)

number = 4545
solution = ['dede']
test_case = [number, solution]
test_function(test_case)

print(all_codes(112222))