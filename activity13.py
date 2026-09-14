##activity 13

age = int(input("Enter you Age -->> "))
is_employed = bool(input("Are you currently employed? (True/False) -->> "))
credit_score = eval(input("Credit score history -->> "))
annual_income = eval(input("How much is your Annual income? -->> "))
has_collateral = bool(input("Do you have any collateral? -->> "))

base_interest = 0.0

#baseline eligibility
if age >= 21 and is_employed == True:
    if credit_score >= 750:
        if has_collateral == True:
            pass
        elif True:
            pass
        else:
            pass
    else:
        pass
else:
    print("Declined, You did not reach the requirements")

if age >= 21 and is_employed == True:
    if credit_score >= 750:
        if has_collateral == False:


##f credit_score >=


# 500 below is low-credit score 750 is considered as high-credit score