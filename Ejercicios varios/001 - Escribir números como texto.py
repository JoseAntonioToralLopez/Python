"PEDIR UN NÚMERO POR PANTALLA Y DEVOLVERLO ESCRITO"
"DE 7 A SIETE"


def text_number(int_number):
    if int_number < 0 or int_number > 9:
        print("El número tiene que estar comprendido entre 0 y 9")
    else:
        numbers = ["Cero", "Uno", "Dos", "Tres", "Cuatro", "Cinco", "Seis", "Siete", "Ocho", "Nueve"]
        return numbers[int_number] 

int_number = int(input("Introduce un número (0-9): "))
print(text_number(int_number))



