print(__name__)
def main():
    m = input("Input: ")
    print(shorten(m))
def shorten(word):
    new = ""
    for i in word:
        if i != "a" and i != "e" and i != "o" and i != "u" and i != "i" and i != "A" and i != "E" and i != "O" and i != "U" and i != "I":
            new += i
    return new


if __name__ == "__main__":
    main()
else:
    print(__name__)
