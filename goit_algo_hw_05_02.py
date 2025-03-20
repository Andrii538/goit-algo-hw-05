from typing import Callable
import re


def generator_numbers(text: str):
    """
    Функція, яка аналізує текст, ідентифікує всі дійсні числа і повертати їх як генератор.\n
    Аргумент:
    text (str): Рядок по якому здійснюється пошук.\n
    Повертає:
    Генератор дійсних чисел.
    """
    cleaned_num = re.findall(r"\d+\.\d+|\d+", text)  # Знаходимо всі дійсні числа в рядку.
    # Ітеруємо по знайденим дійсним числам і повертаємо генератор.
    for num in cleaned_num:
        yield float(num)


def sum_profit(text: str, func: Callable):
    """
    Функція, яка обчислює загальну суму знайдених дійсних чисел.\n
    Аргумент:
    text (str): Рядок з текстом по якому здійснюється пошук.\n
    func (Callable): Функція яка здійснює пошук.\n
    Повертає:
    Суму дійсних чисел знайдених функцією func в рядку text.
    """
    total = 0
    for num in func(text):
        total += num
    return total


text = "Загальний дохід працівника складається з декількох частин: 1000.01 як основний дохід, доповнений додатковими надходженнями 27.45 і 324.00 доларів."
total_income = sum_profit(text, generator_numbers)
print(f"Загальний дохід: {total_income}")
