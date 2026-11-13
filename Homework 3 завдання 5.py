import inspect
import colorama
from colorama import Fore, Back, Style, Cursor, init


def detailed_inspection(obj, name):
    print(f"\n{'=' * 15} ІНТРОСПЕКЦІЯ КОМПОНЕНТА: {name} {'=' * 15}")
    members = inspect.getmembers(obj)

    public_members = [(m_name, m_val) for m_name, m_val in members if not m_name.startswith('_')]

    print(f"Знайдено публічних елементів: {len(public_members)}")
    for m_name, m_val in public_members:
        print(f"  • {m_name:<15} | Тип: {type(m_val).__name__:<10} | Значення: {repr(m_val)}")


def main():
    init(autoreset=True)

    print(f"Повна версія бібліотеки Colorama: {colorama.__version__}")

    detailed_inspection(colorama, "Модуль colorama")

    detailed_inspection(Fore, "Клас Fore (Кольори тексту)")

    detailed_inspection(Back, "Клас Back (Кольори фону)")

    detailed_inspection(Style, "Клас Style (Стилі оформлення)")

    detailed_inspection(Cursor, "Клас Cursor (Керування курсором)")

    print(f"\n{Style.BRIGHT}{Fore.CYAN}{'=' * 15} ДЕМОНСТРАЦІЯ ВИКОРИСТАННЯ {'=' * 15}")

    print(Style.BRIGHT + Fore.GREEN + "Цей текст яскравий і зелений.")
    print(Back.YELLOW + Fore.BLACK + "Цей текст має жовтий фон і чорний текст.")
    print(Style.DIM + "Цей текст приглушений (DIM).")

    print(Cursor.UP(1) + "Цей рядок піднято курсором вище.")

    print(Style.RESET_ALL + "\nУсі стилі успішно скинуто.")


if __name__ == "__main__":
    main()