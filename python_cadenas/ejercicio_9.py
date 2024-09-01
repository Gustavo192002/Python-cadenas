"""
Escribir un programa que pregunte al usuario la fecha de su nacimiento
en formato dd/mm/aaaa y muestra por pantalla, el día, el mes y el año.
Adaptar el programa anterior para que también funcione cuando el día o el mes
se introduzcan con un solo carácter.
"""
#le pedimos al usuario que ingrese su fecha de nacimiento
fecha_de_nacimiento = input("Ingresa la fecha de tu nacimiento usando el formato dd/mm/aaaa: ")
#Buscamos el dia que esta escrito antes del primer "/"
dia = fecha_de_nacimiento[:fecha_de_nacimiento.find('/')]
#Buscamos el primer "/" y tomamos los valores que estan despues de el y los gurdamos en fecha parcial
fecha_parcial = fecha_de_nacimiento[fecha_de_nacimiento.find('/')+1:]
#Extraemos el mes
mes = fecha_parcial[:fecha_parcial.find('/')]
#extraemos el año
año = fecha_parcial[fecha_parcial.find('/')+1:]
#Imprimimos nuestro resultado
print('Día', dia)
print('Mes', mes)
print('Año', año)