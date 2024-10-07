import os
import shutil
import argparse
from pathlib import Path


def parse_args():

    parser = argparse.ArgumentParser(
        description='Рекурсивне копіювання файлів та сортування за розширенням.')
    parser.add_argument('source_dir', type=str, nargs='?',
                        help='Шлях до вихідної директорії')
    parser.add_argument('dest_dir', type=str, nargs='?', default='dist',
                        help='Шлях до директорії призначення (за замовчуванням dist)')
    return parser.parse_args()


def copy_and_sort_files(src_dir, dest_dir):
    try:
        # Перебір файлів і директорій у вихідній директорії
        for item in os.listdir(src_dir):
            src_path = os.path.join(src_dir, item)

            # Якщо це директорія, викликаємо рекурсивно цю ж функцію
            if os.path.isdir(src_path):
                copy_and_sort_files(src_path, dest_dir)
            # Якщо це файл, копіюємо його в нову піддиректорію за розширенням
            elif os.path.isfile(src_path):
                # Отримуємо розширення файлу без крапки
                file_extension = Path(src_path).suffix[1:]
                if not file_extension:
                    # Якщо немає розширення, називаємо теку 'no_extension'
                    file_extension = 'no_extension'

                # Створюємо піддиректорію на основі розширення файлу
                target_dir = os.path.join(dest_dir, file_extension)
                os.makedirs(target_dir, exist_ok=True)

                # Копіюємо файл до відповідної піддиректорії
                target_path = os.path.join(target_dir, item)
                shutil.copy2(src_path, target_path)
                print(f'Копіюємо {src_path} до {target_path}')
    except Exception as e:
        print(f'Помилка при обробці файлу {src_path}: {e}')


def main():
    # Парсимо аргументи командного рядка
    args = parse_args()

    # Якщо аргументи не були передані, запитуємо у користувача
    if not args.source_dir:
        args.source_dir = input(
            "Введіть шлях до вихідної директорії: ").strip()
    if not args.dest_dir or args.dest_dir == 'dist':
        dest_input = input(
            "Введіть шлях до директорії призначення (за замовчуванням 'dist'): ").strip()
        if dest_input:
            args.dest_dir = dest_input

    # Перевіряємо наявність вихідної директорії
    if not os.path.exists(args.source_dir):
        print(f"Вихідна директорія {args.source_dir} не існує.")
        return

    # Створюємо директорію призначення, якщо її ще немає
    os.makedirs(args.dest_dir, exist_ok=True)

    # Викликаємо функцію для копіювання та сортування файлів
    copy_and_sort_files(args.source_dir, args.dest_dir)


if __name__ == '__main__':
    main()
