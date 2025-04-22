from Funciones import validador_int
# Crear una función que le solicite al usuario el ingreso de un número flotante y lo retorne.

#Declaramos variable vacía
num_usuario = None
primer_texto_visible = "Ingrese un número de tope"

num_usuario_int = validador_int(num_usuario, primer_texto_visible)

def funcion_devolver_dato( num_ingresado: int ) -> int:
    """ 
    Retorna un valor y muestra un print sobre el mismo 

    Args:
        num_ingresado: Primer y único número ingresado

    Returns:
        El mismo número ingresado
    """
    print(f"Número ingresado tipo int: {num_ingresado}")
    return num_ingresado

funcion_devolver_dato(num_usuario_int)