def Lin(lis, key):
    found = False
    for i in range(len(lis)):
        if key == lis[i]:
            print(f"Item found at position {i+1}")
            found = True
    if not found:
        print("Item is not in the list")

if __name__ == "__main__":
    lis = [2, 3, 4, 5, 2]
    key = int(input("Gimme number: "))
    Lin(lis, key)
