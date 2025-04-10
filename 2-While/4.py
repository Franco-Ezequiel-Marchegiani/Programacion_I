#Mostrar la suma de los números pares desde el 1 hasta el 10.
contador = 0

while contador < 10:
    contador = contador + 1
    if contador % 2 == 0:
        print(f"Contando de a pares... {contador}")

print(f"Contador: {contador}")