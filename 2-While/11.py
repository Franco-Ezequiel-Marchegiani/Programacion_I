# Realizar un programa que permita que el usuario ingrese todos los números que desee. Una vez finalizada la carga determinar:

# La suma acumulada de los números negativos. - OK
# La suma acumulada de los números positivos. - OK
# La cantidad de números negativos ingresados. - OK
# El promedio de los números positivos. - OK
# El número positivo más grande. - OK
# El porcentaje de números negativos ingresados, respecto del total de ingresos.

contador_global = 0
max_numero = 0
cantidad_positivos = 0
cantidad_negativos = 0
suma_positivos = 0
suma_negativos = 0

while True:

    ingresar_numeros = float(input("Ingrese un número: "))
    
    if ingresar_numeros > 0:
        cantidad_positivos += 1
        suma_positivos += ingresar_numeros
        if ingresar_numeros >= max_numero:
            max_numero = ingresar_numeros

    elif ingresar_numeros < 0:
        cantidad_negativos += 1
        suma_negativos -= ingresar_numeros

    contador_global += 1
    pregunta = input("Quiere ingresar otro número? s/n ")
    if pregunta == "n":
        break

promedio_positivos = suma_positivos / cantidad_positivos
porcentaje_negativos = (cantidad_negativos * 100) / contador_global

print("\n Rejunte de información: \n")
print("------------------------------------------------------ \n")
print(f"La suma acumulada de los números negativos es de: {suma_negativos}")
print(f"La suma acumulada de los números positivos es de: {suma_positivos}")
print(f"La cantidad de números negativos ingresados son de: {cantidad_negativos}")
print(f"El promedio de los números positivos es de: {promedio_positivos}")
print(f"El número positivo más grande es el: {max_numero}")
print(f"El porcentaje de números negativos ingresados, respecto del total de ingresos: {porcentaje_negativos} \n")
print("------------------------------------------------------")