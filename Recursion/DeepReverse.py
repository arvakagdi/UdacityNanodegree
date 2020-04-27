def deep_reverse(arr):
    if len(arr) == 0:
        return []
    else:
        lastnum = arr[0]
        substr = deep_reverse(arr[1:])

        if type(lastnum) != list:
            substr.append(lastnum)
        else:
            substr.append(deep_reverse(lastnum))
        return substr

def deep_reverse2(arr):
    return reverse(arr,0)

def reverse(arr,index):
    if index == len(arr):
        return []
    else:
        firstnum = arr[index]
        substr = reverse(arr,index+1)

        if type(firstnum) != list:
            substr.append(firstnum)
        else:
            substr.append(reverse(firstnum,0))
        return substr

def test_function(test_case):
    arr = test_case[0]
    solution = test_case[1]

    output = deep_reverse2(arr)
    if output == solution:
        print("Pass")
    else:
        print("False")


arr = [1, 2, 3, 4, 5]
solution = [5, 4, 3, 2, 1]
test_case = [arr, solution]
test_function(test_case)


arr = [1, 2, [3, 4, 5], 4, 5]
solution = [5, 4, [5, 4, 3], 2, 1]
test_case = [arr, solution]
test_function(test_case)


arr = [1, [2, 3, [4, [5, 6]]]]
solution = [[[[6, 5], 4], 3, 2], 1]
test_case = [arr, solution]
test_function(test_case)

arr =  [1, [2,3], 4, [5,6]]
solution = [ [6,5], 4, [3, 2], 1]
test_case = [arr, solution]
test_function(test_case)