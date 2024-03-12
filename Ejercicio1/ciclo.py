op = "si"
while op == "si":
    edad = int(input("Ingrese edad: "))
    precio = int(input("Ingrese precio asiento: "))

    if 5 < edad <= 14:
        descuento = 0.35
    elif 14 < edad <= 19:
        descuento = 0.25
    elif 19 < edad <= 45:
        descuento = 0.10
    elif 45 < edad <= 65:
        descuento = 0.25
    elif edad > 65:
        descuento = 0.35  
    else:
        print("No cumple con edad mínima")
        exit()
        
    final = round(descuento*precio)
    print("Precio asiento: $" + str(precio))
    print("Descuento: $"+ str(final))
    print("Precio final: $" + str(precio - final))
    op = input("Desea realizar otra consulta? si/no: ")