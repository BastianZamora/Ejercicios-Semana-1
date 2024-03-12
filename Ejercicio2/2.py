ing = int(input("Indique ingresos: $"))
costoCasa = 10000000

if 0 < ing < 80000:
    años = 7
    pie = round(0.3 * costoCasa)
    pagoMensual = round((costoCasa - pie) / 84)
elif 80000 <= ing:
    años = 10
    pie = round(0.15 * costoCasa)
    pagoMensual = round((costoCasa - pie) / 120)
else:
    print("Error")
    pie = 0
    pagoMensual = 0
    años = "error"
print("Pie: $" + str(pie))
print("Pago mensual por",años,"años: $" + str(pagoMensual))