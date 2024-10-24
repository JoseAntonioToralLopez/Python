
def add_numbers(number_choice, numbers):
    user_numbers = []

    while len(user_numbers<6):
        number_choice = int(input("Selecciona un número: "))

        if number_choice < 0 or number_choice > 60:
            print("Los números tienen que ser entre 0 y 60")

        numbers.append(number_choice)
        return numbers



print(user_numbers)