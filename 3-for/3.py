# Ingresar un número. Mostrar los números desde 0 hasta el número ingresado.

num_usuario = int(input("Ingrese un número de tope: "))
contador = 0
for contador in range(num_usuario):
    contador += 1
    print(contador)

print("Fin")