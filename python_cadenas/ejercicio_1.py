"""
Escribir un programa que pregunte el nombre del usuario en la consola y un número entero 
e imprima por pantalla en líneas distintas el nombre del usuario tantas veces como el 
número introducido
"""
#pedimos el nombre al usuario
nombre_del_usuario = input("Ingrese su nombre: ")
#pedimos cuantas veces queremos que se repita su nombre
numero_entero = int(input("Cuantas veces quiere repetir su nombre: "))
#lo imprimimos en la consola la operacion de multilicar el nombre del usario y las veces
#que queremos que se repita su nombre y agregamos el "\n" para los saltos entre lineas
print ((nombre_del_usuario + "\n") * (numero_entero))