"""
Escribir un programa que pregunte el correo electrónico del usuario en la consola y muestre
por pantalla otro correo electrónico con el mismo nombre 
(la parte delante de la arroba @) pero con dominio ceu.es.
"""
#Le pedimos al usuario que ingrese su correo electronico 
correo_electronico = input("Ingrese su correo electronico: ")
#Reenplazamos lo que esta escrito despues de la @ por @ceu.es usando "find"
print(correo_electronico[:correo_electronico.find('@')] + '@ceu.es')