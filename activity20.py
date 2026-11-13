#While loop and list
#understand each lines of your code :3

movie = []

isContinue = True

while isContinue == True:
    ans = input("Do you movie any movies? (Yes | No) ").lower()

    if ans == "yes":
        title = input("What title of the Movie do you movie -->> ")
        movie.append(title)
        ans = input("Do you wish to continue? (Yes | No) ").lower()
        if ans == "yes":
            print("Continue")
            continue
    else:
        print(movie)
