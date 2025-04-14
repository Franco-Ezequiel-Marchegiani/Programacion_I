# Ingresar un número. Mostrar cada número primo que hay entre el 1 y el número ingresado. Informar cuántos números primos se encontraron.

""" 
num_usuario = int(input("Ingrese un número de tope: "))

for contador in range(num_usuario):
    contador += 1
    
    for i in range(contador):
        if (contador != 1 ) and (contador != num_usuario):
            if num_usuario % contador == 0:
                print(f"Pass, {contador} NO es primo")
        else:
            print(f"Valor primo: {contador}")
 """
