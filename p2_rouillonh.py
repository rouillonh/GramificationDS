values = []
#Este mensaje es para avisar al usuario lo que tiene que hacer para terminar el bucle
print("Si usted desea terminar de ingresar valores, ingrese 'fin'")
#El bucle es para que se ingresen los valores
while True:
    x = input("Valor: ")
    values.append(x)
    if x == "fin":
        break
#imprimimos las listas con y sin los valores repetidos y ordenados
print(values)
values = list(set(values))
print(values)   