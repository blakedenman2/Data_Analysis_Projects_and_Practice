from tabulate import tabulate
import sys


def main():
    if len(sys.argv) == 2:
        if sys.argv[1].endswith(".csv") == False:
            sys.exit("Not a Python file")
        else:
            table = read_table(sys.argv[1])
            print(tabulate(table, headers="firstrow", tablefmt="grid"))
    elif len(sys.argv) == 1:
        sys.exit("Too few command-line arguments")
    else:
        sys.exit("Too many command-line arguments")


def read_table(filename):
    try:
        with open(filename, "r") as file:
            lines = file.readlines()
            menu = [line.strip().split(",") for line in lines]
            return menu
    except FileNotFoundError:
        sys.exit("File does not exist")


if __name__ == "__main__":
    main()
