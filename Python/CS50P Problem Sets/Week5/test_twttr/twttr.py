vowels = list("AaEeIiOoUu")


def main():
    word = input("Input: ")
    print(f"Output: {shorten(word)}")


def shorten(word):
    fix = ""
    for i in word:
        if i in vowels:
            fix += ""
        else:
            fix += i
    return fix


if __name__ == "__main__":
    main()
