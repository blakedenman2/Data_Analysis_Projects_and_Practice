uppercase = ("ABCDEFGHIJKLMNOPQRSTUVWXYZ")

def main():
    camel = (input("camelCase: "))
    snake = replace(camel)
    print("snake_case:",snake)


def replace(camel):
    snake = ""
    for letter in camel:
        if letter in uppercase:
            snake += "_" + letter.lower()
        else:
            snake += letter
    snake = snake.lstrip("_")
    return snake
main()
