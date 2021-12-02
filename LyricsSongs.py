# This algorithm display a list of groups or artists, the user can choose between one of them
# After the user has choosen any artist there is going to appear another list of its songs
# So the user can take a look into the lyrics and information of a certain song

artista = ["Avril Lavigne", "Simple Plan", "3 Doors Down",
            "Backstreet Boys", "Kings Of Leon", "Linkin Park",
            "Breaking Benjamin", "Atreyu", "3 Days Grace"]

avrilLavigne = ["Complicated", "I'm With You", "Tomorrow"]
simplePlan = ["Welcome To My Life", "When I'm Gone", "Perfect"]
threeDoorsDown = ["Kryptonite", "Looser", "Here Without You"]
backstreetBoys = ["Everybody", "I Still", "Incomplete"]
kingsOfLeon = ["Find Me", "Sex On Fire", "Use Somebody"]
linkinPark = ["Faint", "In The End", "Breaking The Habit"]
breakingBenjamin = ["Cold", "Diary Of Jane", "Forget It"]
atreyu = ["Lose It", "Lonely", "Super Hero"]
threeDaysGrace = ["I Hate Everything About You", "Home", "I'm a Machine"]

print("\nArtistas a Seleccionar:\n")
artista.sort()
for i in artista:
    print("\t"+i)

artistaOpcion = str(input("\nElige un artista de la lista:   -"))
artistaOpcion.lower()

if(artistaOpcion == artista[0].lower()):
    threeDaysGrace.sort()
    for i in threeDaysGrace:
        print("\t"+i)
if(artistaOpcion == artista[1].lower()):
    threeDoorsDown.sort()
    for i in threeDoorsDown:
        print("\t"+i)
if(artistaOpcion == artista[2].lower()):
    atreyu.sort()
    for i in atreyu:
        print("\t"+i)
if(artistaOpcion == artista[3].lower()):
    avrilLavigne.sort()
    for i in avrilLavigne:
        print("\t"+i)
if(artistaOpcion == artista[4].lower()):
    backstreetBoys.sort()
    for i in backstreetBoys:
        print("\t"+i)
if(artistaOpcion == artista[5].lower()):
    breakingBenjamin.sort()
    for i in breakingBenjamin:
        print("\t"+i)
if(artistaOpcion == artista[6].lower()):
    kingsOfLeon.sort()
    for i in kingsOfLeon:
        print("\t"+i)
if(artistaOpcion == artista[7].lower()):
    linkinPark.sort()
    for i in linkinPark:
        print("\t"+i)
if(artistaOpcion == artista[8].lower()):
    linkinPark.sort()
    for i in linkinPark:
        print("\t"+i)

cancionOpcion = str(input("\n Elige alguna canción  -"))