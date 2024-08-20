precio_total:float = float(input("Ingrese el precio del producto: "))
porcentaje:float = float(input("Ingrese el descuento: "))

descuento = precio_total*(porcentaje/100)
precio_final= precio_total-descuento

print("El precio total es : " , int(precio_total))
print("El precio final con el descuento es de: " , int(precio_final))