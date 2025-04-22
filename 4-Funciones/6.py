# Crea una función que verifique si un número dado es par o impar. La función debe imprimir un mensaje indicando si el número es par o impar.

num_usuario = None
while num_usuario == None or not num_usuario.isdigit():
    num_usuario = input("Ingrese un número: ")

num_usuario_int = int(num_usuario)

def calculo_par_impar( num_ingresado: int ):
    """ 
    Analiza el int del parámetro y calcula si es par o impar 
    """
    if num_ingresado % 2 == 0:
        print(f"Número {num_ingresado} es par")
    else:
        print(f"Número {num_ingresado} es impar")    

calculo_par_impar(num_usuario_int)