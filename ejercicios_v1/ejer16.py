#Encontrar el diámetro, la circunferencia y el área de un círculo
import math,os

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
			radio = float(input("Ingrese el valor del radio del círculo: "))
			#Se verifica si radio es un número positivo
			if radio <=0:
				#imprimimos el mensaje al usuario advirtiendo que ingresó un numero negativo
				print("Ingrese solo valores positivos")
			#Caso contrario si el valor del radio es correcto y es positivo
			else:
				#rompemos el ciclo
				break
		#Manjeamos el error
		except ValueError:
	        # si la conversión falla, mostramos un mensaje de error
			print("El valor ingresado no es un número. Por favor, ingrese un valor válido.")
	#retornamos el valor del radio
	return radio

def propiedadesCirculo(radio):
	'''
    Funcion que permite hacer el calculo del diametro,circunferencia y area del circulo dado el radio

    Parametros:
    ------------
        radio: float

    Retorna:
    ------------
        diametro,circunferencia,area: float
    '''
	# Calcular el diámetro
	diametro = round(2 * radio,4)
	# Calcular la circunferencia
	circunferencia = round(2 * math.pi * radio,4)
	# Calcular el área
	area = round(math.pi * radio**2,4)
	# Devolver los resultados en un diccionario
	return diametro,circunferencia,area

if __name__ == "__main__":
	#Se guarda el valor del radio que ingrese el usuario
	radio = ingresoDatos()
	#Se guarda el valor del diametro,circunferencia,area que retorna de la función 
	diametro,circunferencia,area = propiedadesCirculo(radio)
	#imprimimos el resultado del diámetro
	print(f"El diámetro es: {diametro}")
	#imprimimos el resultado de la circunferencia
	print(f"El circunferencia es: {circunferencia}")
	#imprimimos el resultado del área
	print(f"El área es: {area}")
	#volvemos al menú principal
	os.system("python main.py")

