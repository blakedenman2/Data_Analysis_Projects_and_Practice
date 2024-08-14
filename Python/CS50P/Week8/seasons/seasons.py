import sys
import inflect
from datetime import datetime, date


class Seconds:
    def __init__(self, birth_date_input):
        try:
            self.birth_date = datetime.strptime(birth_date_input, "%Y-%m-%d").date()
        except ValueError:
            sys.exit("Invalid Date")
        self.today = date.today()
        self.time_difference = abs((self.today - self.birth_date).days)
        self.total_minutes = self.time_difference*24*60

    def __str__(self):
        p = inflect.engine()
        sentence = p.number_to_words(self.total_minutes, andword="")
        return f"{sentence.capitalize()} minutes"


def main():
    birth_date_input = input("Date of birth: ")
    print(Seconds(birth_date_input))


if __name__ == "__main__":
    main()
