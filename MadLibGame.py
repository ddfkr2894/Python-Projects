# This algorithm is going to ask to the user for a coulpe of random words
# so the incompleted paragraph will be displayed with those words.

name = str(input("Escribe un nombre   "))
age = int(input("Escribe tu edad   "))
likes = str(input("Escrbie algún gusto en particular   "))
lifeStyle = str(input("Escribe tu profesión o la de alguien mas    "))
wish = str(input("Desea algo! :)   "))
goodbye = str(input("Ingresa cualquier tipo de despedida      "))

print("¡Hola! Me llamo " + name + "!")
print("tengo " + str(age) +" y me gustan las " + likes + ".")
print("Actualmente soy un " + lifeStyle + " y mi mayor")
print("deseo es " + wish + ".")
print("Por ahora, sólo puedo decir " + goodbye)