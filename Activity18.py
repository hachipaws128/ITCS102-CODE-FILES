#The while loop: Drain until empty

come = True

while come == True:
    ask = input("Are you still there? ")
    
    if ask.lower() == "yes":
        print("Oh, Okay let's keep going! ")
        continue
    else:
        print("I think you left...")
        break

