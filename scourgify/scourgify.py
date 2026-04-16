import sys
import csv

l = []

if len(sys.argv) < 3:
    sys.exit("Too few command-line arguments")

elif len(sys.argv) > 3:
    sys.exit("Too many command-line arguments")

else:
    try:
        with open(sys.argv[1]) as file:
            reader = csv.DictReader(file)
            for line in reader:
                dict = {}
                dict["first"] = line["name"].split(",")[1].strip()
                dict["last"] = line["name"].split(",")[0].strip()
                dict["house"] = line["house"]
                l.append(dict)

    except FileNotFoundError:
        sys.exit(f"Could not read {sys.argv[1]}")

    try:
        with open(sys.argv[2], 'w', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=['first', 'last', 'house'])
            writer.writeheader()
            writer.writerows(l)

    except FileNotFoundError:
        sys.exit(f"Could not read {sys.argv[2]}")



