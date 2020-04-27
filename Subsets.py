'''
Problem Statement
Given an integer array, find and return all the subsets of the array.
The order of subsets in the output array is not important.
However the order of elements in a particular subset should remain the same as in the input array.
Note: An empty set will be represented by an empty list

Example 1
arr = [9]
output = [[] , [9]]

Example 2
arr = [9, 12, 15]
output =  [[],[15],[12],[12, 15],[9],[9, 15],[9, 12],[9, 12, 15]]
'''

import copy

def subsets(arr):
    """
    :param: arr - input integer array
    Return - list of lists (two dimensional array) where each list represents a subset
    TODO: complete this method to return subsets of an array
    """
    Subset = []
    if len(arr) == 0:
        Subset.append([])

    else:
        curr_elem = arr[-1]
        substr = subsets(arr[:-1])

        for elem in substr:
            Subset.append(elem)

        for element in substr:
            r = copy.deepcopy(element)
            r.append(curr_elem)
            Subset.append(r)

    return Subset


def test_function(test_case):
    arr = test_case[0]
    solution = test_case[1]

    output = subsets(arr)

    output.sort()
    solution.sort()

    if output == solution:
        print("Pass")
    else:
        print("Fail")

arr = [9]
solution = [[], [9]]
test_case = [arr, solution]
test_function(test_case)


arr = [5, 7]
solution = [[], [7], [5], [5, 7]]
test_case = [arr, solution]
test_function(test_case)

arr = [9, 12, 15]
solution = [[], [15], [12], [12, 15], [9], [9, 15], [9, 12], [9, 12, 15]]
test_case = [arr, solution]
test_function(test_case)

arr = [9, 8, 9, 8]
solution = [[],
[8],
[9],
[9, 8],
[8],
[8, 8],
[8, 9],
[8, 9, 8],
[9],
[9, 8],
[9, 9],
[9, 9, 8],
[9, 8],
[9, 8, 8],
[9, 8, 9],
[9, 8, 9, 8]]
test_case = [arr, solution]
test_function(test_case)

