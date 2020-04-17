def daysBetweenDates(year1, month1, day1, year2, month2, day2):
    list31 = [1,3,5,7,8,10,12]
    list30 = [2,4,6,9,11]
    TotalDays = 0

    # while dateBefore (year1, month1, day1, year2, month2, day2):
    while (year1 != year2 or month1 != month2 or day1!= day2):
        if month1 in list31:
            if day1 != 31:
                TotalDays += 1
                day1 += 1

            else:
                if month1 != 12:
                    month1 += 1
                    day1 = 0
                else:
                    year1 += 1
                    month1 = 1
                    day1 = 0

        elif month1 in list30:
            if month1 == 2 and year1 % 4 == 0:
                if day1 != 29:
                    TotalDays += 1
                    day1 += 1

                else:
                    if month1 != 12:
                        month1 += 1
                        day1 = 0
                    else:
                        year1 += 1
                        month1 = 1
                        day1 = 0

            elif month1 == 2 and year1 % 4 != 0:
                if day1 != 28:
                    TotalDays += 1
                    day1 += 1
                else:
                    if month1 != 12:
                        month1 += 1
                        day1 = 0
                    else:
                        year1 += 1
                        month1 = 1
                        day1 = 0
            else:
                if day1 != 30:
                    TotalDays += 1
                    day1 += 1
                else:
                    if month1 != 12:
                        month1 += 1
                        day1 = 0
                    else:
                        year1 += 1
                        month1 = 1
                        day1 = 0

    return TotalDays

def testDaysBetweenDates():
    # test same day
    assert (daysBetweenDates(2017, 12, 30,
                             2017, 12, 30) == 0)
    # test adjacent days
    assert (daysBetweenDates(2017, 12, 30,
                             2017, 12, 31) == 1)
    # test new year
    assert (daysBetweenDates(2017, 12, 30,
                             2018, 1, 1) == 2)
    # test full year difference
    assert (daysBetweenDates(2012, 6, 29,
                             2013, 6, 29) == 365)

    # print (daysBetweenDates(2012, 6, 29,
    #                          2013, 6, 29))
    print(daysBetweenDates(1900, 1, 1, 1999, 12, 31))

    print("Congratulations! Your daysBetweenDates")
    print("function is working correctly!")

testDaysBetweenDates()