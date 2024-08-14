def main():
    greeting = input("Greeting: ")
    print(f"${value(greeting)}")


def value(greeting):
    greeting = greeting.lstrip().title()
    if greeting.startswith("Hello") == True:
        return 0
    elif greeting.startswith("H") == True:
        return 20
    else:
        return 100


if __name__ == "__main__":
    main()
