months_list =[
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December",
    "01", "02", "03", "04", "05", "06", "07", "08", "09", "1", "2", "3", "4", "5",
    "6", "7", "8", "9", "10", "11", "12"
]

months_dict = {"January":"01",
    "February":"02",
    "March":"03",
    "April":"04",
    "May":"05",
    "June":"06",
    "July":"07",
    "August":"08",
    "September":"09",
    "October":"10",
    "November":"11",
    "December":"12"}

days = ["01", "02", "03", "04", "05", "06", "07", "08", "09", "1", "2", "3", "4", "5",
    "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19",
    "20", "21", "22", "23", "24", "25", "26", "27", "28", "29", "30", "31"]

def main():
    while True:
        try:
            date = input("Date: ").strip()
            if check_and_split(date) == False:
                continue
            else:
                values = check_and_split(date)
            if check_list(values) == False:
                continue
            else:
                print(reorg(values))
                break
        except (KeyError, ValueError):
            pass

def check_and_split(date):
    if "/" in date:
        if any(character.isalpha() for character in date):
            return False
        else:
            values = list(date.split("/"))
    elif "," in date:
        date = date.replace(",","")
        values = list(date.split(" "))
    else:
        return False
    mnth = str(values[0])
    if mnth.isalpha():
        mnth = months_dict[values[0]]
    values[0] = f"{int(mnth):02}"
    values[1] = f"{int(values[1]):02}"
    return values

def check_list(values):
    if values[0] in months_list and values[1] in days:
        return True
    else:
        return False

def reorg(values):
    year, month, day = values[2], values[0], values[1]
    new_date = "-".join([year, month, day])
    return new_date

main()
