import sys
from pathlib import Path
from colorama import init, Fore, Style

# Ініціалізація colorama для підтримки кольорів у терміналі
init(autoreset=True)

def display_directory_structure(path, indent_level=0):
    """
    Рекурсивно відображає структуру директорії з кольоровим виведенням.

    Args:
        path (Path): Об'єкт Path, що вказує на поточну директорію або файл.
        indent_level (int): Рівень відступу для візуалізації ієрархії.
    """
    prefix = "  " * indent_level
    if indent_level > 0:
        prefix += "┣ " if path.is_dir() else "┣ 📜"

    if path.is_dir():
        # Виведення імені директорії синім кольором
        print(f"{prefix}{Fore.BLUE}📂{path.name}{Style.RESET_ALL}")
        # Рекурсивний виклик для піддиректорій та файлів
        for item in sorted(path.iterdir()):
            display_directory_structure(item, indent_level + 1)
    elif path.is_file():
        # Виведення імені файлу зеленим кольором
        print(f"{prefix}{Fore.GREEN}{path.name}{Style.RESET_ALL}")

def main():
    """
    Головна функція скрипта, яка обробляє аргументи командного рядка
    та запускає відображення структури директорії.
    """
    # Перевірка наявності аргументу командного рядка
    if len(sys.argv) < 2:
        print(f"{Fore.RED}Помилка: Будь ласка, вкажіть шлях до директорії як аргумент.")
        print(f"Використання: python {Path(__file__).name} <шлях_до_директорії>{Style.RESET_ALL}")
        sys.exit(1)

    # Отримання шляху з аргументів командного рядка
    target_path = Path(sys.argv[1])

    # Перевірка існування шляху
    if not target_path.exists():
        print(f"{Fore.RED}Помилка: Вказаний шлях '{target_path}' не існує.{Style.RESET_ALL}")
        sys.exit(1)

    # Перевірка, чи є шлях директорією
    if not target_path.is_dir():
        print(f"{Fore.RED}Помилка: Вказаний шлях '{target_path}' не є директорією.{Style.RESET_ALL}")
        sys.exit(1)

    print(f"{Fore.CYAN}Відображення структури директорії: '{target_path}'{Style.RESET_ALL}\n")
    # Початок відображення структури з кореневої директорії
    display_directory_structure(target_path)

if __name__ == "__main__":
    main()
