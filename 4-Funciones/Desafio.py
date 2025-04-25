import random
from modulo_funciones import *
eleccion = None
texto_visible = 'Seleccione entre Piedra (1) Papel (2) o Tijera (3): '

def mostrar_ganador(aciertos_jugador: int, aciertos_maquina: int):
    print(f"Y tenemos un ganador! Nuestro personal se está encargando de contar los puntos...")
    ganador = verificar_ganador_partida(aciertos_jugador, aciertos_maquina)
    print(f"Y el ganador del torneo de Piedra, Papel o Tijera es... \n{ganador}!! ")
    if ganador == "La Máquina":
        param_user = input(f"\nTe gustaría volver a intentarlo? y/n ")
        if param_user == "y" or param_user == "Y":
            print("Vamos entonces por una revancha! \n")
            print("------------------------------------------------------\n")
            jugar_piedra_papel_tijera()
        else:
            print(f"Nos vemos en una próxima edicción!")


def jugar_piedra_papel_tijera() -> str:
    """ 
    📌 Objetivo: Gestiona toda la lógica del juego, usando las funciones anteriores.

    🔹 Flujo de la función:
    Inicia una partida donde el jugador compite contra la máquina.
    En cada ronda, el jugador elige una opción y la máquina genera una elección aleatoria.
    Se determina el ganador de la ronda.
    Se verifica si la partida continúa o si alguien ha ganado.
    Al finalizar, la función devuelve quién ganó la partida ("Jugador" o "Máquina"). 
    
    Retorno:
    Mensaje indicando quién es el ganador
    """
    print("Bienvenidos al torneo de Piedra, Papel o Tijera!!\n")
    print("Edición: Jugador vs Máquina, crees que puedes ganarle a tu computadora? \nQue comience la partida!")
    print(f"\n------------------------------------------------------\n")
    puntaje_usuario = 0
    puntaje_maquina = 0
    numero_ronda = 0
    while True:
        numero_ronda = numero_ronda + 1
        
        print(f"Ronda N° {numero_ronda}")
        #El usuario selecciona entre 1 y 3
        eleccion_usuario = int(validador_juego(eleccion, texto_visible))
        #La máquina selecciona entre 1 y 3
        eleccion_maquina = random.randint(1,3)

        print(f"\nEl usuario juega: {mostrar_elemento(eleccion_usuario)}")
        print(f"Y la máquina responde con: {mostrar_elemento(eleccion_maquina)}")

        resultado_ronda = verificar_ganador_ronda(eleccion_usuario, eleccion_maquina)
        if resultado_ronda == "Empate":
            print(f"\nDamas y caballeros En esta ronda N°{numero_ronda} tenemos un empate!")
            print("Veamos cómo sigue!")
        else:
            print(f"\nEl ganador de la Ronda N°{numero_ronda} es {resultado_ronda}!")

        if resultado_ronda == "Jugador":
            puntaje_usuario = puntaje_usuario + 1
        elif resultado_ronda == "Máquina":
            puntaje_maquina = puntaje_maquina + 1

        print(f"Quedando el marcador en:")
        print(f"Humano: {puntaje_usuario}")
        print(f"Máquina: {puntaje_maquina}\n")
        
        #Luego de verificar el ganador, se verifica el estado de la partida con booleano. Si es false hacer un break del for
        estado_partida = verificar_estado_partida(aciertos_jugador = puntaje_usuario, aciertos_maquina = puntaje_maquina, ronda_actual = numero_ronda )
        if estado_partida == False:
            break
        else:
            print("No se vayan a ninguna parte, que esto aún no termina!\n")
    #Llamamos a la función para calcular, y anunciar al ganador
    mostrar_ganador(aciertos_jugador = puntaje_usuario, aciertos_maquina = puntaje_maquina)
    
jugar_piedra_papel_tijera()