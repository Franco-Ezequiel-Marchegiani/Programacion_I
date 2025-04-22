# Ingresar un número. Mostrar todos los divisores que hay desde el 1 hasta el número ingresado. Mostrar la cantidad de divisores encontrados.

num_usuario = None
while num_usuario == None or not num_usuario.isdigit():
    num_usuario = input("Ingrese un número de tope: ")

num_usuario_int = int(num_usuario)
#Nota for: 
#El primer parámetro es el inicio, 
# El segundo el límite, arranca de 0 al número, así que se le suma 1
# El 3ro cada cuanto va iterando
#for i in range(3, -10, -3);
for contador in range(1, num_usuario_int + 1, 1):
    if num_usuario_int % contador == 0:
        print(f"Divisores: {contador}") 
        
""" 
for contador in range(num_usuario_int):
    contador += 1
    if num_usuario_int % contador == 0:
        print(f"Divisores: {contador}")  """