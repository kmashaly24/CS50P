import re
import sys

def main():
    print(count(input("Text: ")))

def count(s):
    s = " " + s
    output = re.findall("\Wum\W*", s, flags=re.IGNORECASE)
    return len(output)

if __name__ == "__main__":
    main()
