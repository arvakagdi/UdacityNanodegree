def reverse_string(input):
    if len(input) == 0:
        return ''
    return (input[-1] + reverse_string(input[0:-1]))

print(reverse_string('abcdefghijkl'))

# Test Cases

print("Pass" if ("" == reverse_string("")) else "Fail")
print("Pass" if ("cba" == reverse_string("abc")) else "Fail")


