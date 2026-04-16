v = input("camelCase: ")
l = []
for i in v:
    if i.isupper():
        l.append(v[:v.index(i)])
        v = v[v.index(i):]

l.append(v)

snake = "_".join(l)
print(f"snake_case: {snake.lower()}")
