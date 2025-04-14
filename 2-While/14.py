# Pedir al usuario el ingreso de una nota. La misma debe estar comprendida entre 1 y 10 inclusive.

validador = True

while validador:
    ingresar_clave = float(input("Ingrese un número entre 1 y 10: "))
    if ingresar_clave >= 1 and ingresar_clave <= 10:
        validador = False
    else:
        print("Valor incorrecto, intente nuevamente.")

print(f"Muy bien!")