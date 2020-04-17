# def duplicate_number(arr):
#     """
#     :param - array containing numbers in the range [0, len(arr) - 2]
#     return - the number that is duplicate in the arr
#     """
#     count = {}
#     for num in arr:
#         if num not in count:
#             count[num] = 1
#         else:
#             return num
#     pass

def duplicate_number(arr):   # with time comp O(n) and space comp O(1)
    """
    :param - array containing numbers in the range [0, len(arr) - 2]
    return - the number that is duplicate in the arr
    """
    range = len(arr) - 2
    Total = 0

    while range != 0:
        Total += range
        range -= 1

    arrlen = sum(arr)

    return  arrlen - Total
    pass


def test_function(test_case):
    arr = test_case[0]
    solution = test_case[1]
    output = duplicate_number(arr)
    if output == solution:
        print("Pass")
    else:
        print("Fail")


arr = [0, 0]
solution = 0

test_case = [arr, solution]
test_function(test_case)

arr = [0, 2, 3, 1, 4, 5, 3]
solution = 3

test_case = [arr, solution]
test_function(test_case)


arr = [0, 1, 5, 4, 3, 2, 0]
solution = 0

test_case = [arr, solution]
test_function(test_case)


arr = [0, 1, 5, 5, 3, 2, 4]
solution = 5

test_case = [arr, solution]
test_function(test_case)