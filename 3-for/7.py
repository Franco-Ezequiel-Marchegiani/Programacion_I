#Mostrar los números pares que hay desde la unidad hasta el número 50.
print("Listado números pares: ")
for contador in range(50):
    if contador % 2 == 0:
        print(f"{contador}")