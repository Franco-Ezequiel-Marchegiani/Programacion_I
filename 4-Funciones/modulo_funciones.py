
def validador_juego( param_user: str, texto_visible: str) -> int | str:
    """ 
        Recibe una variable vacía, valida que lo que ingrese el usuario
        sea un string numérico positivo entre 1 y 3, utilizando "isdigit()" para ello.
        También muestra el mensaje que recibe por parámetros

    Args:
        param_user: Variable vacía para rellenar con lo que el usuario ingrese
        texto_visible: Texto que le indicará al usuario qué ingresar

    Returns:
        Devuelve una variable type int con el dato que el usuario haya seleccionado
        Ya validado que sea un número
    """
    
    #Validamos que sí o sí sea un número con isdigit(), en formato str
    while param_user == None or not param_user.isdigit():
        param_user = input(f"{texto_visible}")
        #Validamos que se cumpla isDigit
        if param_user.isdigit() == False:
            pass
        #Verificamos que solo acepte valores del 1 al 3
        elif (1 <=  int(param_user) <= 3):
            pass
        else:
            param_user = None
    
    return int(param_user)

def verificar_ganador_ronda(jugador: int, maquina: int) -> str:
    """ 
    Determina quién ganó la ronda según las elecciones del jugador y la máquina.
    Parámetros:
        jugador (int): Elección del jugador (1 para Piedra, 2 para Papel, 3 para Tijera).
        maquina (int): Elección de la máquina (1 para Piedra, 2 para Papel, 3 para Tijera).

    Retorno:
    "Jugador" → Si el jugador gana la ronda.
    "Máquina" → Si la máquina gana la ronda.
    "Empate" → Si ambos eligen el mismo elemento. 
    """
    txt_jugador = "Jugador"
    txt_maquina = "Máquina"
    txt_empate = "Empate"
    #Buscarle la vuelta para optimizar esto urgentemente
    #Case user pick Piedra
    
    if jugador == maquina:
        return txt_empate
    #Caso que el usuario elija Piedra
    elif jugador == 1 and maquina == 2:
        return txt_maquina
    elif jugador == 1 and maquina == 3:
        return txt_jugador
    #Caso que el usuario elija Papel
    elif jugador == 2 and maquina == 1:
        return txt_jugador
    elif jugador == 2 and maquina == 3:
        return txt_maquina
    #Caso que el usuario elija Tijera
    elif jugador == 3 and maquina == 1:
        return txt_maquina
    elif jugador == 3 and maquina == 2:
        return txt_jugador
    
    #Como comentario, averigué que para optimizar más aún, se puede usar módulo (%) en 3, quedando:
    """ 
    if jugador == maquina:
        return "Empate"
    elif (jugador - maquina) % 3 == 1:
        return "Jugador"
    else:
        return "Máquina"
    """
    # Pero tuve que buscar en internet al respecto y no me pareció justo colocarlo,
    # lo optimicé lo más que pude Con los conocimientos que adquirí hasta el momento :) 


def verificar_estado_partida(aciertos_jugador: int, aciertos_maquina: int, ronda_actual: int) -> bool:
    """ 
    Determina si la partida sigue en curso o ya ha finalizado. 
    Parámetros:
        aciertos_jugador (int): Cantidad de rondas ganadas por el jugador.
        aciertos_maquina (int): Cantidad de rondas ganadas por la máquina.
        ronda_actual (int): Número de la ronda actual.

    Retorno:
    True → Si la partida sigue en curso.
    False → Si la partida ha finalizado (porque alguien ganó dos veces seguidas o se jugaron todas las rondas).
    """
    #Si ya se superó la tercera ronda, 
    if aciertos_jugador == 2 or aciertos_maquina == 2:
        return False
    else:
        return True


def verificar_ganador_partida(aciertos_jugador: int, aciertos_maquina: int) -> str:
    """ 
    Objetivo: Determina quién ganó la partida comparando los aciertos finales.

    Parámetros:
    aciertos_jugador (int): Cantidad de rondas ganadas por el jugador.
    aciertos_maquina (int): Cantidad de rondas ganadas por la máquina.

    Retorno:
    "Jugador" → Si el jugador tiene más aciertos.
    "Máquina" → Si la máquina tiene más aciertos. """
    if aciertos_jugador > aciertos_maquina:
        return "El Jugador"
    else:
        return "La Máquina"


def mostrar_elemento(eleccion: int) -> str:
    """ 
    Objetivo: Convierte la elección numérica en un texto legible.

    Parámetros:
    eleccion (int): Número de elección (1 para Piedra, 2 para Papel, 3 para Tijera).

    Retorno:
    "Piedra" cuando su elección == 1.
    "Papel" cuando su elección == 2.
    "Tijera" cuando su  elección == 3. """
    match eleccion:
        case 1:
            return "Piedra"
        case 2:
            return "Papel"
        case 3:
            return "Tijera"


