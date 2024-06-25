vowels = list("AaEeIiOoUu")

def main():
    word = input("Input: ")
    print(f"Output: {conv(word)}")

def conv(word):
    fix = ""
    for i in word:
        if i in vowels:
            fix += ""
        else:
            fix += i
    return fix

main()
