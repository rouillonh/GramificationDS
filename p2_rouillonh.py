values = []
print("Si usted desea terminar de ingresar valores, ingrese 'fin'")
while True:
    x = input("Valor: ")
    values.append(x)
    if x == "fin":
        break
print(values)
values = list(set(values))
print(values)