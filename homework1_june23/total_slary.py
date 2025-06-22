def total_salary(path):
    try:
        with open(path, 'r', encoding='utf-8') as file:
            salaries = []
            for line in file:
                parts = line.strip().split(',')
                if len(parts) != 2:
                    continue  # пропускаємо рядки з некоректним форматом
                try:
                    salary = float(parts[1])
                    salaries.append(salary)
                except ValueError:
                    continue  # пропускаємо рядки з нечисловими зарплатами

            if not salaries:
                return 0, 0

            total = sum(salaries)
            average = total / len(salaries)
            return total, average

    except FileNotFoundError:
        print("Помилка: файл не знайдено.")
        return 0, 0
    except Exception as e:
        print(f"Сталася помилка: {e}")
        return 0, 0
    
total, average = total_salary("homework1_june23\salary.txt")
print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")

