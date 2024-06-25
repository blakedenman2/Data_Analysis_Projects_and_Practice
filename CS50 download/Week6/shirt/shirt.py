import sys
import os
from PIL import Image, ImageOps


def main():
    if length() and before_file_type(sys.argv[1]) and after_file_type(sys.argv[2]) and compare_file_type(sys.argv[1], sys.argv[2]):
        try:
            im1 = sys.argv[1]
            im2 = sys.argv[2]
            im1 = Image.open(im1)
        except FileNotFoundError:
            sys.exit("Input does not exist")
        shirt = Image.open("shirt.png")
        size = shirt.size
        im1 = ImageOps.fit(im1, size)
        im1.paste(shirt, mask=shirt)
        im1.save(im2)


def length():
    if len(sys.argv) == 3:
        return True
    elif len(sys.argv) <= 2:
        sys.exit("Too few command-line arguments")
    else:
        sys.exit("Too many command-line arguments")


def before_file_type(before):
    _, ext = os.path.splitext(before)
    if ext.strip().lower() in [".jpeg", ".png", ".jpg"]:
        return True
    else:
        sys.exit("Invalid input")


def after_file_type(after):
    _, ext = os.path.splitext(after)
    if ext.strip().lower() in [".jpeg", ".png", ".jpg"]:
        return True
    else:
        sys.exit("Invalid output")


def compare_file_type(before, after):
    _, before_ext = os.path.splitext(before)
    _, after_ext = os.path.splitext(after)
    if before_ext.strip().lower() == after_ext.strip().lower():
        return True
    else:
        sys.exit("Input and output have different extensions")


if __name__ == "__main__":
    main()
