#Global Freight Calculator



name = input("Put your name -->> ")
product = input("Put your product name -->> ")
weight = float(input("Put your weight (kg) of product -->> "))
distance = float(input("How far is your Location (km)? -->> "))
is_express = input("Is it Express? (True/False) -->> ").upper() == "true"
is_international = input("Is it International? (True/False) -->> ").upper() == "true"
is_rush = input("Do you want to rush your order? (True/False) -->> ").upper() == "true"
fragile = input("Is it Fragile? (True/False) -->> ").upper() == "true"

base_cost = (weight * 2.50) + (distance * 0.15)

if weight <= 2.0 and distance <= 50 and is_express == True and is_international == True and is_rush == True:
    total = 0.00

elif is_express:
    total = base_cost * 1.5

elif is_international:
    total = base_cost * 2.0

elif is_rush:
    total = base_cost * 1.70

else:
    total = base_cost

print("\n============...Shipping Details...============")
print("Client Name: ", name)
print("Type of Item: ", product)
print("Shipping Cost: $", total)
print("=============...Kg & Km Details...============")
print("Weight: ", weight, "kg")
print("Distance: ", distance, "km")
print("=============...Shipping Options...============")
print("Is international: ", is_international)
print("Is express: ", is_express)
print("Is fragile: ", fragile)
print("================================================")