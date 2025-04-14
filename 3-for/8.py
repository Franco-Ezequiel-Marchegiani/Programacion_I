# Realizar un programa que permita mostrar una pirámide de números. Por ejemplo: si se ingresa el numero 5, la salida del programa será la siguiente:
#1
#12
#123
#1234
#12345

num_usuario = int(input("Ingrese un número de tope: "))
contador = 0
data = ''
for contador in range(num_usuario):
    contador += 1
    data = str('')
    for i in range(contador):
        i += 1
        data = data + str(i)
    print(data)
        
print("Fin")