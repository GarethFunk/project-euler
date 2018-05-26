# approx 36,500 days in 20th century so let's just run through them all!

def daysinmonth(year, month):
    if month == 4 or month == 6 or month == 9 or month == 11:
        return 30
    elif month == 2:
        if leapyear(year):
            return 29
        else:
            return 28
    else:
        return 31

def leapyear(year):
    if year%100 == 0:
        # is a centruty
        if year%400 == 0:
            return True
        else:
            return False
    elif year%4 == 0:
        return True
    else:
        return False

def tomorrow(day, date, month, year):
    if day < 7:
        day += 1
    else:
        day = 1
    if date < daysinmonth(year, month):
        date += 1
    else:
        # New month
        date = 1
        if month < 12:
            month += 1
        else:
            # New Year
            month = 1
            year += 1
            if leapyear(year):
                print(str(year) + " was a leap year")
    return day, date, month, year
        

year = 1900
month = 1
date = 1
day = 1 # 1 = mon, 2 = tue etc.
num_sundays_on_first = 0

while year < 2001:
    day, date, month, year = tomorrow(day, date, month, year)
    # print(str(day) + ", " + str(date) + "/" + str(month) + "/" + str(year))
    if day == 7 and date == 1 and year > 1900:
        num_sundays_on_first += 1

print(num_sundays_on_first)
