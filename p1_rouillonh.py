def digitos():
    nums = []
    print("Ingrese números de 2 digitos")
    print("Si desea dejar de ingresar numeros, escriba cualquier no número o decimal")
    while True:
        n = input("Número: ")
        if n.isdigit() == False:
            break
        elif n.isdigit()== True:  
            if len(str(n)) == 2:
                nums.append(int(n))
                continue
            else:
                print("El número ingresado no tiene 2 digitos, no será contabilizado")
                continue  
    return nums
nums = digitos()
suma = 0
for i in nums:
    suma += i
print("La suma de los valores de la lista es ",suma)
print("La suma multiplicada por 9 es: ",suma*9)
mayor = 0
menor = 100
for i in nums:
    if i > mayor:
        mayor = i
print("El número mayor es ",mayor)
for i in nums:
    if i < menor:
        menor = i
print("El número menor es ", menor)
print("La cantidad de elementos de la lista es ", len(nums))
