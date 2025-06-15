# exercise_1 
from datetime import datetime
def get_days_from_today(date):
    try:
        input_date = datetime.strptime(date, '%Y-%m-%d').date()                 # Перетворення рядка у дату
        today = datetime.today().date()                                         # Поточна дата
        delta = today - input_date                                              # Обчислення різниці у днях
        return delta.days
    except ValueError:
        print("Неправильний формат дати. Використовуйте 'РРРР-ММ-ДД'.")         # Обробка неправильного формату дати
        return None

print(get_days_from_today("2021-10-09"))                                        # Може повернути, наприклад, -1344 (залежить від поточної дати)
print(get_days_from_today("2025-06-01"))                                        # Наприклад, 13 (якщо сьогодні 2025-06-14)
print(get_days_from_today("wrong-format"))                                      # Виведе повідомлення про помилку і поверне None



# exercise_2
import random
def get_numbers_ticket(min, max, quantity):
    if not (1 <= min <= max <= 1000) or \
       not (min <= quantity <= max):
       return []
    numbers = random.sample(range(min, max + 1), quantity)
    return sorted(numbers)
lottery_numbers = get_numbers_ticket(1, 49, 6)
print("Ваші лотерейні числа:", lottery_numbers)





# exercise_3
import re
def normalize_phone(phone_number):
    digits = re.sub(r'\D', '', phone_number)                                  # Видаляємо всі символи, крім цифр
    if digits.startswith('380'):                                              # Обробка номера з міжнародним кодом
        return '+{}'.format(digits)
    elif digits.startswith('0'):
        return '+38{}'.format(digits)
    elif digits.startswith('38'):
        return '+{}'.format(digits)
    else:
        return '+38{}'.format(digits)
    
raw_numbers = [
    "067\t123 4567",
    "(095) 234-5678\n",
    "+380 44 123 4567",
    "380501234567",
    "    +38(050)123-32-34",
    "     0503451234",
    "(050)8889900",
    "38050-111-22-22",
    "38050 111 22 11   ",
]
sanitized_numbers = [normalize_phone(num) for num in raw_numbers]
print("Нормалізовані номери телефонів для SMS-розсилки:", sanitized_numbers)




# exercise_4
from datetime import datetime, timedelta

def get_upcoming_birthdays(users):
    today = datetime.today().date()
    in_7_days = today + timedelta(days=7)
    upcoming = []
    for user in users:
        birthday = datetime.strptime(user["birthday"], "%Y.%m.%d").date()
        birthday_this_year = birthday.replace(year=today.year)
        if birthday_this_year < today:
            birthday_this_year = birthday_this_year.replace(year=today.year + 1)
        if today <= birthday_this_year <= in_7_days:
            congratulation_date = birthday_this_year
            if congratulation_date.weekday() == 5:  # субота
                congratulation_date += timedelta(days=2)
            elif congratulation_date.weekday() == 6:  # неділя
                congratulation_date += timedelta(days=1)
            upcoming.append({
                "name": user["name"],
                "congratulation_date": congratulation_date.strftime("%Y.%m.%d")
            })

    return upcoming
users = [
    {"name": "John Doe", "birthday": "1985.01.23"},
    {"name": "Jane Smith", "birthday": "1990.01.27"},
    {"name": "Mike Black", "birthday": "1983.01.28"},
    {"name": "Anna White", "birthday": "1986.01.29"}
]

upcoming_birthdays = get_upcoming_birthdays(users)
print("Список привітань на цьому тижні:", upcoming_birthdays)
