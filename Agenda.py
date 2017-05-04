'''
Universidad Nacional Autónoma de México
Programa de Tecnología en Cómputo

@author: Francisco J. Martínez Molina
@email: fco.mtz@unam.mx
@date: 06.05.2017
'''

''' Directorio telefónico
Implementar un directorio telefónico donde se almacenen los siguientes datos:
	* Nombre
	* Apellido paterno
	* Número telefónico
	* Correo electrónico
	* Edad
Con las funcionalidades de registro y búsqueda de contactos.
'''

''' Definición de constantes para acceder a la ubicaciones de la lista '''
CONST_NOMBRE = 0
CONST_PATERNO = 1
CONST_NUMERO = 2
CONST_EMAIL = 3
CONST_EDAD = 4

indice = 0
opcion = "n"
agenda = {}

while opcion != "e":
	
	if opcion == 'n':

		print("Registro de nuevo contacto")
		
		nombre = input("Nombre: ")
		paterno = input("Apellido paterno: ")
		numero = input("Número telefónico: ")
		mail = input("Correo electrónico: ")
		edad = int(input("Edad: "))

		agenda = {indice:[nombre, paterno, numero, mail, edad]}
		++indice
    
	elif opcion == 'b':
		buscarNombre = input("Ingresa nombre del contacto: ")
		'''@TODO implementar método para la búsqueda de contactos. '''

	else :
		print("Opcion no valida..!")

	print("Eleje una opcion: ")
	print("Nuevo contacto (n)\tBuscar (b)\tSalir (e)")
	opcion = input("Ingresa opcion: ")