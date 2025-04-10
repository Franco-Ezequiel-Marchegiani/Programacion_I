# 7- Solicitar al usuario que ingrese números (hasta que no quiera ingresar más). Calcular la suma de los números positivos y el producto de los negativos.


positivos = 0
negativo = 1

while True:

    ingresar_numeros = float(input("Ingrese un número: "))
    
    if ingresar_numeros > 0:
        positivos += ingresar_numeros
    elif ingresar_numeros < 0:
        negativo *= ingresar_numeros

    pregunta = input("Quiere ingresar otro número? s/n ")
    if pregunta == "n":
        break


print(f"Los números positivos ingresados, a excepción del 0, son: \n {positivos}")
print(f"El Producto de los números negativos ingresados, a excepción del 0, son: \n {negativo}")