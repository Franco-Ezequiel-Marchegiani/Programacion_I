import math
from Funciones import validador_int
# Escribe una función que calcule el área de un círculo. La función debe recibir el radio como parámetro y devolver el área.

radio_usuario = None
texto_visible = "Ingrese el Radio: "

radio = validador_int(radio_usuario, texto_visible)


def area_circulo( radio: int ) -> int:
    """ 
    Recibe por parámetro EL RADIO, y calcula el área del círculo en base a eso.     

    Args:
        base: Valor tipo int
        altura: Valor tipo int

    Returns:
        Retorna como resultado el área en tipo int
    """
    area = math.pi * (radio * radio) #Es elevado al cuadrado, también puede ser " radio**2 "
    print(f"Area total calculada: {area}")
    return area

area_circulo(radio)