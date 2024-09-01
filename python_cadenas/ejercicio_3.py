"""
Escribir un programa que pregunte el nombre del usuario en la consola y después
de que el usuario lo introduzca muestre por pantalla <NOMBRE> 
tiene <n> letras, donde <NOMBRE> es el nombre de usuario en mayúsculas y <n> es el 
número de letras que tienen el nombre.
"""
#Pedimos el nombre del usuario
nombre_del_usuario = input("Ingrese su nombre: ")

#Convertimos el nombre en mayusculas
nombre_en_mayusculas = nombre_del_usuario.upper()

#Contamos cuantas letras tiene el nombre
cantidad_de_letras = len(nombre_del_usuario.replace(" ", ""))

# Mostrar el resultado
print(f"{nombre_en_mayusculas} tiene {cantidad_de_letras} letras")
