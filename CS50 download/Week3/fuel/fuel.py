def main():
    fuel_level = get_level()
    print(fuel_level)

def get_level():
    while True:
        try:
            reading = (input("Fraction: "))
            reading = reading.strip()
            numerator, slash, denominator = reading.partition("/")
            numerator = int(numerator)
            denominator = int(denominator)
            level = round((numerator / denominator) * 100)
            if 0<= level <= 1:
                return "E"
            elif 100 >= level >= 99:
                return "F"
            elif 1 < level < 99:
                return str(level) + "%"
            else:
                pass
        except (ValueError, ZeroDivisionError):
            pass


main()
