from datetime import date
import re
import inflect
import sys

def main():
        birthday = input("")
        if match := re.search("(\d{4})-(\d{2})-(\d{2})", birthday):
            year = int(match.group(1))
            month = int(match.group(2))
            day = int(match.group(3))
            print(minutes(year, month, day))

        else:
            sys.exit("Invalid date")


def minutes(year, month, day):
    birth = date(year, month, day)
    p = inflect.engine()
    now = date.today()
    days = (now - birth).days
    minutes = days * 24 * 60
    string = string = p.number_to_words(minutes, andword="") + " minutes"
    return string.capitalize()

if __name__ == "__main__":
    main()
