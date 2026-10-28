#code challenge 6 THE "X"

for x in range(0, 5):
    for y in range(0, 5):
        if x == y or x+y == 5-1:
            print("*", end="")
        else:
            print(" ", end="")
    print()
