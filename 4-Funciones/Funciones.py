def validador_int( param_user: None, texto_visible: str) -> int:
    """ 
        Recibe una variable vacía, valida que lo que ingrese el usuario
        sea un string numérico positivo, utilizando "isdigit()" para ello.
        También muestra el mensaje que recibe por parámetros

    Args:
        param_user: Variable vacía para rellenar con lo que el usuario ingrese
        texto_visible: Texto que le indicará al usuario qué ingresar

    Returns:
        Devuelve una variable type int con el dato que el usuario haya seleccionado
        Ya validado que sea un número
    """
    #Validamos que sí o sí sea un número con isdigit(), en formato str
    while param_user == None or not param_user.isdigit():
        param_user = input(f"{texto_visible}")
    
    return int(param_user)

def validador_int_none( param_user: str, texto_visible: str) -> int | str:
    """ 
        Recibe una variable vacía, valida que lo que ingrese el usuario
        sea un string numérico positivo, utilizando "isdigit()" para ello.
        También muestra el mensaje que recibe por parámetros

    Args:
        param_user: Variable vacía para rellenar con lo que el usuario ingrese
        texto_visible: Texto que le indicará al usuario qué ingresar

    Returns:
        Devuelve una variable type int con el dato que el usuario haya seleccionado
        Ya validado que sea un número
    """
    
    #Validamos que sí o sí sea un número con isdigit(), en formato str
    while param_user == None or not param_user.isdigit():
        param_user = input(f"{texto_visible}")
        if param_user == "":
            return param_user
    
    return int(param_user)