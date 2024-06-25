import sys
import csv

info = []


def main():
    if len(sys.argv) == 3:
        try:
            with open(sys.argv[1]) as file:
                DictReader = csv.DictReader(file)
                for row in DictReader:
                    first, last = row["name"].strip('"').split(", ")
                    info.append({"first": first, "last": last, "house": row["house"]})
            with open(sys.argv[2], "w") as file:
                writer = csv.DictWriter(file, fieldnames=["first", "last", "house"])
                writer.writeheader()
                for new_row in info:
                    writer.writerow(new_row)
        except FileNotFoundError:
            sys.exit(f"Could not read {sys.argv[1]}")
    elif len(sys.argv) <= 2:
        sys.exit("Too few command-line arguments")
    else:
        sys.exit("Too many command-line arguments")


if __name__ == "__main__":
    main()
