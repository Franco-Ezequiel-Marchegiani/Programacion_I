# Ingresar 10 números enteros. Determinar el máximo y el mínimo.

contadorNumero = 0
max_value = 0
min_value = 0

while contadorNumero < 10:
    print(f"max_value: {max_value}")
    print(f"min_value: {min_value}")
    
    ingresoNumero = float(input("Ingrese un número: "))
    contadorNumero += 1
    #Si el número que ingresa el usuario es MAYOR, se guarda su valor
    if ingresoNumero >= max_value:
        max_value = ingresoNumero
    #Si el número que ingresa el usuario es MENOR, se guarda su valor
    #Primero guarda el primer valor mínimo
    if min_value == 0:
        min_value = ingresoNumero
    #Luego guarda el valor si el número ingresado es más pequeño que el primer valor
    if ingresoNumero <= min_value:
        min_value = ingresoNumero



print(f"Valor más alto: {max_value}")
print(f"Valor más bajo: {min_value}")