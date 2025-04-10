# Solicitar al usuario que ingrese números (hasta que no quiera ingresar más). 
# Calcular la suma de los números ingresados y el promedio de los mismos.

contador = 0
suma_numeros = 0

while True:

    ingresar_numeros = float(input("Ingrese un número: "))
    
    if ingresar_numeros > 0:
        contador += 1
        suma_numeros += ingresar_numeros

    pregunta = input("Quiere ingresar otro número? s/n ")
    if pregunta == "n":
        break

#Calculando el promedio
promedio = suma_numeros / contador

print(f"Cantidad de números ingresados: \n {contador}")
print(f"Promedio de los números ingresados: \n {promedio}")