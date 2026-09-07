#selection statement / conditional statement

#if, else

name = "name1"
password = "asuka16"

u = input("Put your Username >> ")
p = input("Put your Password >> ")

if u == name and p == password: 
	print("Username and Password are correct!")
else:
	print("Incorrect username or password")
