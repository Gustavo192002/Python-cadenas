"""
Escribir un programa que pida al usuario que introduzca una frase
en la consola y una vocal, y después muestre por pantalla la misma frase
pero con la vocal introducida en mayúscula.
"""
#Le pedimos al usuario que ingrese su frase 
frase = input("Ingrese una frase: ")
#Le pedimos que ingrese la inicial qen minuscula
vocal_en_minuscula = input("Introduce una vocal en minuscula:  ")
#Imprimos la frase y la vocal que colocamos la volvemos en mayusculas 
print(frase.replace(vocal_en_minuscula, vocal_en_minuscula.upper()))