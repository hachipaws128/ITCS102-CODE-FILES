rows = int(input("Enter how many rows -->> "))

for x in range(rows):
  for y in range(rows - x - 1):
    print(" ", end="")
  for z in range(x + 1):
    print("* ", end="")
  print()

for x in range(rows):
  for y in range(x+1):
    print(" ", end="")
  for z in range(rows - x - 1):
    print("* ", end="")
  print()
