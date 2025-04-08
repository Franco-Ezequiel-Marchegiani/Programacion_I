metros_consumidos = float(input("Ingrese la cantidad de metros cúbicos consumidos: "))
tipo_cliente = input("Ingrese su tipo de cliente, opciones: \n 'Residencial', 'Comercial' o 'Industrial': ")

error = False

consumo_base = 7000
costo_metro_cubico = 200
costo_consumo = costo_metro_cubico * metros_consumidos

subtotal_consumo = consumo_base + costo_consumo
bonificaciones = 0
recargos = 0
iva = 0.21
subtotal = 0
pago_final = 0
descuento_especial = False
print(f"subtotal_consumo: {subtotal_consumo}")
match tipo_cliente:
    case "Residencial":
        if metros_consumidos < 30:
            bonificaciones = 0.10 # -10%
        elif metros_consumidos > 80:
            recargos = 0.15 # +15% 
        
        #Especial Case:
        if subtotal_consumo < 35000:
            descuento_especial = True
            subtotal_consumo = subtotal_consumo - (subtotal_consumo * 0.05) #Descuento especial -5%

    case "Comercial":
        if metros_consumidos < 50:
            recargos = 0.05 # +5% 
        elif metros_consumidos > 150: # and metros_consumidos <= 300
            bonificaciones = 0.08 # -8%
        elif metros_consumidos > 300:
            bonificaciones = 0.12 # -12%
        
    case "Industrial":
        if metros_consumidos < 200:
            recargos = 0.10 # +10%
        elif metros_consumidos > 500: # and metros_consumidos <= 300
            bonificaciones = 0.20 # -8%
        elif metros_consumidos > 1000:
            bonificaciones = 0.30 # -12%
    case _:
        error = True
        print("Ingrese un tipo de cliente válido")

#Pasadas las validaciones, sumamos beneficios y recargos:

if bonificaciones != 0:
    subtotal_consumo = subtotal_consumo - (subtotal_consumo * bonificaciones) 

if recargos != 0:
    subtotal_consumo = subtotal_consumo + (subtotal_consumo * recargos) 

#Asignamos el subtotal ya con los beneficios o recargos
subtotal = subtotal_consumo
#Asignamos el IVA y mostramos el pago final
pago_final = subtotal + (subtotal * iva)

print("------------------------------")
print(f"Tipo de cliente: {tipo_cliente}")
print(f"Cantidad de metros consumidos fueron: {metros_consumidos}")
print(f"Consumo base de: ${consumo_base}")
print(f"Costo de consumo: ${costo_consumo}")
print(f"{bonificaciones}% de Bonificaciones")
print(f"{recargos}% de recargos")
if descuento_especial:
    print(f"5% de descuento especial")
print(f"Subtotal con recargos y bonificaciones: {subtotal}")
print(f"IVA: {iva}")
print(f"Total final a pagar: ${pago_final} ")
print("------------------------------")
