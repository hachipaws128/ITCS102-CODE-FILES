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
    print("High Credit Score of 720")
    if rev >= 50000:
      base_fee = max_loan * 0.015
      print("Your base fee rate: ",base_fee)
  else:
    base_fee = max_loan * 0.025
    print("Your base fee rate: ",base_fee)
elif cc <= 620 and cc < 720: #tier2
  max_loan = rev * 1.5
  if yrs_b >= 5:
    base_fee = max_loan * 0.02
    print("Your base fee rate: ",base_fee)
  else:
    base_fee = max_loan * 0.035
    print("Your base fee rate: ",base_fee)


