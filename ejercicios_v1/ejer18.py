#Ingresar dos números y realizar todas las operaciones aritméticas
import os
def ingresoDatos():
	'''
    Funcion que permite el ingreso de dos números 

    Parametros:
    ------------
        No tiene parámetros

    Retorna:
    ------------
        num_1,num_2: float
    '''
	while True:
		try:
	        # solicitamos al usuario que ingrese el primer numero
			num_1 = float(input("Ingrese el primer número: "))
	        # solicitamos al usuario que ingrese el segundo numero
			num_2 = float(input("Ingrese el segundo número: "))
	       	#salimos del ciclo si los datos son correctos
			break
		#Manejamos el ciclo
		except ValueError:
	        # si la conversión falla, mostramos un mensaje de error
			print("El valor ingresado no es un número. Por favor, ingrese un valor válido.")
	#retornamos el valor del primero y segundo número
	return num_1,num_2


def operacionesAritmeticas(num_1,num_2):
	'''
    Funcion que permite realizar todas las operaciones aritméticas con los dos números ingresados como suma, resta, multiplicación, división

    Parametros:
    ------------
        num_1,num_2: float

    Retorna:
    ------------
        suma,resta,multiplicacion,division: float
    '''
	#Se realiza la suma de dos números y solo con tres decimales
	suma = round(num_1 + num_2,3)
	#Se realiza la resta de dos números y solo con tres decimales
	resta = round(num_1 - num_2,3)
	#Se realiza la multiplicacion de dos números y solo con tres decimales
	multiplicacion = round(num_1 * num_2,3)
	#Sentencia try - except que controla la división para cero
	try:
		#Se realiza la división de dos números y solo con tres decimales
		division = round(num_1 / num_2,3)
	#Manejamos el error de división para cero
	except ZeroDivisionError:
		#Asignamos el valor de Indefinido a la división
		division = "Indefinido"
	#retornamos todas las operaciones
	return suma,resta,multiplicacion,division
	
if __name__ == "__main__":
	#Se guarda el valor del primer y segundo número que ingrese el usuario
	num_1,num_2=ingresoDatos()
	#Se guarda el valor de la suma,resta,multiplicacion,division que retorna de la función 
	suma,resta,multiplicacion,division=operacionesAritmeticas(num_1,num_2)
	#imprimimos el resultado de la suma
	print(f"Suma: {suma}")
	#imprimimos el resultado de la resta
	print(f"Resta: {resta}")
	#imprimimos el resultado de la multipliación
	print(f"Multiplicación: {multiplicacion}")
	#imprimimos el resultado de la división
	print(f"División: {division}")
	#volvemos al menú principal
	os.system("python ejercicios_v1/main.py")
	
	