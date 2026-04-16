def main():
    fraction = input("Fraction: ")
    percentage = convert(fraction)
    print(gauge(percentage))

def convert(fraction):
    while True:
        try:
            s = fraction.split("/")
            x = int(s[0])
            y = int(s[1])
            f = round(x/y, 2)
            if x > y:
                fraction = input("Fraction: ")
            else:
                return f*100
        except(ValueError, ZeroDivisionError):
            raise

def gauge(percentage):
    if percentage >= 99:
        return "F"
    elif percentage <= 1:
        return "E"
    else:
        return f"{int(percentage)}%"

if __name__ == "__main__":
    main()
