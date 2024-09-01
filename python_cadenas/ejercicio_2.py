"""
Escribir un programa que pregunte el nombre completo del usuario
en la consola y después muestre por pantalla el nombre completo del usuario
tres veces, una con todas las letras minúsculas, otra con todas las letras 
mayúsculas y otra solo con la primera letra del nombre y de los apellidos en mayúscula. 
El usuario puede introducir su nombre combinando mayúsculas y minúsculas como quiera.
"""
#Pedimos el nombre del usuario
name_del_usuario = input("Escribe tu nombre completo: ")
#Mostramos el nombre completo en minúsculas
print(name_del_usuario.lower())
#Mostramos el nombre completo en mayusculas
print(name_del_usuario.upper())
#Mostramos la inicial en mayusculas
print(name_del_usuario.title())