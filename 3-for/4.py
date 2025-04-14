#Ingresar un número y mostrar la tabla de multiplicar de ese número. Por ejemplo si se ingresa el numero 5:
#	5 x 0 = 0
#	5 x 1  = 5
#	5 x 2 = 10
#	5 x 3  = 15 …

num_usuario = int(input("Ingrese un número: "))

for contador in range(10):
    contador += 1
    calculo = contador * num_usuario
    print(f"{num_usuario} x {contador} = {calculo}")

print("Fin")