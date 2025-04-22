# Define una función que encuentre el máximo de tres números. La función debe aceptar tres argumentos y devolver el número más grande.


num_usuario = None
num_usuario_dos = None
num_usuario_tres = None
while ((num_usuario == None or not num_usuario.isdigit()) 
        or (num_usuario_dos == None or not num_usuario_dos.isdigit()) 
        or (num_usuario_tres == None or not num_usuario_tres.isdigit())
    ):
    num_usuario = input("Ingrese un número: ")
    num_usuario_dos = input("Ingrese un segundo número: ")
    num_usuario_tres = input("Ingrese un último número: ")

num_usuario_int = int(num_usuario)
num_usuario_dos_int = int(num_usuario_dos)
num_usuario_tres_int = int(num_usuario_tres)

def identificador_max( 
        num_ingresado: int,
        num_usuario_dos_int: int, 
        num_usuario_tres_int: int ):
    """ 
    Analiza los 3 parámetros, y de ahí devuelve el valor más alto
    """
    #Si el primer número es el mayor, retorna ese número
    if (num_ingresado >= num_usuario_dos_int) and (num_ingresado >= num_usuario_tres_int):
        return num_ingresado
    #Si el segundo número es el mayor, lo devuelve
    elif (num_usuario_dos_int >= num_ingresado) and (num_usuario_dos_int >= num_usuario_tres_int):
        return num_usuario_dos_int
    #Si el tercer número es el mayor, lo devuelve
    elif (num_usuario_tres_int >= num_ingresado) and (num_usuario_tres_int >= num_usuario_dos_int):
        return num_usuario_tres_int
    else:
        return False

llamada_funcion = identificador_max(num_usuario_int, num_usuario_dos_int, num_usuario_tres_int)

if llamada_funcion == False:
    print("Ocurrió un error, intente nuevamente")
else:
    print(f"El valor más alto ingresado es: {llamada_funcion}")