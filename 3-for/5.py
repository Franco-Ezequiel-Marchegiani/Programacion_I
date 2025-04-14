# Se ingresan un máximo de 10 números o hasta que el usuario ingrese el número 0. Mostrar la suma y el promedio de todos los números.

suma_data = 0
promedio = 0

for contador in range(10):
    num_usuario = int(input("Ingrese un número: "))
    
    suma_data += num_usuario
    if num_usuario == 0:
        break
    contador += 1

promedio = suma_data / contador
print(f"suma_data: {suma_data}")
print(f"promedio: {promedio}")
print("Fin")