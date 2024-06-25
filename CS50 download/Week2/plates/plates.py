def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    if two(s) and size(s) and char(s) and nums(s):
        return True
    else:
        return False

numbers = ("1234567890")
letters = ("ABCDEFGHIJKLMNOPQRSTUVWXYZ")

def two(s):
    for i in s[0:2]:
        if i in numbers:
            return False
    return True
#“All vanity plates must start with at least two letters.”

def size(s):
    s = list(s)
    if 2 <= len(s) <= 6:
        return True
    else:
        return False
#“… vanity plates may contain a maximum of 6 characters (letters or numbers) and a minimum of 2 characters.”

def nums(s):
    s = list(s)
    del s[0:2]
    s = "".join(s)
    s = s.lstrip("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
    if s.find("0") == 0:
        return False
    else:
        s = s.rstrip("1234567890")
        s = list(s)
        if len(s) == 0:
            return True
        else:
            return False

#could use rstrip to strip numbers and then lstrip(2) to get the left two letters away
#then check if the remaining string isalpha() - which is True if only letters remain, false if not
# have to add a contingency for if there are no more digits remaining (like the two left were stripped and the others were numbers)
#“Numbers cannot be used in the middle of a plate; they must come at the end. For example, AAA222 would be an
#acceptable … vanity plate; AAA22A would not be acceptable. The first number used cannot be a ‘0’.”

def char(s):
    for i in s:
        if i in numbers or i in letters:
            continue
        else:
            return False
    return True
#“No periods, spaces, or punctuation marks are allowed.”

main()
