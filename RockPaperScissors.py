# This algorithm is just to make the rock paper and scissors game

from random import *

listaOpciones = ["piedra", "papel" ,"tijera"]
computdora = listaOpciones[randint(0, 2)]
respuesta = "y"
nombreJugador = (input("¿Cuál es tu nombre? "))

while (respuesta == "y" or respuesta == "Y"):
    print("¡Que hubolas " + nombreJugador + "! ¡Amos a jugar!")
    print("¿¡Piedra, papel o tijera!?")
    jugador = input("¡Elígele!  ").lower()
    print("Computadora: " + computdora)
    if(jugador == computdora):
        print("¡Enpate! JAJA")
    elif(jugador == "piedra" and computdora == "papel"):
        print("¡La computadora gana! JAJSJA")
    elif(jugador == "piedra" and computdora == "tijera"):
        print("¡Ganaste" + nombreJugador + "¡:D")
    elif(jugador == "papel" and computdora == "piedra"):
        print("¡Ganaste" + nombreJugador + "¡:D")
    elif(jugador == "papel" and computdora == "tijera"):
        print("¡La computadora gana! JAJSJA")
    elif(jugador == "tijera" and computdora == "piedra"):
        print("¡La computadora gana! JAJSJA")
    elif(jugador == "tijera" and computdora == "papel"):
        print("¡Ganaste " + nombreJugador + "¡:D")
    respuesta = input("¿Deseas volver a intentar? Y/N   ")