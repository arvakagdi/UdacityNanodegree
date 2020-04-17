def nth_row_pascal(n):
    """
    :param: - n - index (0 based)
    return - list() representing nth row of Pascal's triangle
    """
    MyList = [1]

    for i in range (1,n+1):
        if i == 1:
            return MyList
        if i == 2:
           MyList.append(1)
           return MyList
        if i > 2:
            for j in range(1,i+1):
                MyList.append(1)










def test_function(test_case):
    n = test_case[0]
    solution = test_case[1]
    output = nth_row_pascal(n)
    if solution == output:
        print("Pass")
    else:
        print("Fail")


n = 0
solution = [1]

test_case = [n, solution]
test_function(test_case)

n = 1
solution = [1, 1]

test_case = [n, solution]
test_function(test_case)

n = 2
solution = [1, 2, 1]

test_case = [n, solution]
test_function(test_case)

n = 3
solution = [1, 3, 3, 1]

test_case = [n, solution]
test_function(test_case)

n = 4
solution = [1, 4, 6, 4, 1]

test_case = [n, solution]
test_function(test_case)