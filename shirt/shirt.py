from PIL import Image, ImageOps
import sys
import os

extentions = [".jpg" ,".jpeg" ,".png"]

if len(sys.argv) < 3:
    sys.exit("Too few command-line arguments")

elif len(sys.argv) > 3:
    sys.exit("Too many command-line arguments")

else:
    extention1 = os.path.splitext(sys.argv[1])[1]
    extention2 = os.path.splitext(sys.argv[2])[1]

    if extention1 == extention2 and extention1 in extentions:
        try:
            before = Image.open(sys.argv[1])

        except FileNotFoundError:
            sys.exit("Input does not exist")

        shirt = Image.open("shirt.png")
        size = shirt.size
        after = ImageOps.fit(before, size)
        after.paste(shirt, shirt)
        after.save(sys.argv[2])

    elif extention1 != extention2:
        sys.exit("Input and output have different extensions")

    else:
        sys.exit("Invalid output")

