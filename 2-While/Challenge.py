contador = 0
capacidad_empleados = 9
#Cantidad de empleados de género masculino que votaron por IOT o IA, 
# cuya edad esté entre 25 y 50 años (inclusive)
contenedor_primer_case = 0
# Porcentaje de empleados que NO votaron por IA, siempre y cuando:
#- Su género no sea Femenino 
#- Su edad está entre los 33 y 40 años.
contenedor_segundo_case = 0
# Empleado masculino de mayor edad: Mostrar su nombre y la tecnología que votó.

while contador <= capacidad_empleados:
    #Datos usuario
    nombre = input("Ingrese su nombre: ")
    edad = float(input("Ingrese su edad: "))
    genero = input("Ingrese su genero. Masculino, Femenino, Otro: ")
    tecnologia = input("Seleccione su tecnología.\n IA \n RV/RA \n IOT \n")

    if (
            (genero == "Masculino" or genero == "masculino" ) 
            and (tecnologia == "IOT" or tecnologia == "IA") 
            and (edad >= 25 and edad <= 50)
        ):
            contenedor_primer_case += 1
    elif (
            (genero != 'Femenino' or genero != 'femenino') 
            and (edad >= 33 and edad <= 40)
        ):
            contenedor_segundo_case += 1
    elif  (
            (genero == "Masculino" or genero == "masculino" ) 
            and edad >= 18
        ):
            print(f"Nombre: {nombre} Tecnología seleccionada: {tecnologia}")

    contador += 1
    print(f"Empleado N°: {contador}")

porcentaje_segundo_caso = (contenedor_segundo_case * 100) / capacidad_empleados

print(f"El análisis fue el siguiente: \n")
print(f"-----------------------------------")
print(f"Cantidad de empleados registrados: {contador}")
print(f"Cantidad de empleados masculinos entre 25 y 50 años que votaron por IOT o IA: {contenedor_primer_case}")
print(f"Un {porcentaje_segundo_caso}% de los empleados NO votaron por IA.")
print(f"Se registraron los nombres de los empleados masculinos mayores de edad, y su tecnología seleccionada.")
print(f"-----------------------------------")