#Calcular la formula de la velocidad
import os
def ingresoDatos():
	'''
    Funcion que permite el ingreso de la distancia y el tiempo

    Parametros:
    ------------
        No tiene parámetros

    Retorna:
    ------------
        distancia,tiempo: float
    '''
	while True:
		try:
	        # solicitamos al usuario que ingrese el valor de la distancia
			distancia = float(input("Ingrese el valor de la distancia: "))
	        # solicitamos al usuario que ingrese el valor del tiempo
			tiempo = float(input("Ingrese el valor del tiempo: "))
			#Se verifica que se ingrese un valor positivo para el tiempo
			if tiempo<=0:
				#imprimimos el mensaje al usuario advirtiendo que ingresó un numero negativo para el valor del tiempo
				print("Solo ingrese valores positivos para el tiempo")
	        # Salimos del ciclo si los datos son correctos
			break
		#Manejamos el error
		except ValueError:
	        # si la conversión falla, mostramos un mensaje de error
			print("El valor ingresado no es un número. Por favor, ingrese un valor válido.")
	#retornamos el valor de la distancia y el tiempo
	return distancia,tiempo
	
def calculoVelocidad(distancia,tiempo):
	'''
    Funcion que permite hacer el calculo de la velocidad con los valores de la distancia y el tiempo

    Parametros:
    ------------
        No tiene parámetros

    Retorna:
    ------------
       distancia/tiempo: float
    '''
	#Guardamos el calculo de la velocidad en la variable respectiva
	velocidad = distancia/tiempo
	#retornamos el valor de velocidad
	return velocidad

if __name__ == "__main__":
	#Se guarda el valor de la distancia y tiempo que ingrese el usuario
	distancia,tiempo=ingresoDatos()
	#imprimimos el valor de la velocidad calculada
	print(f"El valor de la velocidad es: {calculoVelocidad(distancia,tiempo)} [m/s]")
	#volvemos al menú principal
	os.system("python ejercicios_v1/main.py")