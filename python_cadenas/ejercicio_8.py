"""
Escribir un programa que pregunte por consola 
el precio de un producto en euros con dos decimales y muestre por pantalla 
el número de euros y el número de céntimos del precio introducido.
"""
#Le pedimos al usuario que ingrese el precio del producto
precio_del_producto = input("Ingrerse el precio del producto con 2 decimales: ")
#Luego imprimos cual es el presio en euros y cuanto es en centavos
print(precio_del_producto[:precio_del_producto.find('.')], 'euros con', precio_del_producto[precio_del_producto.find('.')+1:], 'centavos.')