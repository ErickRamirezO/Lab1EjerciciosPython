#Ingresar un valor en libras y tranformalo a kilos y gramos
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
	        # solicitamos al usuario que ingrese un valor en libras
			libras = float(input("Ingrese un valor en libras: "))
	        #Se verifica si libras es un número positivo
			if libras <=0.0:
				#imprimimos el mensaje al usuario advirtiendo que ingresó un numero negativo
				print("Ingrese solo valores positivos")
			#si el valor ingresado es float y positivo
			else:
				#Se rompe el ciclo
				break
			#Se maneja el error
		except ValueError:
	        # si la conversión falla, mostramos un mensaje de error
			print("El valor ingresado no es un número. Por favor, ingrese un valor válido.")
	#retornamos el valor de las libras
	return libras

def conversionLibrasAKilos(libras):
	'''
    Funcion que hace la conversión de libras a kilos

    Parametros:
    ------------
        libras : float

    Retorna:
    ------------
        No retorna ningún valor
    '''
	#Hacemos el calculo de la conversión de libras a kilos con tres decimales
	kilos = round(libras/2.2046,3)
	#imprimimos la conversión
	print(f"{libras} libras a kilos es: {kilos}")

def conversionLibrasAGramos(libras):
	'''
    Funcion que transforma libras a gramos

    Parametros:
    ------------
        libras : float

    Retorna:
    ------------
        No retorna ningún valor
    '''
	#Hacemos el calculo de la conversión de libras a gramos con tres decimales 
	gramos = round(libras*453.6,3)
	#imprimimos la conversión
	print(f"{libras} libras a gramos es: {gramos}")
	
if __name__ == "__main__":
	#Se guarda el valor de libras que ingrese el usuario
	valor_libras = ingresoDatos()
	#Se llama a la función que hace la conversión de libras a kilos
	conversionLibrasAKilos(valor_libras)
	#Se llama a la función que hace la conversión de libras a gramos
	conversionLibrasAGramos(valor_libras)
	#volvemos al menú principal
	os.system("python main.py")