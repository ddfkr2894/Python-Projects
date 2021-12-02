import qrcode
from PIL import Image

# Indicamos el nombre y ruta de la imagen que tendrá en el centro el código
imagenlogo = r'./pandemicDays.jpg'
logo = Image.open(imagenlogo)

# Ajustamos el tamaño de la imagen
hsize = int((float(logo.size[1])*float(100/float(logo.size[0]))))
logo = logo.resize((100, hsize), Image.ANTIALIAS)
QRcode = qrcode.QRCode(error_correction=qrcode.constants.ERROR_CORRECT_H)

# Llenamos de datos el código QR
url = 'https://drive.google.com/file/d/1T6j__9V0yCvkJKO7yrYaW21Il2HmHoqH/view?usp=sharing' #URL del Código
QRcode.add_data(url)
QRcode.make

# Le damos un color al código y un color al fondo
QRcolor = 'Green'
QRfondo = 'White'

# Agregamos nuestra imagen al código QR
QRimg = QRcode.make_image(fill_color=QRcolor, back_color=QRfondo).convert('RGB')

#Establecemos la posicion de la imagen, en este caso será el centro.
pos = ((QRimg.size[0] - logo.size[0]) // 2,(QRimg.size[1] - logo.size[1]) // 2)
QRimg.paste(logo, pos)

# Guardamos la imagen de nuestro código QR en un directorio
QRimg.save(r'./QR-CodePersonalized.png')