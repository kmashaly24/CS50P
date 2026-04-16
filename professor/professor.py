import random

def main():
    level = get_level()
    score = 0
    trials = 3
    for i in range(10):
        random1, random2 = generate_integer(level)
        while True:
                print(str(random1) + " + " + str(random2) + ' =', end = ' ')
                result = input()
                try:
                    if int(result) == (random1 + random2):
                        score += 1
                        break
                    else:
                        print("EEE")
                        trials -= 1
                        if trials == 0:
                            print(str(random1) + " + " + str(random2) + ' = ' + str(random1 + random2))
                            break
                except ValueError:
                    pass
    print(f"Score: {score}")


def get_level():
        while True:
            try:
                n = int(input("Level: "))
                if n == 1 or n == 2 or n == 3:
                    return n
                    break
            except ValueError:
                pass

def generate_integer(level):
    if level == 1:
        random1 = random.randint(0, 9)
        random2 = random.randint(0, 9)
    elif level == 2:
        random1 = random.randint(10, 99)
        random2 = random.randint(10, 99)
    else:
        random1 = random.randint(100, 999)
        random2 = random.randint(100, 999)
    return random1, random2


if __name__ == "__main__":
    main()
