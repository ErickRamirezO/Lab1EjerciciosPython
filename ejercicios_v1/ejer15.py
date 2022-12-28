#Resuelva la siguiente ecuacion
import os

def ingresoDatos():
	'''
    Funcion que permite el ingreso del valor de k

    Parametros:
    ------------
        No tiene parámetros

    Retorna:
    ------------
        k: float
    '''
	while True:
		try:
	        # solicitamos al usuario que ingrese el valor de k
			k = float(input("Ingrese el valor de k: "))
	        #Se rompe el ciclo
			break
		#Se maneja el error
		except ValueError:
	        # si la conversión falla, mostramos un mensaje de error
			print("El valor ingresado no es un número. Por favor, ingrese un valor válido.")
	#retornamos el valor de k
	return k

def resolverEcuacion(k):
	'''
    Funcion que permite hacer el calculo para la ecuación planteada
	((-1)k+1)/(1*k-1)((-1)^{k+1})/(2*k-1)

    Parametros:
    ------------
        k : float

    Retorna:
    ------------
        resultado: float
    '''
	#Se hace todo el calculo de la expresión planteada
	resultado = ((-1)*k+1)/(2*k-1)((-1)^(k+1))/(2*k-1)
	#retornamos resulatado que contiene el calculo de la expresión
	return resultado

if __name__ == "__main__":
	#Se guarda el valor de k que ingrese el usuario
	k = ingresoDatos()
	#imprimimos el resultado de la ecuación
	print(f"El resultado de la ecuacion es: {resolverEcuacion(k)}")
	#volvemos al menú principal
	os.system("python main.py")