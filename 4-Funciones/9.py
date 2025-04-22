from Funciones import validador_int
# Diseña una función que calcule la potencia de un número. La función debe recibir la base y el exponente como argumentos y devolver el resultado.

base_usuario = None
primer_texto_visible = "Seleccione la Base: "
exponente_usuario = None
segundo_texto_visible = "Seleccione la Exponente: "

base = validador_int(base_usuario, primer_texto_visible)
exponente = validador_int(exponente_usuario, segundo_texto_visible)


def calculo_potencia( radio: int, exponente: int ) -> int:
    """ 
    Recibe por parámetro EL Radio y exponente para calcular la potencia
    Args:
        base: Valor tipo int
        exponente: Valor tipo int

    Returns:
        Retorna como resultado la potencia en tipo int
    """
    potencia = radio ** exponente
    print(f"Potencia: {potencia}")
    return potencia

calculo_potencia(base, exponente)