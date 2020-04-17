'''Get the numebr of days between given dates'''

def Leapyear (year):
    if year % 400 == 0:
        return 29

    if year % 100 == 0:
        return 28
    if year % 4 == 0:
        return 29

    else:
        return 28

def DaysInMonth (month,year):
    list31 = [1, 3, 5, 7, 8, 10, 12]
    list30 = [4, 6, 9, 11]

    if month in list31:
        return 31
    elif month in list30:
        return 30
    else:
        return Leapyear(year)

def nextDay(year, month, day):
    if day != DaysInMonth(month,year):
        return (year, month, day + 1)
    else:
        if month != 12:
            return (year, month + 1, 1)
        else:
            return (year + 1, 1, 1)

def dateIsBefore(year1, month1, day1, year2, month2, day2):
    """Returns True if year1-month1-day1 is before
       year2-month2-day2. Otherwise, returns False."""
    if year1 < year2:
        return True
    if year1 == year2:
        if month1 < month2:
            return True
        if month1 == month2:
            return day1 < day2
    return False

def daysBetweenDates(year1, month1, day1, year2, month2, day2):

    assert not dateIsBefore(year2, month2, day2, year1, month1, day1)

    days = 0
    while dateIsBefore(year1, month1, day1, year2, month2, day2):
        year1, month1, day1 = nextDay(year1, month1, day1)
        days += 1
    return days


print (daysBetweenDates(1900, 1, 1, 1999, 12, 31))


'''Test Stubs'''
def test():
    test_cases = [((2012, 1, 1, 2012, 2, 28), 58),
                  ((2012, 1, 1, 2012, 3, 1), 60),
                  ((2011, 6, 30, 2012, 6, 30), 366),
                  ((2011, 1, 1, 2012, 8, 8), 585),
                  ((1900, 1, 1, 1999, 12, 31), 36523),
                  ((2012,2,28,2012,2,29),1),
                  ((2012, 1, 1, 2013, 1, 1), 366),
                  ((2013, 1, 24, 2013, 6, 29), 156)]

    # for (args, answer) in test_cases:
    #     result = daysBetweenDates(*args)
    #     if result != answer:
    #         print ("Test with data:", args, "failed")
    #     else:
    #         print("Test case passed!")

    for (args,ans) in test_cases:
        test = daysBetweenDates(*args)
        if test == ans:
            print("Test Passed")
        else:
            print ("Test case:", args, " failed with answer:", test, "expected answer:", ans)

    assert nextDay(2013,1,1) == (2013,1,2)
    assert nextDay(2013,2,28) == (2013,3,1)
    assert nextDay(2012,12,31) == (2013,1,1)

    print(Leapyear(1900))
    print(Leapyear(2012))
    print(Leapyear(2013))

    assert dateIsBefore(1900,1,1, 2019,2,4) == True
    assert dateIsBefore(1909,3,1,1909,3,31) == True
    assert dateIsBefore(1909,2,31, 1909,2,1) == False


test()