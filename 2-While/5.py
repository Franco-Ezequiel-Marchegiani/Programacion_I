#5- Solicitar el ingreso de 5 números, calcular la suma de los números ingresados y el promedio. Mostrar la suma y el promedio por pantalla.

totalNumeros = 5
contadorNumero = 0
ingresoNumero = 0
while contadorNumero < 5:
    
    ingresoNumero += float(input("Ingrese un número: "))
    contadorNumero += 1

prom = ingresoNumero / contadorNumero
print(f"Suma tota: {ingresoNumero}")
print(f"Promedio: {prom}")
print(f"Contador Número: {contadorNumero}")
