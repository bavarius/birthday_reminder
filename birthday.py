#!usr/bin/python
# -*- coding: iso-8859-15 -*-
import argparse
import csv
import datetime
import re

# program parameters
threshold_days_before_birthday = 15

# initialisations
year_of_birth = re.compile('\\d{4}') #regular expression: 4 digits for year-of-birth

def file_read_csv(file_name):
    input = []

    with open(file_name, 'r', newline='') as csv_file:
        reader = csv.DictReader(csv_file, delimiter=';')
        for row in reader:
            print(row['Name'], row['dd'], row['mm'], row['yyyy'])
            input.append(row)

    return input

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
        return u' wird %s am %s.%s.%s' % (str(year_of_upcoming_bday - byear), d, m, str(year_of_upcoming_bday))
    else:
        return u' am %s.%s.%s' % (d, m, str(year_of_upcoming_bday))

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

    parser = argparse.ArgumentParser(description='Birthday Reminder')
    parser.add_argument('-c', '--csv', required=True, type=str, help="Geburtstagsdatei im csv-Format (Trennzeichen: ';' - Semikolon)")

    args = parser.parse_args()

    if args.csv is not None:
        birthday_list = file_read_csv(args.csv)

    for element in birthday_list:
        year_of_upcoming_bday, day_diff = get_day_difference(int(element['dd']), int(element['mm']), today)
        if day_diff < threshold_days_before_birthday:
            # display of birthday triggered - do formatting for output
            bday_childs_name = element['Name']
            age_string = get_age_string(bday_childs_name, int(element['dd']), int(element['mm']), year_of_upcoming_bday)
            friendly_time = get_friendly_time(day_diff)
            print(bday_childs_name.split('(')[0].strip() + age_string, '-', friendly_time)

if __name__ == "__main__":
    main()
