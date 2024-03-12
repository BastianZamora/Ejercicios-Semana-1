edad = int(input("Ingrese edad: "))
precio = int(Input("Ingrese precio entrada: "))
if edad < 6:
    print("No cumple con edad mínima")
    exit()
if 5 < edad:
    descuento = 0.35
    if 14 < edad:
        descuento = 0.25
        if 19 < edad:
            descuento = 0.10
            if 45 < edad:
                descuento = 0.25
                if 65 < edad:
                    descuento = 0.35
    
final = round(descuento*precio)
print("Precio asiento: $" + str(precio))
print("Descuento: $"+ str(final))
print("Precio final: $" + str(precio - final))
