#Dadas dos longitudes ingresadas por el usuario que corresponden a los lados de un rectángulo calcular el perímetro y el área del mismo
import os

def ingresoDatos():
	'''
    Funcion que permite el ingreso de los valores del largo y ancho de un rectángulo

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
			if largo <=0 or ancho <= 0:
				#imprimimos el mensaje al usuario advirtiendo que ingresó un numero negativo
				print("Ingrese solo valores positivos")
	        #Caso contrario
			else:
				#Se rompe el ciclo
				break
		#Se maneja el error
		except ValueError:
	        # si la conversión falla, mostramos un mensaje de error
			print("El valor ingresado no es un número. Por favor, ingrese un valor válido.")
	#retornamos el valor de largo y ancho
	return largo,ancho

def area(largo, ancho):
	'''
    Funcion que permite calcular el área de un rectángulo

    Parametros:
    ------------
        largo,ancho: float

    Retorna:
    ------------
        largo*ancho: float
    '''
	#retornamos el valor del area
	return largo*ancho

def perimetro(largo, ancho):
	'''
    Funcion que permite calcular el perímetro de un rectángulo

    Parametros:
    ------------
        largo,ancho: float

    Retorna:
    ------------
        2*(largo+ancho): float
    '''
	#retornamos el valor del perimetro
	return 2*(largo+ancho)

if __name__ == "__main__":
	#Se guarda el valor del largo y ancho que ingrese el usuario
	largo,ancho = ingresoDatos()
	#Se guarda el valor del perimetro que retorne de la función perimetro
	perimetro=perimetro(largo,ancho)
	#Se guarda el valor del área que retorne de la función area
	area=area(largo,ancho)
	#imprimimos el resultado del perimetro del rectángulo
	print(f"El perimetro del rectángulo es de: {perimetro} [m]")
	#imprimimos el resultado del area del rectángulo
	print(f"El área el rectángulo es de: {area} [m]")
	#volvemos al menú principal
	os.system("python ejercicios_v1/main.py")
	