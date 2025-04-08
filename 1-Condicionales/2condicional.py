""" 
Calcular una nota aleatoria entre el 1 y el 10 inclusive, para luego mostrar un mensaje según el valor:
6, 7, 8, 9 y 10  ---> Promoción directa, la nota es ...
4 y 5            ---> Aprobado, la nota es ...
1, 2 y 3         ---> Desaprobado, la nota es ...
"""

nota = float(input("Ingrese la nota correspondiente: "))
estado = ''

#Condicional para que la nota sea entre 1 y 10
if nota <= 0 or nota >= 11:
    print("Por favor, ingrese una nota entre 1 y 10")
else:
    #Lógica condicional
    if nota >= 1 and nota <= 3:
        estado = 'Desaprobado'
    elif nota == 4 or nota == 5:
        estado = 'Aprobado'
    elif nota >= 6 and nota <= 10:
        estado = 'Promoción directa'
    else:
        estado = ''

    print(f"{estado}, la nota es {nota}")
