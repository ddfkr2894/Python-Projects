from os import error
import qrcode
from PIL import Image

logo = Image.open("./img/80enFrances.png")

hsize = int((float(logo.size[1]) * float(100/float(logo.size[0]))))
logo = logo.resize((100, hsize), Image.ANTIALIAS)
QRcode = qrcode.QRCode(error_correction = qrcode.constants.ERROR_CORRECT_H)

QRimg = QRcode.make_image(fill_color = 'Grey', back_color = 'White').convert('RGB')

pos = ((QRimg.size[0] - logo.size[0]) // 2,(QRimg.size[1] - logo.size[1]) // 2)
QRimg.paste(logo, pos)

QRimg.save("./GeneratedFiles/80enFrancesQR.png")