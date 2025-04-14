# Solicitarle al usuario el ingreso de un color. Validar que el mismo sea Rojo, Verde o Azul.

validador = True

while validador:
    ingresar_clave = input("Ingrese un color: ")
    if ingresar_clave == "Rojo" or ingresar_clave == "Verde" or ingresar_clave == "Azul":
        validador = False
    else:
        print("Mhh pruebe con otro.")

print(f"Bienvenido a Telefé!")