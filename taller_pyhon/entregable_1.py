lado_a:float = float(input("Ingrese la primer longitud: "))
lado_b:float = float(input("Ingrese la segunda longitud: "))
lado_c:float = float(input("Ingrese la tercera longitud: "))

if (lado_a == lado_b and lado_b == lado_c):
    print("segun las longitudes es un triangulo equilatero")
elif (lado_a == lado_b or lado_b == lado_c or lado_c == lado_a ):
    print(" segun los lados es un triangulo isosceles")
else:
    print("El triangulo es un escaleno")

    
