# 9- Solicitar al usuario que ingrese 5 números. Calcular la suma de los números ingresados y el promedio de los mismos.

numero_totales = 5
contador = 0
suma_numeros = 0

while contador < numero_totales:
    numero_usuario = float(input("Ingrese un número: "))
    suma_numeros += numero_usuario

    contador += 1

promedio = suma_numeros / contador

print(f"suma_numeros: {suma_numeros}")
print(f"Promedio: {promedio}")