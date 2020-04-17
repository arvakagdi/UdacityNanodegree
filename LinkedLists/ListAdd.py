def add_one(arr):
    """
    :param: arr - list of digits representing some number x
    return a list with digits represengint (x + 1)
    """
    i = len(arr)-1

    if arr[i] < 9:
        arr[i] += 1
        return arr
    else:
        arr[i] = 0
        while i > 0:
            i -= 1
            if arr[i] < 9:
                arr[i] += 1
                return arr
            else:
                arr[i] = 0
        if arr[0] < 9:
            arr[i] += 1
            return arr
        else:
            newlist = [1]
            newlist.append(arr)
            return arr

    pass


def test_function(test_case):
    arr = test_case[0]
    solution = test_case[1]

    output = add_one(arr)
    for index, element in enumerate(output):
        if element != solution[index]:
            print("Fail")
            return
    print("Pass")

arr = [0]
solution = [1]
test_case = [arr, solution]
test_function(test_case)

arr = [1, 2, 3]
solution = [1, 2, 4]
test_case = [arr, solution]
test_function(test_case)

arr = [9, 9, 9]
solution = [1, 0, 0, 0]
test_case = [arr, solution]
test_function(test_case)