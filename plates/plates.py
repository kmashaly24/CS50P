import re
def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

def is_valid(s):

    if len(s) <= 6 and len(s) >= 2 and s.isalnum():
        if s.isalpha():
            return True
        else:
            for i in s:
                if i.isdigit():
                    x = s.index(i)
                    break
            if len(s[0:x]) >= 2 and s[x:].isdigit() and s[x] != "0":
                return True
            else:
                return False
    else:
        return False

if __name__ == "__main__":
    main()





