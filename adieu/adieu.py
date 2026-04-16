import inflect
p = inflect.engine()
all = []
try:
    while True:
        s = input("name: ")
        all.append(s)
except EOFError:
    if len(all) == 1:
        print('Adieu, adieu, to ' + all[0])
    else:
        print('Adieu, adieu, to ' + p.join(all))
