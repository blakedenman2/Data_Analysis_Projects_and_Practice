def main():
    greeting = input("Greeting: ").title()
    greeting = greeting.lstrip()
    if greeting.startswith("Hello") == True :
        print("$0")
    elif greeting.startswith("H") == True :
        print("$20")
    else : print("$100")


main()
