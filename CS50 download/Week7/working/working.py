import re
import sys


def main():
    print(convert(input("Hours: ")))


def convert(s):
    if matches := re.search(r"^(1[0-2]|[1-9])(:[0-5][0-9])? ([AP]M) to (1[0-2]|[1-9])(:[0-5][0-9])? ([AP]M)$", s):
        hour1, minutes1, ampm1, hour2, minutes2, ampm2 = matches.groups()
        hour1 = hour11(hour1, ampm1)
        hour2 = hour22(hour2, ampm2)
        if minutes1 is None:
            minutes1 = ":00"
        if minutes2 is None:
            minutes2 = ":00"
        return f"{hour1:02}{minutes1} to {hour2:02}{minutes2}"

    else:
        raise ValueError

def hour11(hour1, ampm1):
    hour1 = int(hour1)
    if ampm1 == "PM" and hour1 == 12:
        hour1 = 12
        return hour1
    elif ampm1 == "PM":
        hour1 += 12
        return hour1
    elif ampm1 == "AM" and hour1 == 12:
        hour1 = 0
        return hour1
    else:
        return hour1

def hour22(hour2, ampm2):
    hour2 = int(hour2)
    if ampm2 == "PM" and hour2 == 12:
        hour2 = 12
        return hour2
    elif ampm2 == "PM":
        hour2 += 12
        return hour2
    elif ampm2 == "AM" and hour2 == 12:
        hour2 = 0
        return hour2
    else:
        return hour2

if __name__ == "__main__":
    main()
