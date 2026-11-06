
from getpass import getpass
isLogin = False
loginAttempt = 0

print("\n>>============================<<")
user = input("\nPut your Username -->> ")
passw = getpass("Put your Password -->> ")
print("\n>>============================<<")

while isLogin == False:
    uname = input("\nUsername: ")
    pw = getpass("Password: ")
    
    if uname == user and pw == passw:
        print("\nYou've been successfully Login")
        print("Login attempts ", loginAttempt)
        isLogin = True
    else:
        print("Try Again..")
        loginAttempt += 1
        isLogin = False
