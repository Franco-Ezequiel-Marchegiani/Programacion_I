# Crea una función que verifique si un número dado es par o impar. La función retorna True si el número es par, False en caso contrario

num_usuario = None
while num_usuario == None or not num_usuario.isdigit():
    num_usuario = input("Ingrese un número: ")

num_usuario_int = int(num_usuario)

def calculo_par_impar( num_ingresado: int ):
    """ 
    Analiza el int del parámetro y calcula si es par o impar.

    Params:
        num_ingresado: Número tipo int
    
    Retorna "True" si es par
    O "False" si es impar
    """
    if num_ingresado % 2 == 0:
        return True
    else:
        return False

llamada_funcion = calculo_par_impar(num_usuario_int)
print(f"Respuesta del return de la función: {llamada_funcion}")