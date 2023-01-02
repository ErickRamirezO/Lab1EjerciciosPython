#Ingresar un valor en dólares y transformarlo en euros y yen
import os

def ingresoDatos():
	'''
    Funcion que permite el ingreso del valor de las libras

    Parametros:
    ------------
        No tiene parámetros

    Retorna:
    ------------
        libras: float
    '''
	while True:
		try:
	        # solicitamos al usuario que ingrese un valor en dólares
			dolares = float(input("Ingrese un valor en dólares: "))
			#validamos que el valor de libras no sea un número negativo
			if dolares<=0:
				#imprimimos el mensaje al usuario advirtiendo que ingresó un numero negativo
				print("Ingrese solo valores positivos")
			#si el valor ingresado es float y positivo
			else:
				#se rompe el ciclo
				break
		#Se maneja el error
		except ValueError:
	        # si la conversión falla, mostramos un mensaje de error
			print("El valor ingresado no es un número. Por favor, ingrese un valor válido.")
	#retornamos el valor de dólares
	return dolares

def dolaresAEuros(dolares):
	'''
    Funcion que hace la conversión de dólares a Euros

    Parametros:
    ------------
        dolares : float

    Retorna:
    ------------
        euros: float
    '''
	#variable que contiene la tasa de cambio actual (2022-12-27) del euro
	tasaCambioActualEuro = 0.94
	#variable que contiene la conversión de dólares a euros
	euros = dolares * tasaCambioActualEuro
	#retorna el valor en euros solo con 2 decimales
	return round(euros,2)

def dolaresAYen(dolares):
	'''
    Funcion que hace la conversión de dólares a Yenes

    Parametros:
    ------------
        dolares : float

    Retorna:
    ------------
        yenes: float
    '''
	#variable que contiene la tasa de cambio actual (2022-12-27) del yen
	tasaCambioActualYen = 133.40
	#variable que contiene la conversión de dólares a yenes
	yenes = dolares * tasaCambioActualYen
	#retorna el valor en yenes solo con 2 decimales
	return round(yenes,2)

if __name__ == "__main__":
	#Se guarda el valor de dólares que ingrese el usuario
	dolares = ingresoDatos()
	#Se guarda el valor de euros que retorna de la función 
	euros = dolaresAEuros(dolares)
	#Se guarda el valor de yenes que retorna de la función
	yenes = dolaresAYen(dolares)
	#imprimos el resultado de la conversion de dolares a euros
	print(f"{dolares} dólares a Euros son: {euros}")
	#imprimos el resultado de la conversion de dolares a yenes
	print(f"{dolares} dólares a Yenes son: {yenes}")
	#volvemos al menú principal
	os.system("python ejercicios_v1/main.py")