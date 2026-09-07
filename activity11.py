#import demo #it hides your password or hides the text you put
import getpass #folder

name = "name1"
password = "asuka16"

u = input("Put your Username >> ")
p = getpass.getpass("Put your Password >> ")

if u == name and p == password: 
	print("Username and Password are correct!")
else:
	print("Incorrect username or password")
