import argparse
import csv
import datetime
import re

# program parameters
threshold_days_before_birthday = 15

def file_read_csv(file_name):
    input = []

    with open(file_name, 'r', encoding='cp852', newline='') as csv_file:
        reader = csv.DictReader(csv_file, delimiter=';')
        for row in reader:
            # print(row['Name'], row['dd'], row['mm'], row['yyyy'])
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

def get_age_string(persons_name, d, m, year_of_birth, year_of_upcoming_bday):
    """
    forms a string with the age of the birthday child
    """

    if year_of_birth > 0: # year found in birthday list
        return ' wird %s am %s.%s.%s' % (str(year_of_upcoming_bday - year_of_birth), d, m, str(year_of_upcoming_bday))
    else:
        return ' am %s.%s.%s' % (d, m, str(year_of_upcoming_bday))

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
            year_of_birth = 0
            if element['yyyy'] is not None:
                year_of_birth = int(element['yyyy'])
            age_string = get_age_string(bday_childs_name, int(element['dd']), int(element['mm']), year_of_birth, year_of_upcoming_bday)
            friendly_time = get_friendly_time(day_diff)
            print(bday_childs_name + age_string, '-', friendly_time)

if __name__ == "__main__":
    main()
