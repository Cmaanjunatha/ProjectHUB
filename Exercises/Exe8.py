year = int(input("Enter year : "))
if year % 2 == 0:
    if year %4 == 0:
        if year % 400 == 0:
            print("{0} is leap year")
        else:
            print("{0} is not a leap year")
    else:
        print("{0} is not a leap year")
else:
    print("{0} is not a leap year")


