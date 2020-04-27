def power_of_two(number):
    if number == 0:
        return 1
    else:
        return 2* power_of_two(number-1)

print(power_of_two(4))


def sum_of_int(integer):
    if integer == 0:
        return 0
    else:
        return integer + sum_of_int(integer-1)

def sum_of_array(arr):
    if len(arr) == 1:
        return arr[0]
    else:
        return arr[0] + sum_of_array(arr[1:])

print("sum of 8 integers is: ",sum_of_array([1,2,3,4,5,6,7,8]))
print(power_of_two(100))


def sum_of_array(arr):
    # with complexity n*n as we are using slicing
    if len(arr) == 1:
        return arr[0]
    else:
        return arr[0] + sum_of_array(arr[1:])


#O(n) complexity by using index
def sum_array_index(arr,index):
    if len(arr) - index == 1:
        return arr[index]
    else:
        return (arr[index] + sum_array_index(arr,index + 1))

print("sum of 8 integers is: ",sum_array_index([1,2,3,4,5,6,7,8],0))


def sum(n):
    sum = 0
    while n != 0:
        sum  += n
        n -= 1
    return sum

print(sum(5))