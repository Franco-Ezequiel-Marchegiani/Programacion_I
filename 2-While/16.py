# Solicitarle al usuario el ingreso de un color. Validar que el mismo sea Rojo, Verde o Azul.

apellido = ''
edad = 0
estado_civil = ''
num_legajo = 0
validador = True

while validador:
    ingreso_apellido = input("Ingrese su apellido: ")
    ingreso_edad = float(input("Ingrese su edad: "))
    ingreso_estado_civil = input("Ingrese su estado civil: ")
    ingreso_num_legajo = float(input("Ingrese su número de legajo (4 números): "))
    if ((ingreso_edad >= 18 and ingreso_edad <= 90) 
        and 
        (ingreso_estado_civil == "Soltero/a" 
            or ingreso_estado_civil == "Casado/a" 
            or ingreso_estado_civil == "Divorciado/a" 
            or ingreso_estado_civil == "Viudo/a"
        )):
        #Asignamos valores a variables si está todo ok
        apellido = ingreso_apellido
        edad = ingreso_edad
        estado_civil = ingreso_estado_civil
        num_legajo = ingreso_num_legajo
        validador = False
    else:
        print("Corrobore los datos e intente nuevamente.")

print("Datos guardados correctamente! Su información es: ")
print("------------------------------------------------------------------")
print(f"apellido: {apellido} ")
print(f"edad: {edad} ")
print(f"estado_civil: {estado_civil} ")
print(f"num_legajo: {num_legajo} ")
print("------------------------------------------------------------------")