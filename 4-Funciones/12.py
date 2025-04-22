# Crear una función que imprima la tabla de multiplicar de un número recibido como parámetro. La función debe aceptar parámetros opcionales (inicio y fin) para definir el rango de multiplicación. Por defecto es del 1 al 10.

from Funciones import validador_int, validador_int_none

# Escribir una función que calcule el área de un rectángulo. La función recibe la base y la altura y retorna el área. 
# (Área= base X altura )

#Declaramos variable vacía

numero_usuario = None
primer_texto_visible = "Seleccione un número: "
inicio_usuario = ""
segundo_texto_visible = "Seleccione un Inicio: "
fin_usuario = None
tercer_texto_visible = "Seleccione un Fin: "


base = validador_int(numero_usuario, primer_texto_visible)
inicio = validador_int_none(inicio_usuario, segundo_texto_visible)
fin = validador_int_none(fin_usuario, tercer_texto_visible)


def tabla_multiplicar( base: int, inicio: int | str, fin: int | str ) -> bool:
    """ 
    Recibe por parámetro la base y altura, y calcula el área en base a eso.     

    Args:
        base: Valor tipo int para evaluar valor a multiplicar
        inicio: Valor tipo int o None para indicar el inicio para mostrar, si es None es 0
        fin: Valor tipo int o None para indicar el fin para mostrar, si es None es 10

    Returns:
        Muestra en pantalla el rango de tablas de multiplicar 
        según el número brindado por el parámetro base. Devuelve un true de default
    """
    #El primer parámetro es el inicio, 
    # El segundo el límite, arranca de 0 al número, así que se le suma 1
    # El 3ro cada cuanto va iterando
    if inicio == "":
        inicio = 1
    if fin == "":
        fin = 10
    print(f"Tabla del {base}")
    for index in range(inicio, fin + 1, 1):
        print(f"{index} x {base} : {(index * base)}")
    
    return True

tabla_multiplicar(base, inicio, fin)