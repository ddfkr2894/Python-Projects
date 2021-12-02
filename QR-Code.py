import qrcode
from PIL import Image

# Ingresamos la cadena que queremos hacer QR, puden ser strings o bien en este caso el mismo URL
cadena = "https://drive.google.com/file/d/1T6j__9V0yCvkJKO7yrYaW21Il2HmHoqH/view?usp=sharing"
imagen = qrcode.make(cadena)

nombre_imagen = input("Introduce nombre de la imagen    ") + ".png"
archivo_imagen = open(nombre_imagen, 'wb')
imagen.save(archivo_imagen)
archivo_imagen.close()

ruta_imagen = "./" + nombre_imagen
Image.open(ruta_imagen).show()