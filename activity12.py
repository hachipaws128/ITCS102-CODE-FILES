#multiple if and elif conditions

#create a python program that would capture age group


print("========= LOG IN ============")

name = input("Please input your name -->> ")
age = int(input("Please input your age -->> "))


print("\n=========== RECOGNATION AS ========== ")

if age >= 0 and age <= 5:
	print("You are considered as INFANT")
elif age >= 6 and age <= 10:
	print("You are considered as KID")
elif age >= 11 and age <= 17:
	print("You are considered as PRE-TEEN")
elif age >= 18 and age <= 25:
	print("You are considered as PRE-ADULTHOOD")
elif age >= 26 and age <= 59:
	print("You are considered as ADULT")
elif age >= 60 and age <= 150:
	print("You are considered as SENIOR")
else:
	print("Invalid Age")

print("\n====================================")