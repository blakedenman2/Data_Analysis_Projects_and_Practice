import emoji

def main():
    sentence = input("Input: ")
    print(emoji.emojize(f"Output: {sentence}", language="alias"))


main()
