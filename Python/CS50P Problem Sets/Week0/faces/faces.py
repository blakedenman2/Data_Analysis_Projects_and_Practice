# Ask user to say something
# If smiley, convert to emoji
# If frowny, convert to emoji
# If neither, no change

def main():
    value = input("Say something along with an :( or :) emoticon and I'll make it look cooler!\n ")
    print(value.replace(":)", "🙂").replace(":(", "🙁"))


main()
