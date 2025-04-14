# Ingresar un número. Mostrar todos los divisores que hay desde el 1 hasta el número ingresado. Mostrar la cantidad de divisores encontrados.

num_usuario = int(input("Ingrese un número de tope: "))

for contador in range(num_usuario):    
    contador += 1
    if num_usuario % contador == 0:
        print(f"Divisores: {contador}") 