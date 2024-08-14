#Have the user input something
#Replace spaces with "..." after removing white space from either end
#Couldn't figure out how to do a split/join thing to make it so a double space between words would be eliminated and always come out clean

def main():
    original = input("Tell me something, and I'll say it back to you slower: ")
    print(original.strip().replace(" ", "..."))

#Run it

main()
