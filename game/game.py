import random
while True:
    level = input("Level: ")
    try:
        n = random.randint(1, int(level))
        if int(level) >= 1:
            while True:
                try:
                    guess = int(input("Guess: "))
                    if guess >= 1:
                        if guess > n:
                            print("Too large!")
                        elif guess < n:
                            print("Too small!")
                        else:
                            print("Just right!")
                            break
                except ValueError:
                    pass
            break
    except ValueError:
        pass
