def is_palindrome(input):
    if len(input)/2 == 0:
        return True
    else:
        # if input[0] == input[-1]:
        #     return (is_palindrome(input[1:-1]))
        # else:
        #     return False
        return (input[0] == input[-1] and is_palindrome(input[1:-1]))     #see how code can be made efficient


# Test Cases
print ("Pass" if  (is_palindrome("")) else "Fail")
print ("Pass" if  (is_palindrome("a")) else "Fail")
print ("Pass" if  (is_palindrome("madam")) else "Fail")
print ("Pass" if  (is_palindrome("abba")) else "Fail")
print ("Pass" if not (is_palindrome("Udacity")) else "Fail")
