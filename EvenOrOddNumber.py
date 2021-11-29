# The following one is just a small algorithm to recognize if certain number is even or odd.
# Also the algorithm asks to the user if wants to repeat the process.
# Everytime the user press 'y' or 'Y' the loop will repeat. Any other key pressed will end loop.

#answerString = 'y'

#while answerString == 'y' or answerString == 'Y':
#    numero = int(input("Ingresa un número:  "))
#    if(numero % 2 == 0):
#        print('El numero es par')
#    else:
#        print('El numero es inpar')
#    answerString = str(input('¿Deseas probar otro número? (Y/N)  '))

# I decided to make the same algorithm using the tkInter library.
import tkinter
from tkinter import *

windowApp = Tk()
windowApp.title("Even or Odd Numbers")
windowApp.geometry("400x150")


def comprobar():
    num = int(textbox1.get())
    if(num % 2 == 0):
        etiqueta2['text'] = "El número es par"
    else:
        etiqueta2['text'] = "El número es inpar"


etiqueta1 = tkinter.Label(windowApp, text="Ingresa un número!")
etiqueta1.pack()
textbox1 = tkinter.Entry(windowApp)
textbox1.pack()
boton1 = tkinter.Button(windowApp, text="Comprobar!", command=comprobar)
boton1.pack()
etiqueta2 = tkinter.Label(windowApp, text='')
etiqueta2.pack()

windowApp.mainloop()