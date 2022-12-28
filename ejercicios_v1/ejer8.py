#Ingresar el radio del circulo del usuario y calcule el área
import os

#Variable Pi que guarda el valor de Pi como si fuera una constante
PI=3.1416

def ingresoDatos():
	'''
    Funcion que permite el ingreso del valor del radio de un círculo

    Parametros:
    ------------
        No tiene parámetros

    Retorna:
    ------------
        radio: float
    '''
	while True:
		try:
	        # solicitamos al usuario que ingrese el valor del radio
			radio = float(input("Ingrese el radio del círculo: "))
			#Se verifica si el radio es un número positivo
			if radio <=0:
				#imprimimos el mensaje al usuario advirtiendo que ingresó un numero negativo
				print("Ingrese solo valores negativos")
			#si el valor ingresado es float y positivo
			else:
	        	#rompemos el ciclo
				break
		except ValueError:
	        # si la conversión falla, mostramos un mensaje de error
			print("El valor ingresado no es un número. Por favor, ingrese un valor válido.")
	#retornamos el valor del radio
	return radio

def areaCirculo(radio):
	return PI*(radio**2)

if __name__ == "__main__":
	#Se guarda el valor del radio que ingrese el usuario
	radio=ingresoDatos()
	#imprimimos el resultado del área del círculo
	print(f"El valor del área del círculo es: {areaCirculo(radio)} [m]")
	#volvemos al menú principal
	os.system("python main.py")