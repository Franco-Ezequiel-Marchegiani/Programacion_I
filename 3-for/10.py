# Ingresar un número. Determinar si el número es primo o no.

num_usuario = int(input("Ingrese un número para analizar: "))

es_primo = False
for contador in range(num_usuario):    
    contador += 1
    if (contador != 1 ) and (contador != num_usuario):
        if num_usuario % contador == 0:
            print("NO es primo")
            es_primo = False
            break
    else:
        es_primo = True
if es_primo:
    print("Es primo!")

print(f"Valor Variable: {es_primo}")