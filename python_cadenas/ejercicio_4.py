"""
Los teléfonos de una empresa tienen el siguiente formato prefijo-número-extension 
donde el prefijo es el código del país +34, y la extensión tiene dos dígitos
(por ejemplo +34-913724710-56). Escribir un programa que pregunte por un número de teléfono
con este formato y muestre por pantalla el número de teléfono sin el prefijo y la extensión.
""" 
#le pedimos al usuario que ingrese le numero de telefono con el formato "+xx-xxxxxxxxx-xx"
numero_de_telefono = input("Ingrese le numero de telefono con el formato +xx-xxxxxxxxx-xx: ")
#Imprimos el numero de telefono y eliminamos el codigo de area y los ultimos 2 numerosa
print('El numero de telefono es ', numero_de_telefono[4:-3])