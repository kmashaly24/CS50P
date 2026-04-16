m = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]
while True:
    try:
        date = input("Date: ")
        if "/" in date:
            date = date.split("/")
            month = date[0].strip()
            day = date[1]
            year = date[2]
            if int(month) <= 12 and int(day) <= 31:
                print(f"{year.strip()}-{str(month).zfill(2)}-{day.zfill(2)}")
                break

        elif "," in date:
            date = date.split(",")
            year = date[1]
            date = date[0].split(" ")
            month = date[0]
            day = date[1]
            if month in m:
                month = str(int(m.index(month))+1)
                if int(month) <= 12 and int(day) <= 31:
                    print(f"{year.strip()}-{str(month).zfill(2)}-{day.zfill(2)}")
                    break

    except IndexError:
        pass
    except ValueError:
        pass
