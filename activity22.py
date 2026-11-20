#list and dictionary
jotaro_a = ["Time Stop", "Barrage", "Enhanced Senses", "Star Finger"]
kakyoin_a = ["Emerald Splash", "Marionette Control", "Coiled Body & Unraveling"]
joseph_a = ["Sun-like energy", "Thorny vines", "Divination"]
dio_a = ["The World", "Hermit Purple-like Vine Stand", "Space Ripper Stingy Eyes"]

asta_w = ["Demon-Slayer Sword", "Demon-Dweller Sword", "Demon-Destroyer Sword", "Devil Union"]
yuno_p = ["Wind Magic & Creation Magic", "Star Magic", "Spirit Magic & Spirit Dive"]
yami_p = [""]
noelle_p = [""]

goldship_s = [""]
sw_s = [""]
tamamo_s = [""]
agnest_s = [""]
agnesd_s = [""]

rem_p = [""]
ram_p = [""]
subaru_p = [""]
meili_p = [""]
emilia_p = [""]



jotaro = jotaro_a
kakyoin = kakyoin_a
joseph = joseph_a
dio = dio_a

asta = asta_w
yuno = yuno_p
yami = yami_p
noelle = noelle_p

goldship = goldship_s
specialw = sw_s
tamamo = tamamo_s
agnest = agnest_s
agnesd = agnesd_s

rem = rem_p
ram = ram_p
subaru = subaru_p
meili = meili_p
emilia = emilia_p



jjba = {"Jotaro":jotaro,"Kakyoin":kakyoin,"Joseph":joseph,"Dio":dio}
black_clover = {"Asta","Yuno","Yami","Noelle"}
umamusume = {"GoldShip","Special Week","Tamamo","Agnes Tachyon","Agnes Digital"}
zero = {"Rem":rem,"Ram":ram,"Subaru":subaru,"Meili":meili,"Emilia":emilia}

fav = {"Jojo's Bizzare Adventure":jjba, "Umamusume":umamusume}
fantasy = {"Black Clover":black_clover, "Re:Zero":zero}

anime = {"JJBA":fav, "Black Clover":fantasy, "Umamusume":fav, "Re:Zero":fantasy}

print(anime["JJBA"])
print(anime["JJBA"][0][-3])
