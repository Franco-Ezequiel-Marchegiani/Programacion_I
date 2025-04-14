#Pedir el ingreso de una clave. Validar que el ingreso del usuario sea correcto. Solo tendrá 3 intentos.

contador = 3
clave = '720'

validador = True
validation = True
while validador:
    
    ingresar_clave = input("Ingrese la clave: ")
    if ingresar_clave == clave:
        validador = False
        validation = True
    else:
        contador -= 1
        if contador == 0:
            print(f"Clave incorrecta, cuenta bloqueada.")
        else:
            print(f"Clave incorrecta, le quedan {contador} intentos.")
    if contador == 0:
        validador = False
        validation = False

if validation:
    print(f"Bienvenido!")
else:
    print("Llegó al límite de intentos, comuniquese al 0800...")