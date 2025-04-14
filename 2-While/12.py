# Pedir el ingreso de una clave. Validar que el ingreso del usuario sea correcto. Tendrá intentos indeterminados.

clave = '720'

validador = True
while validador:
    ingresar_clave = input("Ingrese la clave: ")
    if ingresar_clave == clave:
        validador = False
    else:
        print("Clave incorrecta, intente nuevamente.")

print(f"Bienvenido!")