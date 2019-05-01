import datetime

def print_header():
    print('----------------------------')
    print('         CUMPLE APP         ')
    print('----------------------------')


'''
Obtiene los datos de la fecha de nacimiento del usuario
luego lo convierte en un formato de fecha para python y lo retorna
'''

def get_birthday_from_user():
    print('Cuando naciste?')
    year = int(input("Anio [YYYY]:"))
    month = int(input("Mes [MM]:"))
    day = int(input("Dia [DD]:"))

    birthday = datetime.date(year, month, day)
    return birthday


'''
Toma la fecha insertada por el usuario (original_date) y la fecha de hoy, obtenida
en el main, determina el anio actual y lo resta del anio que el usuario introdujo
para returnar el numero de dias
'''
def compute_days_beetween_dates(original_date, target_date):
    this_year = datetime.date(target_date.year, original_date.month, original_date.day)
    dt = this_year - target_date
    return dt.days


'''
Imprime el numero de dias restantes para el cumpleanios
tambien puede determinar si el cumple ya paso o si es hoy
'''
def print_birthday_information(days):
    if days < 0:
        print(f"Tu cumple fue hace {-days} dias este anio")
    elif days > 0:
        print(f"Tu cumple es en {days} dias!")
    else:
        print('Feliz cumple!!!')


def main():
    print_header()
    bday = get_birthday_from_user()
    today = datetime.date.today()
    number_of_days = compute_days_beetween_dates(bday, today)
    print_birthday_information(number_of_days)

main()
