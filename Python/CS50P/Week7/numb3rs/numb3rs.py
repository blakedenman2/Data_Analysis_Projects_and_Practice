import re


def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip):
    try:
        ip = re.search(r"^([0-9]{1,3})\.([0-9]{1,3})\.([0-9]{1,3})\.([0-9]{1,3})$", ip)
        if ip:
            for group in ip.groups():
                if not 0 <= int(group) <= 255:
                    return False
            return True
        else:
            return False
    except (ValueError, TypeError, re.error):
                    return False

if __name__ == "__main__":
    main()
