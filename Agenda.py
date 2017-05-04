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

	'''Registro de nuevo contacto'''
	if opcion == 'n':

		print("Registro de nuevo contacto")
		nombre = input("Nombre: ")
		paterno = input("Apellido paterno: ")
		numero = input("Número telefónico: ")
		mail = input("Correo electrónico: ")
		edad = int(input("Edad: "))

		agenda[indice] = [nombre, paterno, numero, mail, edad]
		indice += 1
    
    '''Búsqueda de contacto por nombre'''
	elif opcion == 'b':

		buscar = input("Ingresa nombre del contacto: ")

		for item in agenda:

			if buscar in agenda[item]:

				print("********** Información del contacto **********")
				print("\n")
				print("Nombre: ",agenda[item][CONST_NOMBRE], agenda[item][CONST_PATERNO])
				print("Tel: ", agenda[item][CONST_NUMERO])
				print("Email: ", agenda[item][CONST_EMAIL])
				print("\n")
				print("****************************************")
				resultado = 1

			else:
				resultado = 0

		if resultado == 0:
			print("****************************************\n")
			print("No se encontraron resultados\n")		
			print("****************************************\n")

    '''Listado de todos los contactos'''
	elif opcion == 'l':

		print("********** Lista de contactos **********")
		
		for item in agenda:
			print("\n")
			print("Nombre: ",agenda[item][CONST_NOMBRE], agenda[item][CONST_PATERNO])
			print("Tel: ", agenda[item][CONST_NUMERO])
			print("Email: ", agenda[item][CONST_EMAIL])
			print("\n")

		print("****************************************")

	else :
		print("Opcion no valida..!")

	print("Eleje una opcion: ")
	print("(n) Nuevo contacto\t(b) Buscar\t(l) Listar agenda\t(e) Salir")
	opcion = input("Ingresa opcion: ")