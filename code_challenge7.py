#Code challenge 7 Floyd's Triangle

digit = 1 
for x in range(5):
    for y in range(x + 1):
        print(digit,end=" ")
        digit = digit + 1
    print()
