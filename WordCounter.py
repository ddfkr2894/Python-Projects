# This algorithm counts the words given by the user inside an input

text = str(input("¿En qué estás pensando ahora? "))
# This method split() use as a default separator the spaces but it can receive antoher kind of parameters
# dots and comas, letters, numbers or special characteres as well
result = len(text.split())
print("¡Genial! Haz mostrado tu pensamiento en " + str(result) + " palabras!")