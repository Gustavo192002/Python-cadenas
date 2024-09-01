"""
Escribir un programa que pregunte por consola por los productos de una cesta
de la compra, separados por comas, y muestre por pantalla cada uno 
de los productos en una línea distinta.
"""
#Le pedimos al usuario que ingrese los productos
productos_para_la_cesta = input("Ingrese los productos de la cesta y separerlos con ',': ")
#Reemplazamos las comas por "\n" usando replace y luego lo imprimimos
print(productos_para_la_cesta.replace(',', '\n'))