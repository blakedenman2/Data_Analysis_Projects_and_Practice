grocery_list = {}

while True:
    try:
        # get item and add to dict, count how many are in the dict
        key = input("").upper()
        if key in grocery_list:
            grocery_list[key] += 1
        else:
            grocery_list[key] = 1
    except KeyError:
        pass
    except EOFError:
        #return alphabetized list with count
        print("\n", end="")
        alphabetized_list = sorted(grocery_list.keys())
        for key in alphabetized_list:
            print(grocery_list[key], key)
        break



# blank line asking for input
# take input (case insensitive) and store it - dict?
# if more than one of something, count it somehow?
# Catch KeyError - I suppose if they press enter again or something like that, and reprompt I guess
# provide new line for input until ctrl-d is entered
# if EOFError - new line, then print items in alphabetical order with label of how many there are (all uppercase)
