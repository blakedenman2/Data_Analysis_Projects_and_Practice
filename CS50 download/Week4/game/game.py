import random
import sys


def main():
    while True:
        try:
            level = int(input("Level: "))
            if level_check(level):
                n = random.randint(1, level)
                test_function(n)
            else:
                continue
        except (TypeError,ValueError):
            continue


def level_check(level):
    while True:
        try:
            int(level)
            if level>0:
                return True
        except:
            return False


def test_function(n):
    while True:
        try:
            n_guess = int(input("Guess: "))
            if n_guess<=0:
                continue
            elif n_guess > n:
                print("Too Large!")
            elif n_guess < n:
                print("Too small!")
            else:
                sys.exit("Just Right!")
        except (TypeError,ValueError):
            continue


main()
