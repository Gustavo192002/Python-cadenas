"""
Escribir un programa que pida al usuario que introduzca una frase en la
consola y muestre por pantalla la frase invertida.
"""
#Le pedimos al usuario que introduzca su frase
frase = input("Ingrese una frase: ")

# Invertimos la frase
frase_invertida = frase[::-1]

#Imprimimos la frase invertida
print(frase_invertida)
