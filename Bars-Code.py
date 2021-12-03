# This algorithm generates a bar code
# It is necesary to preinstall the python-barcode module
# That can be done using the command pip install python-barcode

from barcode import EAN13
from barcode.writer import ImageWriter

# Establecemos el directorio donde será guardado
directorio = r'./GeneratedFiles'

# Establecemos el numero del código de barras
# Importante: el modelo EAN debe tener 12 digitos
#numero = "202198447392"
numero = "666666666666"

#Generamos el código con un formato EAN13
mi_codigo = EAN13(numero, writer=ImageWriter())

#Guardamos la imagen en el directorio previamente declarado
mi_codigo.save(directorio+"/ddfkr-Bars-Code")