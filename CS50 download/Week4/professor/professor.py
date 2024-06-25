import random
options = [1,2,3]


def main():
    asked =0
    correct =0
    eee =0
    level = get_level()
    while True:
        try:
            if asked <10:
                a = generate_integer(level)
                b = generate_integer(level)
                asked +=1
                while True:
                    try:
                        answer = int(input(f"{a} + {b} = "))
                        if answer==a+b:
                            correct +=1
                            eee =0
                            break
                        else:
                            raise ValueError
                    except:
                        print("EEE")
                        eee +=1
                        if eee ==3:
                            print(f"{a} + {b} = {a+b}")
                            eee =0
                            break
            else:
                raise EOFError
        except EOFError:
            print(f"Score: {correct}")
            return False


def get_level():
    while True:
        try:
            level = int(input("Level: "))
            if level in options:
                return level
        except:
            continue


def generate_integer(level):
    if level ==1:
        rando = random.randint(0,9)
        return rando
    elif level ==2:
        rando = random.randint(10,99)
        return rando
    else:
        rando = random.randint(100,999)
        return rando


if __name__ == "__main__":
    main()
