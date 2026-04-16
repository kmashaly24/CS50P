import re
import sys


def main():
    print(convert(input("Hours: ")))


def convert(s):

    if input := re.search("((\d\d?)(?:\:[0-5]\d)?) (A|P)M to ((\d\d?)(?:\:[0-5]\d)?) (A|P)M", s):
        if input.group(3) == "A" and int(input.group(2)) <= 12 and int(input.group(5)) <= 24:
                if input.group(1)[0:2] == "12":
                    start = "00:00"
                elif ':' not in input.group(1):
                    start = input.group(1) + ':00'
                else:
                    start = input.group(1)

                if input.group(1)[0:2] == "12":
                    end = "12:00"
                elif ':' not in input.group(4):
                    end = str(int(input.group(4)) + 12) + ':00'
                else:
                    end = str(int(input.group(4).split(":")[0]) + 12) + ":" + input.group(4).split(":")[1]


                result = start.zfill(5) + ' to ' + end.zfill(5)
                return result
        elif input.group(3) == "P" and int(input.group(2)) <= 24 and int(input.group(5)) <= 12:
                if input.group(1)[0:2] == "12":
                    end = "00:00"
                elif ':' not in input.group(4):
                    end = input.group(4) + ':00'
                else:
                    end = input.group(4)

                if input.group(1)[0:2] == "12":
                    start = "12:00"
                elif ':' not in input.group(1):
                    start = str(int(input.group(1)) + 12) + ':00'
                else:
                    start = str(int(input.group(1).split(":")[0]) + 12) + ":" + input.group(1).split(":")[1]

        else:
                raise ValueError("Out of range")

        result = start.zfill(5) + ' to ' + end.zfill(5)
        return result
    else:
        raise ValueError("This format is not acceptable.")



if __name__ == "__main__":
    main()
