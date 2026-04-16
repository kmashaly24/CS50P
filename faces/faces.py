em = input()


def convert(s):
    s = s.replace(":(", "🙁")
    s = s.replace(":)", "🙂")
    print(s)
convert(em)
