l = []
dic = {}
while True:
    try:
        order = input()
        l.append(order)
    except EOFError:
        for i in sorted(l):
            if i in dic:
                dic[i] +=1
            else:
                dic[i] = 1
        for k, v in dic.items():
            print(f"{v} {k.upper()}")

        break
