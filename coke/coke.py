print("Amount Due: 50")
value = 50
while value > 0:
    pay = int(input("Insert Coin: "))
    if pay == 25 or pay == 10 or pay == 5:
        value -= pay
        if value < 0:
            print(f"Change Owed: {-1*value}")
        elif value == 0:
            print("Change Owed: 0")
        else:
            print(f"Amount Due: {value}")
    else:
        print("Amount Due: 50")
