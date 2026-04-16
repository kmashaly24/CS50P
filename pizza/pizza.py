import sys
import csv
from tabulate import tabulate

l = []

if len(sys.argv) > 2:
    sys.exit("Too many command-line arguments")

elif len(sys.argv) == 1:
    sys.exit("Too few command-line arguments")

else:
    if sys.argv[1].endswith(".csv"):
        try:
            with open(sys.argv[1]) as file:
                reader = csv.DictReader(file)
                for line in reader:
                    l.append(line)

        except FileNotFoundError:
            sys.exit("File does not exist")

        print(tabulate(l, headers="keys", tablefmt="grid"))

    else:
        sys.exit("Not a csv file")


