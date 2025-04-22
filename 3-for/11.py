# Ingresar un número. Mostrar cada número primo que hay entre el 1 y el número ingresado. Informar cuántos números primos se encontraron.
num_usuario = None
while num_usuario == None or not num_usuario.isdigit():
    num_usuario = input("Ingrese un número para analizar: ")

num_usuario_int = int(num_usuario)

for posible_primo in range(2, num_usuario_int + 1, 1):
    cantidad_divisores = 0

    for posible_divisor in range(1, posible_primo + 1, 1):
        if posible_primo % posible_divisor == 0:
            cantidad_divisores += 1

    if cantidad_divisores == 2:
        print(f"El número {posible_primo} es PRIMO!")

print(f"Cantidad de números divisores: {cantidad_divisores}")

