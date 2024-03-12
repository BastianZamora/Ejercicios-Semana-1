op = "si"
while op == "si":
    ing = int(input("Indique ingresos: $"))
    costoCasa = int(input("Ingrese el valor de la casa: "))

    if 0 < ing < 80000:
        años = 7
        pie = round(0.3 * costoCasa)
        pagoMensual = round((costoCasa - pie) / 84)
        print("Pie: $" + str(pie))
        print("Pago mensual por",años,"años: $" + str(pagoMensual))
    elif 80000 <= ing:
        años = 10
        pie = round(0.15 * costoCasa)
        pagoMensual = round((costoCasa - pie) / 120)
        print("Pie: $" + str(pie))
        print("Pago mensual por",años,"años: $" + str(pagoMensual))
    else:
        print("Error")
    op = input("Desea hacer otra consulta? si/no: ")