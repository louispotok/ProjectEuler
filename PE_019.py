'''
No great poem deserves nineteen,
Try it, and you'll know what I mean.

After reading the forum, another approach
is to use datetime module, but such tricks I loathe.
'''

def main():
    #initial date info
    dates = {'year': 1901,
             'day_of_month': 1,
             'month':1, # 0 is December.
             'day_of_week': 1 + (365 % 7) # 1900 had 365 days and Jan 1 1900 was Monday
    }


    number_outcomes = 0
    while dates['year'] < 2001:
        if dates['day_of_week'] == 0 and dates['day_of_month'] == 1:
            number_outcomes += 1
        dates = increment_dates(dates)
    return number_outcomes

def increment_dates(dates):
    new_dates = {}
    new_dates['day_of_week'] = (dates['day_of_week'] + 1) % 7

    if is_last_day_of_month(dates):
        new_dates['day_of_month'] = 1
        new_dates['month'] = (dates['month'] + 1) % 12
    else:
        new_dates['day_of_month'] = dates['day_of_month'] + 1
        new_dates['month'] = dates['month']

    if new_dates['day_of_month'] == 1 and new_dates['month'] == 1:
        new_dates['year'] = dates['year'] + 1
        print new_dates['year']
    else:
        new_dates['year'] = dates['year']

    print new_dates['year'],new_dates['month'],new_dates['day_of_month']
    return new_dates

def is_last_day_of_month(dates):
    if dates['month'] in [4,6,9,11] and dates['day_of_month'] == 30:
        return True
    if dates['month'] in [0,1,3,5,7,8,10] and dates['day_of_month'] == 31:
        return True
    if dates['month'] == 2 and dates['day_of_month'] == 29:
        return True
    if dates['month'] == 2 and dates['day_of_month'] == 28 and dates['year']%4 != 0:
        return True
    else:
        return False

if __name__ == '__main__':
    print main()