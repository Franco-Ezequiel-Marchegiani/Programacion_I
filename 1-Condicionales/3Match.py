""" 
Una agencia de viajes nos pide informar si hacemos viajes a lugares según la estación del año. 
En caso de hacerlo mostrar por print  el mensaje “Se viaja”, caso contrario mostrar “No se viaja”. 
Si es invierno: solo se viaja a Bariloche.
Si es verano: se viaja a Mar del plata y Cataratas.
Si es otoño: se viaja a todos los lugares.
Si es primavera: se viaja a todos los lugares menos Bariloche.
"""

estacion = input("Ingrese la estación del año. Opciones: \n 'invierno', 'verano', 'otoño', 'primavera': ")
destino = input("Ingrese el destino que desea viajar. Opciones: \n 'Bariloche', 'Mar del plata', 'Cataratas': ")
error = False
mensaje = "No se viaja"
match estacion:
    case "invierno":
        match destino:
            case "Bariloche":
                mensaje = "Se viaja"
            case _:
                print("Por favor, ingrese un destino válido")
                error = True

    case "verano" | "primavera":
        match destino:
            case "Mar del plata" | "Cataratas":
                mensaje = "Se viaja"
            case _:
                print("Por favor, ingrese un destino válido")
                error = True
    case "otoño":
        match destino:
            case "Mar del plata" | "Cataratas" | "Bariloche":
                mensaje = "Se viaja"
            case _:
                print("Por favor, ingrese un destino válido")
                error = True
    case _:
        print("Por favor, ingrese una estación válida")
        error = True

if error == False:
    print(mensaje)