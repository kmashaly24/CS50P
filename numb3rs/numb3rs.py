import re
import sys

def main():
    print(validate(input("IPv4 Address: ")))

def validate(ip):
    if re.match(r"^\d+\.\d+\.\d+\.\d+$", ip):
        l = ip.split(".")
        l = [1 for x in l if int(x)<=255]
        print(l)
        if len(l) == 4:
            return True
        else:
            return False
    else:
        return False

if __name__ == "__main__":
    main()
