# This algorithm select a certain number in the range of 0 to 10
# Then asks the user to guess which number it could be
# If the user gives a wrong answer the algorithm gives a little hint
# saying if the number is bigger or smaller than the typed one

from random import *

secretNumber = randint(0, 10)
userNumber = int

while (userNumber != secretNumber):
    userNumber = int(input("¡Try to guess the number!   "))
    if (userNumber == secretNumber):
        print("¡Congratulations! ¡That was the number I was thinking about!")
    elif (userNumber > secretNumber):
        print("You're close! Try with a smaller one!")
    elif (userNumber < secretNumber):
        print("You're close! Try with a bigger one!")