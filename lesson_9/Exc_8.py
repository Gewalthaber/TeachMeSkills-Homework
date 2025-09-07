import json
import csv
import os
from typing import List, Dict, Any


class EmployeeManager:
    def __init__(self, json_file: str = 'employees.json', csv_file: str = 'employees.csv'):
        self.json_file = json_file
        self.csv_file = csv_file
        self.ensure_files_exist()

    def ensure_files_exist(self):
        if not os.path.exists(self.json_file):
            with open(self.json_file, 'w', encoding='utf-8') as f:
                json.dump([], f)

        if not os.path.exists(self.csv_file):
            with open(self.csv_file, 'w', encoding='utf-8') as f:
                writer = csv.writer(f)
                writer.writerow(['name', 'birth_year', 'position', 'programming_languages', 'height'])

    def json_to_csv(self) -> None:
        try:
            with open(self.json_file, 'r', encoding='utf-8') as f:
                employees = json.load(f)

            if not employees:
                print("JSON файл пуст.")
                return

            with open(self.csv_file, 'w', encoding='utf-8') as f:
                writer = csv.writer(f)
                writer.writerow(['name', 'birth_year', 'position', 'programming_languages', 'height'])

                for employee in employees:
                    writer.writerow([
                        employee['name'],
                        employee['birth_year'],
                        employee['position'],
                        ';'.join(employee['programming_languages']),
                        employee['height']
                    ])

            print(f"Данные успешно преобразованы и сохранены в {self.csv_file}")

        except Exception as e:
            print(f"Ошибка при преобразовании JSON в CSV: {e}")

    def save_to_csv(self, employees: List[Dict[str, Any]]) -> None:
        try:
            with open(self.csv_file, 'w', encoding='utf-8') as f:
                writer = csv.writer(f)
                writer.writerow(['name', 'birth_year', 'position', 'programming_languages', 'height'])

                for employee in employees:
                    writer.writerow([
                        employee['name'],
                        employee['birth_year'],
                        employee['position'],
                        ';'.join(employee['programming_languages']),
                        employee['height']
                    ])

            print(f"Данные успешно сохранены в {self.csv_file}")

        except Exception as e:
            print(f"Ошибка при сохранении в CSV: {e}")

    def add_employee_to_json(self) -> None:
        try:
            print("\n=== Добавление нового сотрудника в JSON ===")

            name = input("Введите имя сотрудника: ").strip()
            birth_year = int(input("Введите год рождения: "))
            position = input("Введите должность: ").strip()

            print("Введите языки программирования (через запятую): ")
            programming_languages = [lang.strip() for lang in input().split(',')]

            height = float(input("Введите рост (в см): "))

            with open(self.json_file, 'r', encoding='utf-8') as f:
                employees = json.load(f)

            new_employee = {
                'name': name,
                'birth_year': birth_year,
                'position': position,
                'programming_languages': programming_languages,
                'height': height
            }

            employees.append(new_employee)

            with open(self.json_file, 'w', encoding='utf-8') as f:
                json.dump(employees, f, ensure_ascii=False, indent=2)

            print("Сотрудник успешно добавлен в JSON файл!")

        except ValueError:
            print("Ошибка: Неверный формат числовых данных!")
        except Exception as e:
            print(f"Ошибка при добавлении сотрудника: {e}")

    def add_employee_to_csv(self) -> None:
        try:
            print("\n=== Добавление нового сотрудника в CSV ===")

            name = input("Введите имя сотрудника: ").strip()
            birth_year = int(input("Введите год рождения: "))
            position = input("Введите должность: ").strip()

            print("Введите языки программирования (через запятую): ")
            programming_languages = [lang.strip() for lang in input().split(',')]

            height = float(input("Введите рост (в см): "))

            with open(self.csv_file, 'a', encoding='utf-8', newline='') as f:
                writer = csv.writer(f)
                writer.writerow([
                    name,
                    birth_year,
                    position,
                    ';'.join(programming_languages),
                    height
                ])

            print("Сотрудник успешно добавлен в CSV файл!")

        except ValueError:
            print("Ошибка: Неверный формат числовых данных!")
        except Exception as e:
            print(f"Ошибка при добавлении сотрудника: {e}")

    def find_employee_by_name(self) -> None:
        try:
            search_name = input("Введите имя для поиска: ").strip().lower()

            with open(self.json_file, 'r', encoding='utf-8') as f:
                employees = json.load(f)

            found = False
            for employee in employees:
                if employee['name'].lower() == search_name:
                    print("\nНайден сотрудник:")
                    self.print_employee(employee)
                    found = True
                    break

            if not found:
                print("Сотрудник с таким именем не найден.")

        except Exception as e:
            print(f"Ошибка при поиске сотрудника: {e}")

    def filter_by_language(self) -> None:
        try:
            language = input("Введите язык программирования для фильтрации: ").strip().lower()

            with open(self.json_file, 'r', encoding='utf-8') as f:
                employees = json.load(f)

            filtered_employees = []
            for employee in employees:
                if any(lang.lower() == language for lang in employee['programming_languages']):
                    filtered_employees.append(employee)

            if filtered_employees:
                print(f"\nСотрудники, владеющие языком '{language}':")
                for i, employee in enumerate(filtered_employees, 1):
                    print(f"\n{i}.")
                    self.print_employee(employee)
            else:
                print(f"Сотрудники, владеющие языком '{language}', не найдены.")

        except Exception as e:
            print(f"Ошибка при фильтрации по языку: {e}")

    def filter_by_year_and_height(self) -> None:
        try:
            year = int(input("Введите год рождения для фильтрации: "))

            with open(self.json_file, 'r', encoding='utf-8') as f:
                employees = json.load(f)

            filtered_employees = [emp for emp in employees if emp['birth_year'] < year]

            if filtered_employees:
                total_height = sum(emp['height'] for emp in filtered_employees)
                average_height = total_height / len(filtered_employees)

                print(f"\nСотрудники, родившиеся до {year} года:")
                for i, employee in enumerate(filtered_employees, 1):
                    print(f"\n{i}.")
                    self.print_employee(employee)

                print(f"\nСредний рост этих сотрудников: {average_height:.2f} см")
            else:
                print(f"Сотрудники, родившиеся до {year} года, не найдены.")

        except ValueError:
            print("Ошибка: Введите корректный год!")
        except Exception as e:
            print(f"Ошибка при фильтрации по году: {e}")

    def print_employee(self, employee: Dict[str, Any]) -> None:
        print(f"Имя: {employee['name']}")
        print(f"Год рождения: {employee['birth_year']}")
        print(f"Должность: {employee['position']}")
        print(f"Языки программирования: {', '.join(employee['programming_languages'])}")
        print(f"Рост: {employee['height']} см")

    def display_menu(self) -> None:
        print("\n" + "=" * 50)
        print("СИСТЕМА УПРАВЛЕНИЯ СОТРУДНИКАМИ")
        print("=" * 50)
        print("1. Преобразовать JSON в CSV")
        print("2. Добавить сотрудника в JSON")
        print("3. Добавить сотрудника в CSV")
        print("4. Найти сотрудника по имени")
        print("5. Фильтровать по языку программирования")
        print("6. Фильтровать по году рождения и вывести средний рост")
        print("7. Выйти из программы")
        print("=" * 50)

    def run(self) -> None:
        while True:
            self.display_menu()

            try:
                choice = input("Выберите действие (1-7): ").strip()

                if choice == '1':
                    self.json_to_csv()
                elif choice == '2':
                    self.add_employee_to_json()
                elif choice == '3':
                    self.add_employee_to_csv()
                elif choice == '4':
                    self.find_employee_by_name()
                elif choice == '5':
                    self.filter_by_language()
                elif choice == '6':
                    self.filter_by_year_and_height()
                elif choice == '7':
                    print("Выход из программы...")
                    break
                else:
                    print("Неверный выбор. Пожалуйста, выберите от 1 до 7.")

            except KeyboardInterrupt:
                print("\n\nПрограмма прервана пользователем.")
                break
            except Exception as e:
                print(f"Произошла ошибка: {e}")

def create_sample_json():
    sample_data = [
    {
        "name": "John Smith",
        "birthday": "02.10.1990",
        "height": 175,
        "weight": 76.5,
        "car": True,
        "languages": ["C++", "Python"]
    },
    {
        "name": "Alexey Alexeev",
        "birthday": "05.06.1986",
        "height": 197,
        "weight": 101.2,
        "car": False,
        "languages": ["Pascal", "Delphi"]
    },
    {
        "name": "Maria Ivanova",
        "birthday": "28.08.1998",
        "height": 165,
        "weight": 56.1,
        "car": True,
        "languages": ["C#", "C++", "C"]
    }
]

    with open('employees.json', 'w', encoding='utf-8') as f:
        json.dump(sample_data, f, ensure_ascii=False, indent=2)


if __name__ == "__main__":
    if not os.path.exists('employees.json'):
        create_sample_json()
        print("Создан пример JSON файла с данными сотрудников.")

    manager = EmployeeManager()
    manager.run()