#list and dictionary
#JJBA list
jotaro = ["Time Stop"]

kakyoin = ["Emerald Splash"]
joseph = ["Hermit Purple"]
dio = ["Time Stop", "Knife throw"]
bucciarati = ["Sticky Finger"]

#Black Clover List
asta = ["Union"]
yuno = ["Dive form"]
yami = ["Dimensional Slash"]
noel = ["Valkyrie"]

#Umamusume 


jjba = ["Jotaro","Kakyoin","Joseph","Dio","Bucciarati"]
black_clover = ["Asta","Yuno","Yami","Noel"]
umamusume = ["GoldShip","Special Week","Tamamo","Agnes Tachyon","Agnes Digital"]

fav = [jjba]
horse = [umamusume]
fantasy = [black_clover]

anime = {"JJBA":fav, "Black Clover":horse, "Umamusume":horse}

print(anime["JJBA"])
print(anime["JJBA"][0][-3])
