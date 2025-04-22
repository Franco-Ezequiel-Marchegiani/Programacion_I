# Ingresar un número. Determinar si el número es primo o no.
num_usuario = None
while num_usuario == None or not num_usuario.isdigit():
    num_usuario = input("Ingrese un número para analizar: ")

num_usuario_int = int(num_usuario)


""" es_primo = False
for contador in range(1, num_usuario_int + 1, 1):    
    if (contador != 1 ) and (contador != num_usuario_int):
        if num_usuario_int % contador == 0:
            print("NO es primo")
            es_primo = False
            break
    else:
        es_primo = True
if es_primo:
    print("Es primo!")

print(f"Valor Variable: {es_primo}") """

cantidad_divisores = 0
for contador in range(1, num_usuario_int + 1, 1):
    if num_usuario_int % contador == 0:
        cantidad_divisores += 1
        
print(f"cantidad_divisores: {cantidad_divisores}")

if cantidad_divisores == 2:
    print(f"El número {num_usuario_int} es primo!")
else:
    print(f"El número {num_usuario_int} NO es primo!")