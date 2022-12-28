#ingresar la longitud y el ancho de un rectángulo y encontrar su perímetro
import os

def ingresoDatos():
	'''
    Funcion que permite el ingreso del largo y ancho de un rectángulo

    Parametros:
    ------------
        No tiene parámetros

    Retorna:
    ------------
        largo,ancho: float
    '''
	while True:
		try:
	        # solicitamos al usuario que ingrese el valor del largo del rectángulo
			largo = float(input("Ingrese el largo: "))
	        # solicitamos al usuario que ingrese el valor del ancho del rectángulo
			ancho = float(input("Ingrese el ancho: "))
	       	#Se verifica si el largo y ancho son números positivos
			if largo <=0 or ancho <=0:
				#imprimimos el mensaje al usuario advirtiendo que ingresó un numero negativo
				print("Ingrese solo valores positivos")
			#Caso contrario si el valor de largo y ancho son correctos y positivos
			else:
				#rompemos el ciclo
				break
		#Manejamos el error
		except ValueError:
	        # si la conversión falla, mostramos un mensaje de error
			print("El valor ingresado no es un número. Por favor, ingrese un valor válido.")
	#retornamos el valor del largo y ancho
	return largo,ancho

def perimetro(largo, ancho):
	'''
    Funcion que permite hacer el cálculo del perímetro usando los valores del largo y ancho

    Parametros:
    ------------
        largo,ancho: float

    Retorna:
    ------------
         perimetro: float
    '''
	#hacemos el calculo del perimetro
	perimetro = 2*(largo+ancho)
	#retornamos el valor del perimetro
	return perimetro

if __name__ == "__main__":
	#Se guarda el valor del largo y ancho que ingrese el usuario
	largo,ancho = ingresoDatos()
	#imprimimos el valor del perímetro calculado del rectángulo
	print(f"El perímetro del rectángulo es de: {perimetro(largo,ancho)} [m]")
	#volvemos al menú principal
	os.system("python main.py")