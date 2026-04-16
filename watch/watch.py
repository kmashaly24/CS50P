import re
import sys


def main():
    print(parse(input("HTML: ")))


def parse(s):
    if url := re.search("\"https?://(www\.)?youtube\.com/embed/([a-zA-Z0-9]+)\"><", s):
        output = f"https://youtu.be/{url.group(2)}"
        return output
    else:
        return None


if __name__ == "__main__":
    main()
