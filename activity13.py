##activity 13

age = int(input("Enter you Age -->> "))
is_employed = bool(input("Are you currently employed? (True/False) -->> "))
credit_score = eval(input("Credit score history -->> "))
annual_income = eval(input("How much is your Annual income? -->> "))
has_collateral = bool(input("Do you have any collateral? -->> "))

base_interest = 0.0

#baseline eligibility
if (age >= 21 and age <= 75) and is_employed == True:
    if credit_score >= 750:
        if annual_income >= 100000:
            base_interest = 4.5
        else:
            base_interest = 5.0
    elif 600 <= credit_score < 750:
        if has_collateral == True:
            base_interest = 7.0
        elif annual_income < 40000:
            base_interest = 9.5
        elif has_collateral == True and annual_income < 40000:
            base_interest = 8.0
        else:
            base_interest = 8.0
    else:
        print("============...Rejected...============ \nRejected: Credit score too low. \nRequirements: Credit score must be at least 600. \n\nPlease try again. \n=======================================")
        exit()
else:
    print("============...Rejected...============ \nRejected: Failed to meet the requirements. \nRequirements: Age between 21 and 75, and must be employed. \n\nPlease try again. \n=======================================")
    exit()

#Details

print("\nYou have been approved for a loan with the following details: ")

print ("\n============...Details...============")
print("Age:", age)
print("Is employed:", is_employed)
print("Credit Score:", credit_score)
print("Annual Income:", annual_income)
print("Has Collateral:", has_collateral)

print("=======================================")
