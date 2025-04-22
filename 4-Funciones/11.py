from Funciones import validador_int
# Crear una función que (utilizando el algoritmo del ejercicio de la guia de for), muestre todos los números primos comprendidos entre entre la unidad y un número ingresado como parámetro. La función retorna la cantidad de números primos encontrados. Modularizar todo lo posible.

num_usuario = None
texto_visible = "Seleccione un número: "

numero = validador_int(num_usuario, texto_visible)

def calculo_cantidad_primos( numero: int ) -> int:
    """ 
    Realiza el cálculo para determinar cuantos números primos hay entre 1 y el número ingresado por el usuario
    Args:
        numero: Número ingresado por el usuario como tope de búsqueda. Con valor tipo int

    Returns:
        Retorna un int indicando la cantidad de números primos encontrados.
    """
    contador_primos = 0
    for posible_primo in range(2, numero + 1, 1):
        cantidad_divisores = 0

        for posible_divisor in range(1, posible_primo + 1, 1):
            if posible_primo % posible_divisor == 0:
                cantidad_divisores += 1
            if cantidad_divisores > 2:
                break

        if cantidad_divisores == 2:
            contador_primos += 1
            print(f"El número {posible_primo} es PRIMO!")

    #Mensaje con cantidad de números encontrados
    print(f"La cantidad de números primos encontrados fue de {contador_primos}")
    return contador_primos
    

print(calculo_cantidad_primos(numero))
