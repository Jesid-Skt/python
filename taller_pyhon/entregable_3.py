numero_1:float =float(input("ingresa la primer numero: "))
numero_2:float =float(input("ingresa el segundo numero: "))
numero_3:float =float(input("ingresa el tercer numero: ")) 


if numero_1 <= numero_2 and numero_1 <= numero_3:
    if numero_2 <= numero_3:
        print(int(numero_1), int(numero_2), int(numero_3))
    else:
        print(int(numero_1), int(numero_3), int(numero_2))
elif numero_2 <= numero_1 and numero_2 <= numero_3:
    if numero_1 <= numero_3:
        print(int(numero_2), int(numero_1), int(numero_3))
    else:
        print(int(numero_2),int( numero_3), int(numero_1))
else:
    if numero_1 <= numero_2:
        print (int(numero_3), int(numero_1), int(numero_2))
    else:
        print (int(numero_3), int(numero_2), int(numero_1))