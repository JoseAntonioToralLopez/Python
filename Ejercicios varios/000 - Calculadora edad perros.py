"EDAD HUMANA A EDAD DE PERROS EN PYTHON"


def edad_perro(edad_humana):
    if edad_humana < 0:
        print("La edad tiene que ser mayor que 0")
    elif edad_humana < 2:
        return edad_humana * 10.5
    else:
        return 21 + (edad_humana - 2) * 4
    

edad_humana = int(input("Introduce tu edad: "))

print(f"Tu edad perruna es de {edad_perro(edad_humana)} años")