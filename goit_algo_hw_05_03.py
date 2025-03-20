from collections import Counter
import re
import sys


def load_logs(file_path: str) -> list:
    """Завантажує лог-файл і парсить кожен рядок."""
    with open(file_path, 'r') as file:
        return [parse_log_line(line) for line in file]


def parse_log_line(line: str) -> dict:
    """Парсить один рядок логу у словник."""
    log_dict = {}
    pattern = r'(\d{4}-\d{2}-\d{2}) (\d{2}:\d{2}:\d{2}) (\b[A-Z]+\b) (.+)'
    text = re.split(pattern, line)    
    log_dict['Date'] = text[1]
    log_dict['Time'] = text[2]
    log_dict['Level'] = text[3]
    log_dict['Text'] = text[4]
    return log_dict
    

def filter_logs_by_level(logs: list, level: str) -> list:
    """Фільтрує логи за рівнем."""
    logs_by_level = []
    for log in logs:
        if log['Level'] == level:
            line_log = ''.join(f'{log['Date']} {log['Time']} - {log['Text']}')
            logs_by_level.append(line_log)
    return logs_by_level


def count_logs_by_level(logs: list) -> dict:
    """Підраховує кількість записів кожного рівня логування."""
    return dict(Counter(log["Level"] for log in logs))


def display_log_counts(counts: dict):
    """Виводить таблицю статистики."""
    top_string = f'\nРівень логування | Кількість\n{"-"*17}|{"-"*10}\n'
    main_text = '\n'.join(f'{level:<17}| {counts[level]}' for level in counts)
    return top_string + main_text


def main():
    if len(sys.argv) < 2:
        print("Помилка: потрібно вказати шлях до лог-файлу.")
        return
    path = sys.argv[1]
    try:
        log_list = load_logs(path)
        if not log_list:  # Перевірка, чи логи взагалі є
            print(f"Помилка: файл '{path}' існує, але він порожній або не містить коректних логів.")
            return
        print(display_log_counts(count_logs_by_level(log_list)))
        if len(sys.argv) > 2:
            level = sys.argv[2].upper()
            filtered_logs = filter_logs_by_level(log_list, level)
            if filtered_logs:
                print(f"\nДеталі для рівня '{level}':")
                print("\n".join(filtered_logs))
            else:
                print(f"\nРівень '{level}' не знайдено у логах.")
    except FileNotFoundError:
        print(f"Помилка: файл '{path}' не знайдено.")
    except IndexError:
        print(f"Помилка під час читання файлу")


if __name__ == "__main__":
    main()
