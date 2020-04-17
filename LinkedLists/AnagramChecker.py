def anagram_checker(str1, str2):
    """
    Check if the input strings are anagrams of each other

    Args:
       str1(string),str2(string): Strings to be checked
    Returns:
       bool: Indicates whether strings are anagrams
    """
    # seenwords1 = []
    # seenwords2 = []
    #
    #
    # for i in str1:
    #     seenwords1.append(i.lower())
    #
    # for i in str2:
    #     seenwords2.append(i.lower())
    #
    #
    # for i in str1:
    #     if i != " ":
    #         if i.lower() not in seenwords2:
    #             return False
    #         elif i in seenwords2:
    #             seenwords2.remove(i)
    #
    # for i in str2.lower():
    #     if i != " ":
    #         if i not in seenwords1:
    #             return False
    #         elif i in seenwords1:
    #             seenwords1.remove(i)
    # return True

    if len(str1) != len(str2):
        # Clean strings
        clean_str_1 = str1.replace(" ", "").lower()
        clean_str_2 = str2.replace(" ", "").lower()

        if sorted(clean_str_1) == sorted(clean_str_2):
            return True
    pass



print ("Pass" if not (anagram_checker('water','waiter')) else "Fail")
print ("Pass" if anagram_checker('Dormitory','Dirty room') else "Fail")
print ("Pass" if anagram_checker('Slot machines', 'Cash lost in me') else "Fail")
print ("Pass" if not (anagram_checker('A gentleman','Elegant men')) else "Fail")
print ("Pass" if anagram_checker('Time and tide wait for no man','Notified madman into water') else "Fail")