# Crear una función que le solicite al usuario el ingreso de una cadena y la retorne. Escribir una función que calcule el área de un rectángulo. La función recibe la base y la altura y retorna el área. 

#
texto_usuario = input("Ingrese su nombre: ")

def funcion_devolver_dato( texto_ingresado: str ) -> str:
    """ 
    Retorna un valor y muestra un print sobre el mismo 

    Args:
        texto_ingresado: Primer y único string ingresado

    Returns:
        Regresa un string nuevo, incluyendo el que ingresó el usuario
    """
    nuevo_texto = f"Hola {texto_ingresado}! Bienvenido!"
    return nuevo_texto

funcion_devolver_dato(texto_usuario)
print(funcion_devolver_dato(texto_usuario))