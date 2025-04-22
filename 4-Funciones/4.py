from Funciones import validador_int

# Escribir una función que calcule el área de un rectángulo. La función recibe la base y la altura y retorna el área. 
# (Área= base X altura )

#Declaramos variable vacía

base_usuario = None
primer_texto_visible = "Seleccione la Base: "
altura_usuario = None
segundo_texto_visible = "Seleccione la Altura: "

base = validador_int(base_usuario, primer_texto_visible)
altura = validador_int(altura_usuario, segundo_texto_visible)


def area_rectangulo( base: int, altura: int ) -> int:
    """ 
    Recibe por parámetro la base y altura, y calcula el área en base a eso.     

    Args:
        base: Valor tipo int
        altura: Valor tipo int

    Returns:
        Retorna como resultado el área en tipo int
    """
    area = base * altura
    print(f"Area total calculada: {area}")
    return area

area_rectangulo(base,altura)