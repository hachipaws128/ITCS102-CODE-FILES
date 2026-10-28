size = int(input("Input the Size -->> "))

for x in range(0,5):
    for y in range(0,5):
        if x + y == size-1 or x==y :
          print("*",end = " ")
        else:
           print(" ", end= " ")
    print()
