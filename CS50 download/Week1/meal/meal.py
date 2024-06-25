def main():
    yumyum = input("What time is it? ")
    if 7.0 <= convert(yumyum) <= 8.0 :
        print("breakfast time")
    elif 12.0 <= convert(yumyum) <= 13.0 :
        print("lunch time")
    elif 18.0 <= convert(yumyum) <= 19.0 :
        print("dinner time")


def convert(time):
    time = time.lower().strip()
    if time.endswith("a.m.") == True :
        time = time[:-4]
        hours, minutes = (time.split(":"))
        hours = int(hours)
        minutes = float(minutes) / 60
        total = hours + minutes
        return total
    elif time.endswith("p.m.") == True :
        time = time[:-4]
        if time.startswith("12") == True :
            hours, minutes = (time.split(":"))
            hours = int(hours)
            minutes = float(minutes) / 60
            total = hours + minutes
            return total
        else :
            hours, minutes = (time.split(":"))
            hours = int(hours) + 12
            minutes = float(minutes) / 60
            total = hours + minutes
            return total
    else :
        hours, minutes = (time.split(":"))
        hours = int(hours)
        minutes = float(minutes) / 60
        total = hours + minutes
        return total


if __name__ == "__main__":
    main()
