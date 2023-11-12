print("Salario")
horas = float(input("Ingrese horas de trabajo: "))
tarifa = float(input("Ingrese tarifa de trabajo: "))

if horas > 40:
    horas_trabajadas = 40
    horas_extra = horas - 40 
else:
    horas_trabajadas = 0
    horas_extra = 0

salario = (horas_trabajadas * tarifa) + (horas_extra*tarifa*1.5)
print(salario)