import pyfiglet
import sys
fonts = pyfiglet.FigletFont.getFonts()

if len(sys.argv) == 1:
    s = input("Input: ")
    print(pyfiglet.figlet_format(s))

elif len(sys.argv) == 3 and sys.argv[1] == '-f' and sys.argv[2] in fonts:
    s = input("Input: ")
    print(pyfiglet.figlet_format(s, font = sys.argv[2]))
else:
    sys.exit("Invalid usage")
