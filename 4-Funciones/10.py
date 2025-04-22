from Funciones import validador_int
# Crear una función que reciba un número y retorne True si el número es primo, False en caso contrario.


num_usuario = None
texto_visible = "Seleccione un número: "

numero = validador_int(num_usuario, texto_visible)

def detector_num_primos( numero: int ) -> bool:
    """ 
    Realiza el cálculo para determinar si el número ingresado es primo o no. 
    Recorriendo número por número hasta obtener la información necesaria para determinar.
    Args:
        numero: Número ingresado por el usuario con valor tipo int

    Returns:
        Retorna un bool indicando True si es Primo o False si no.
    """

    cantidad_divisores = 0
    for contador in range(1, numero + 1, 1):
        if numero % contador == 0:
            cantidad_divisores += 1
        print(f"cantidad_divisores: {cantidad_divisores}")
        #Rompemos el bucle si ya hay más de 2 divisores:
        if cantidad_divisores > 2:
            break

    #Analizamos la salida en base a la búsqueda realizada
    if cantidad_divisores == 2:
        print(f"El número {numero} es primo!")
        return True
    else:
        print(f"El número {numero} NO es primo!")
        return False

print(detector_num_primos(numero))