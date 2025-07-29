2017 is not a leap year
1900 is a not leap year
2012 is a leap year
2000 is a leap year


year = 2000

if (year % 400 == 0) and (year % 100 == 0):
    print("{0} is a leap year".format(year))

elif (year % 4 ==0) and (year % 100 != 0):
    print("{0} is a leap year".format(year))

else:
    print("{0} is not a leap year".format(year))