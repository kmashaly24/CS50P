def main():

    time = input("What time is it?")
    t = convert(time)
    
    if t >= 7 and t <= 8:
        print("breakfast time")
    elif t >= 12 and t <= 13:
        print("lunch time")
    elif t >= 18 and t <= 19:
        print("dinner time")
    else:
        pass

def convert(time):
        if "a.m." in time:
            time = time.split(":")
            time = int(time[0]) + int(time[1].split()[0])/60
            return time
        elif "p.m." in time:
            time = time.split(":")
            time = int(time[0]) + int(time[1].split()[0])/60 + 12
            return float(time)
        else:
            time = time.split(":")
            time = int(time[0]) + int(time[1])/60
            return time


if __name__ == "__main__":
    main()



