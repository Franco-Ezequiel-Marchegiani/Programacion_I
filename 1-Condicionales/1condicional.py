""" 
A partir del ingreso de la altura en centímetros de un jugador de baloncesto, 
el programa deberá determinar la posición del jugador en la cancha, considerando los siguientes parámetros:
Menos de 160 cm: Base
Entre 160 cm y 179 cm: Escolta
Entre 180 cm y 199 cm: Alero
200 cm o más: Ala-Pívot o Pívot

"""

altura_jugador = float(input("Ingrese el número en cm del jugador (ej. 180): "))
posicion = ''

if altura_jugador < 160:
    posicion = 'Base'
elif altura_jugador >= 160 and altura_jugador < 180:
    posicion = 'Escolta'
elif altura_jugador >= 180 and altura_jugador < 200:
    posicion = 'Alero'
else:
    posicion = 'Ala-Pívot o Pívot'


print(f"La altura del jugador ingresada por el usuario fue de: {altura_jugador}cm")
print(f"La posición asignada es: {posicion}")