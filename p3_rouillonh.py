gadgets = ["Batería","Portátil",100,"Ordenador Central",310.28,"Altavoces",27.00,"Pantalla",1000,"Maletín Electrónico","Lente de cámara"]
cadenas = []
numeros = []
for i in gadgets:
    if type(i) == str:
        cadenas.append(i)
    elif type(i) == int or type(i) == float:
        numeros.append(i)
cadenas2 = sorted(cadenas)
nums = sorted(numeros)
print("\nCadena en orden ascendente ",cadenas2)
print("\nCadena en orden descendente ",list(reversed(cadenas2)))
print("\nNúmeros en orden ascendente ",nums)
print("\nNúmeros en orden descendente ",list(reversed(nums)),"\n")
