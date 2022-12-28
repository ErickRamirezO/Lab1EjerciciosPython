import os

def archivos(opcion):
	'''
    Funcion que permite abrir los diferentes ejercicios segun la opción que se haya ingresado

    Parametros:
    ------------
        opcion: int

    Retorna:
    ------------
        No retorna ningún valor
    '''
	#Sentencia match que recibe la opcion del usuario
	match opcion:
		#Si la opcion es 3
		case 3:
			#Se limpia la pantalla
			os.system ("clear")
			#Se abre el archivo ejer3.py
			os.system("python ejer3.py")
		#Si la opcion es 5
		case 5:
			#Se limpia la pantalla
			os.system ("clear")
			#Se abre el archivo ejer5.py
			os.system("python ejer5.py")
		#Si la opcion es 8
		case 8:
			#Se limpia la pantalla
			os.system ("clear")
			#Se abre el archivo ejer8.py
			os.system("python ejer8.py")
		#Si la opcion es 11
		case 11:
			#Se limpia la pantalla
			os.system ("clear")
			#Se abre el archivo ejer11.py
			os.system("python ejer11.py")
		#Si la opcion es 14
		case 14:
			#Se limpia la pantalla
			os.system ("clear")
			#Se abre el archivo ejer14.py
			os.system("python ejer14.py")
		#Si la opcion es 15
		case 15:
			#Se limpia la pantalla
			os.system ("clear")
			#Se abre el archivo ejer15.py
			os.system("python ejer15.py")
		#Si la opcion es 16
		case 16:
			#Se limpia la pantalla
			os.system ("clear")
			#Se abre el archivo ejer16.py
			os.system("python ejer16.py")
		#Si la opcion es 18
		case 18:
			#Se limpia la pantalla
			os.system ("clear")
			#Se abre el archivo ejer18.py
			os.system("python ejer18.py")
		#Si la opcion es 19
		case 19:
			#Se limpia la pantalla
			os.system ("clear")
			#Se abre el archivo ejer19.py
			os.system("python ejer19.py")
		#Si la opcion es 22
		case 22:
			#Se limpia la pantalla
			os.system ("clear")
			#Se abre el archivo ejer22.py
			os.system("python ejer22.py")
		#Si la opcion no es ninguno de los casos anterior
		case _:
			#Se limpia la pantalla
			os.system ("clear")
			#Se vuelve al menú principal
			menu()

def validacionOpcion():
	'''
    Funcion que permite validar que la opcion que ingrese el usuario sea un numero entero

    Parametros:
    ------------
        No tiene parámetros

    Retorna:
    ------------
        No retorna ningún valor
    '''
	while True:
		#Se prueba el siguiente bloque
		try:
			#solicitamos al usuario ingresar el valor de la opcion deseada
			opcion = int(input("Ingresa una opcion: "))
			#Se rompe el ciclo
			break
		#Se maneja el error
		except ValueError:
			#Imprime mensaje de advertencia
			print("El valor ingresado no es valido, ingresa de nuevo")
	#Se llama a la funcion archivos enviando como parametro la opcion ingresada por el usuario
	archivos(opcion)		
			
def menu():	
	'''
    Funcion que permite mostrar por pantalla el menu principal con los programas realizados

    Parametros:
    ------------
        No tiene parámetros

    Retorna:
    ------------
        No retorna ningún valor
    '''
	#Imprimos la bienvenida al usuario
	print("\n\tBIENVENIDO Usuari@\n")
	#Imprimimos todas las opciones
	print("3.- Dados dos longitudes ingresadas por el usuario...")
	print("5.- Calcular la siguiente expresión y = x^z/2")
	print("8.- Ingresar el radio de un circulo del usuario y calcule el área")
	print("11.- Ingresar un valor en libras y transformarlo a kilo y gramos")
	print("14.- Ingresar un valor en dólares y transformar en euros y yen")
	print("15.- Resuelva la siguiente ecuacion ((-1)k+1)/(2k-1)...")
	print("16.- Encontrar el diámetro, la circunferencia y el área del círculo")
	print("18.- Ingresar dos números y realizar todas las operaciones aritméticas")
	print("19.- Ingresar la longitud y el ancho de un rectángulo y encontrar su perímetro")
	print("22.- Calcular la fórmula de la velocidad")
	#Se hace el llamado a la funcion validacionOpcion
	validacionOpcion()
	

if __name__ == "__main__":
	#Llamamos a la funcion para mostrar menu principal
	menu()