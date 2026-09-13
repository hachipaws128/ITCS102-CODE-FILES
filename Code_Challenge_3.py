#Global Freight Calculator

## This program calculates the shipping cost based on user input for item type, weight, distance, and shipping options.
name = input("Put your name -->> ")
product = input("Put your product name -->> ")
weight = float(input("Put your weight (kg) of product -->> "))
distance = float(input("How far is your Location (km)? -->> "))
is_express = input("Is it Express? (True/False) -->> ").upper() == "true"
is_international = input("Is it International? (True/False) -->> ").upper() == "true"
fragile = input("Is it Fragile? (True/False) -->> ").upper() == "true"

#Calculating the base cost of shipping
base_cost = (weight * 2.50) + (distance * 0.15)

# Calculating the total cost of shipping based on conditions
if weight <= 2.0 and distance <= 100 and is_express == True and is_international == False:
    total = 0.00
elif is_international and is_express:
    total = (base_cost * 1.40) + 50
elif is_express or (is_international and weight > 20):
    total = (base_cost * 1.20) + 25
elif weight > 10 or distance > 1000:
    total = base_cost + 30
else:
    total = base_cost

# Displaying the shipping details
print("\n============...Shipping Details...============")
print("Client Name: ", name)
print("Type of Item: ", product)
print("Shipping Cost: $", total)
print("Weight: ", weight, "kg")
print("Distance: ", distance, "km")
print("Is international: ", is_international)
print("Is express: ", is_express)
print("Is fragile: ", fragile)
print("================================================")
