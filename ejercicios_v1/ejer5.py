#calcular la siguiente expresion y=x^z/2
import os

def ingresoDatos():
	'''
    Funcion que permite ingresar el valor de x y de z

    Parametros:
    ------------
        No tiene parámetros

    Retorna:
    ------------
        x,z: float
    '''
	#solicitamos al usuario ingresar el valor de x
	x = float(input("Ingrese el valor de x: "))
	#solicitamos al usuario ingresar el valor del grado de x en este caso z
	z = float(input("Ingrese el valor del grado de x: "))
	#retornamos el valor de x,z
	return x,z
	
def calculoExpresion(x,z):
	'''
    Funcion que permite calcular la expresión y=x^z/2

    Parametros:
    ------------
        x,z: float

    Retorna:
    ------------
        y: float
    '''
	#Se hace el calculo de la expresión y se lo guarda en la variable y
	y=(x**z)/2
	#Retornamos el valor de y
	return y

if __name__ == "__main__":
	#Se guarda el valor de las variables x,z que ingrese el usuario
	x,z = ingresoDatos()
	#Imprimimos el resultado del calculo de la expresión
	print(f"El resultado de y=x^z/2 es: y={calculoExpresion(x,z)}")
	#volvemos al menú principal
	os.system("python main.py")