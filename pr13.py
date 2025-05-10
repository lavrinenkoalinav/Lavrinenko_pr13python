 import os

# Завдання 1: Простий текстовий редактор
def simple_text_editor():
    filename = input("Введіть ім'я нового файлу (з .txt): ")

    with open(filename, 'w', encoding='utf-8') as file:
        print("Введіть текст (порожній рядок — завершення):")
        while True:
            line = input()
            if line == "":
                break
            file.write(line + "\n")

    print("\nФайл збережено. Вміст файлу:")
    with open(filename, 'r', encoding='utf-8') as file:
        print(file.read())

# Завдання 2: Аналіз вмісту файлу
def analyze_file_content():
    filename = input("Введіть ім'я файлу для аналізу: ")

    try:
        with open(filename, 'r', encoding='utf-8') as file:
            content = file.read()
        lines = content.splitlines()
        words = content.split()
        characters = len(content)

        print("\nАналіз файлу:")
        print(f"Кількість рядків: {len(lines)}")
        print(f"Кількість слів: {len(words)}")
        print(f"Кількість символів: {characters}")
    except FileNotFoundError:
        print("Файл не знайдено!")

# Завдання 3: Пошук і заміна
def search_and_replace():
    filename = input("Введіть ім'я файлу для пошуку та заміни: ")

    try:
        with open(filename, 'r', encoding='utf-8') as file:
            content = file.read()

        to_find = input("Що потрібно знайти: ")
        to_replace = input("На що замінити: ")

        new_content = content.replace(to_find, to_replace)
        new_filename = input("Введіть ім'я нового файлу для збереження змін: ")

        with open(new_filename, 'w', encoding='utf-8') as file:
            file.write(new_content)

        print(f"\nЗміни збережено у файлі: {new_filename}")
    except FileNotFoundError:
        print("Файл не знайдено!")

# Головне меню
def main():
    while True:
        print("\n--- Меню ---")
        print("1. Простий текстовий редактор")
        print("2. Аналіз вмісту файлу")
        print("3. Пошук і заміна")
        print("4. Вихід")
        choice = input("Оберіть дію (1-4): ")

        if choice == '1':
            simple_text_editor()
        elif choice == '2':
            analyze_file_content()
        elif choice == '3':
            search_and_replace()
        elif choice == '4':
            print("Програма завершена.")
            break
        else:
            print("Невірний вибір. Спробуйте ще раз.")

if __name__ == "__main__":
    main()

