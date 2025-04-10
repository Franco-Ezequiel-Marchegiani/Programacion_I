# Solicitar al usuario que ingrese 5 números como mínimo y como máximo 10. 
# Calcular la suma de los números ingresados y el promedio de los mismos.


numero_totales = 10
contador = 0
suma_numeros = 0

while contador < numero_totales:
    numero_usuario = float(input("Ingrese un número: "))
    suma_numeros += numero_usuario

    contador += 1

    if contador >= 5:
        pregunta = input("Desea continuar ingresando números? s/n ")
        if pregunta == "n":
            break


promedio = suma_numeros / contador

print(f"suma_numeros: {suma_numeros}")
print(f"Promedio: {promedio}")