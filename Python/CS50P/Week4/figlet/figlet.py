import random
import sys
from pyfiglet import Figlet

figlet = Figlet()
#get list of available fonts
font_list = figlet.getFonts()


def main():
    chosen_font = set()
    text = input("Input: ")
    #you can set the font with code like this, wherein f is the font’s name as a str:
    figlet.setFont(font=chosen_font)
    # you can output text in that font with code like this, wherein s is that text as a str:
    print(figlet.renderText(text))


def set():
    if len(sys.argv) == 3:
        if sys.argv[1] == "-f" or sys.argv[1] == "--font":
            if sys.argv[2] in font_list:
                return sys.argv[2]
            else:
                sys.exit("Invalid Usage")
        else:
            sys.exit("Invalid Usage")
    elif len(sys.argv) == 1:
        return random.choice(font_list)
    else:
        sys.exit("Invalid Usage")


main()
