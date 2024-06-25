def main():
    while True:
        try:
            fraction = input("Fraction: ")
            percentage = convert(fraction)
            reading = gauge(percentage)
            print(reading)
            break
        except (ValueError, ZeroDivisionError):
            pass


def convert(fraction):
    try:
        reading = fraction.strip()
        numerator, slash, denominator = reading.partition("/")
        numerator = int(numerator)
        denominator = int(denominator)
        level = round((numerator / denominator) * 100)
        if level > 100:
            raise ValueError
        return level
    except ZeroDivisionError:
        raise ZeroDivisionError
    except ValueError:
        raise ValueError


def gauge(percentage):
    if 0 <= percentage <= 1:
        return "E"
    elif 100 >= percentage >= 99:
        return "F"
    elif 1 < percentage < 99:
        return str(percentage) + "%"


if __name__ == "__main__":
    main()
