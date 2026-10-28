#Code challenge 7 Floyd's Triangle

add = 1

for x in range(0,5,1):
    for y in range(-1,x):
        print(add, end= " ")
        add = add + 1
    print()
