s = input("Expression:")
s = s.split()
x = float(s[0])
y = s[1]
z = float(s[2])

if y == "+":
    print(x+z)
elif y == "-":
    print(x-z)
elif y == "*":
    print(x*z)
elif y == "/":
    print(x/z)
else:
    print("operation not found")
