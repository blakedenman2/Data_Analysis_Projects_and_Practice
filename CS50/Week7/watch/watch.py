import re
import sys


def main():
    print(parse(input("HTML: ")))


def parse(s):
    try:
        if html := re.search(r"^<iframe.*(https?://(?:www\.)?youtube.com/embed/xvFZjo5PgG0).*iframe>$", s):
            url = html.group(1)
            short = re.sub(r"^https?://(www\.)?youtube.com/embed/xvFZjo5PgG0$", "https://youtu.be/xvFZjo5PgG0", url)
            return short
        else:
            return None
    except (TypeError, re.error, ValueError):
        sys.exit("Broke")


if __name__ == "__main__":
    main()
