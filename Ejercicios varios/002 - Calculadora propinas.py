"CALCULADORA DE PROPINAS EN PYTHON"

def get_tip_value(bill, tip_pct):
    if bill < 0 or tip_pct < 0:
        print("Los valores tienen que ser positivos")
    else:
        tip_value = bill*(tip_pct/100)
        total_bill = bill + tip_value
        print(f"El valor de la propina es de {round(tip_value, 2)} €")
        print(f"Total a pagar {round(total_bill, 2)} €")

bill = float(input("Introduce el valor de la cuenta (€): "))
tip_pct = float(input("Introduce el valor de la propina (%): "))

get_tip_value(bill, tip_pct)