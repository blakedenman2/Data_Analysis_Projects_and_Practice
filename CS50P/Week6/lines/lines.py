# make sure there is one command line argument
# make sure it ends in .py or exists, otherwise exit
# spit out how many lines that file has that are not blank or starting with #

import sys


def main():
    if len(sys.argv) == 2:
        if sys.argv[1].endswith(".py") == False:
            sys.exit("Not a Python file")
        else:
            print(count_lines(sys.argv[1]))
    elif len(sys.argv) == 1:
        sys.exit("Too few command-line arguments")
    else:
        sys.exit("Too many command-line arguments")


def count_lines(filename):
    try:
        with open(filename) as file:
            lines = file.readlines()
            non_empty_lines = [line for line in lines if line.strip()]
            non_comment_lines = [line for line in non_empty_lines if not line.strip().startswith("#")]
            count = len(non_comment_lines)
            return count
    except FileNotFoundError:
        sys.exit("File does not exist")

if __name__ == "__main__":
    main()
