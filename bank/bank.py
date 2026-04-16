def main():
    s = input("Greating:").strip()
    print(f"${value(s)}")

def value(greeting):
    if greeting.startswith("Hello"):
        return 0
    elif greeting.startswith("H"):
        return 20
    else:
        return 100

if __name__ == "__main__":
    main()
