#!usr/bin/python
# -*- coding: iso-8859-15 -*-
import datetime
import re

# program parameters
threshold_days_before_birthday = 15
birthday_file = 'birthday.ini'

# initialisations
year_of_birth = re.compile('\d{4}') #regular expression: 4 digits for year-of-birth

def read_input(fname):
    """
    reads birthdays from file
    """

    #open file, read lines and close it
    try:
        input = open(fname, 'r')
        lines = input.readlines()
        input.close()
    except:
        print "'" + birthday_file + "'", "kann nicht geoeffnet werden."
        lines = []

    return lines

def get_day_difference(d, m, today):
    """
    calculates the date of the upcoming birthday and the amount of days
    to the next birthday

    returns year of upcoming birthday as integer and day difference as integer
    """

    date_of_upcoming_bday = datetime.date(today.year, m, d)
    diff = date_of_upcoming_bday - today

    if diff.days < 0: #person already had birthday this year -> increase year
        date_of_upcoming_bday = datetime.date(today.year + 1, m, d)
        diff = date_of_upcoming_bday - today

    return int(date_of_upcoming_bday.strftime("%Y")), diff.days

def get_age_string(persons_name, d, m, year_of_upcoming_bday):
    """
    forms a string with the age of the birthday child
    """

    if len(year_of_birth.findall(persons_name)) > 0: # get year from string using regular expression
        byear = int(year_of_birth.findall(persons_name)[0])
        return ' wird ' + str(year_of_upcoming_bday - byear) + ' am ' + d + '.' + m + '.' + str(year_of_upcoming_bday)
    else:
        return ''

def get_friendly_time(day_diff):
    """
    converts small day-differences in friendly names for today and tomorrow
    """

    if day_diff == 0:
        return 'H E U T E'
    elif day_diff == 1:
        return 'M O R G E N'
    else:
        return 'in ' + str(day_diff) + ' Tagen'

def main():
    """
    the program entry point
    """

    today = datetime.date.today()
    birthday_list = read_input(birthday_file)

    for element in birthday_list:
        line = element.partition(' ')
        d, m, trash = line[0].split('.')
        year_of_upcoming_bday, day_diff = get_day_difference(int(d), int(m), today)

        if day_diff < threshold_days_before_birthday:
            # display of birthday triggered - do formatting for output
            bday_childs_name = line[2].replace('\n', '')
            age_string = get_age_string(bday_childs_name, d, m, year_of_upcoming_bday)
            friendly_time = get_friendly_time(day_diff)
            print bday_childs_name.split('(')[0].strip() + age_string, '-', friendly_time

if __name__ == "__main__":
    main()
