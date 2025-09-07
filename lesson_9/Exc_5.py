from tabulate import tabulate

def print_low_grades_table(filename):
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            low_grades = []

            for line_num, line in enumerate(file, 1):
                data = line.strip().split()

                if len(data) >= 3:
                    try:
                        grade = int(data[-1])
                        if grade < 3:
                            name = ' '.join(data[:-1])
                            low_grades.append([name, grade])
                    except ValueError:
                        print(f"⚠️ Ошибка в строке {line_num}: оценка не является числом")

            if low_grades:
                headers = ["№", "Фамилия и имя", "Оценка", "Статус"]
                table_data = []

                for i, (name, grade) in enumerate(low_grades, 1):
                    status = "❌ Неудовлетворительно" if grade == 2 else "⚠️ Плохо"
                    table_data.append([i, name, grade, status])

                print("📊 Учащиеся с оценкой меньше 3 баллов")
                print("=" * 60)
                print(tabulate(table_data, headers=headers, tablefmt="grid", stralign="left"))
                print(f"\nВсего найдено: {len(low_grades)} ученик(ов)")
            else:
                print("✅ Отлично! Учащихся с оценкой меньше 3 баллов не найдено")

    except FileNotFoundError:
        print("❌ Ошибка: Файл не найден!")

print_low_grades_table("students.txt")