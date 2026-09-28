age = int(input("Your age: "))
rev = float(input("Enter monthly: "))
cc = int(input("Enter your Credit Score: "))
yrs_b = int(input("How long your business: "))
has_default = bool(input("Default History: "))
collateral = input("Collateral Name: ")
c_value = float(input("Collateral Value: "))


max_loan = 0
base_fee = 0.0


if age >= 21 and yrs_b >= 2.0 and has_default == False:
  print("Baseline requirements passed")
  
  if cc >= 720: #tier1
    max_loan = rev * 3
    pass
    if rev >= 50000:
      base_fee = max_loan * 0.015
      print("Base fee rate is ",base_fee)
  else:
    base_fee = max_loan * 0.025
    print("Base fee rate is ",base_fee)


if 

