import os
import shutil

os_name = os.name
print(f"Имя ОС: {os_name}")

current_dir = os.getcwd()
print(f"Путь текущей директории: {current_dir}")


def get_size_in_gb(size_bytes):
    return size_bytes / (1024 ** 3)


def rename_random_file(folder_path, folder_name):
    try:
        files = [f for f in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, f))]
        if files:
            old_name = files[0]  # берем первый файл
            name, ext = os.path.splitext(old_name)
            new_name = f"{name}_renamed{ext}"

            old_path = os.path.join(folder_path, old_name)
            new_path = os.path.join(folder_path, new_name)

            os.rename(old_path, new_path)
            print(f"Файл '{old_name}' был переименован в '{new_name}' в папке '{folder_name}'")
            return True
    except Exception as e:
        print(f"Ошибка при переименовании файла в папке '{folder_name}': {e}")
    return False


def find_files():
    folder_name_txt = "Папка TXT"
    folder_name_json = "Папка JSON"
    folder_name_csv = "Папка CSV"

    folder_path_txt = os.path.join(current_dir, folder_name_txt)
    folder_path_json = os.path.join(current_dir, folder_name_json)
    folder_path_csv = os.path.join(current_dir, folder_name_csv)

    folders = {
        folder_name_txt: folder_path_txt,
        folder_name_json: folder_path_json,
        folder_name_csv: folder_path_csv
    }

    for folder_name, folder_path in folders.items():
        try:
            os.mkdir(folder_path)
            print(f"Папка '{folder_name}' создана")
        except FileExistsError:
            print(f"Папка '{folder_name}' уже существует")

    stats = {
        folder_name_txt: {'count': 0, 'total_size': 0},
        folder_name_json: {'count': 0, 'total_size': 0},
        folder_name_csv: {'count': 0, 'total_size': 0}
    }

    for filename in os.listdir(current_dir):
        file_path = os.path.join(current_dir, filename)

        if filename.endswith(".txt") and os.path.isfile(file_path):
            destination_path = os.path.join(folder_path_txt, filename)
            try:
                file_size = os.path.getsize(file_path)
                shutil.move(file_path, destination_path)
                print(f"Файл '{filename}' перемещен в '{folder_name_txt}'")
                stats[folder_name_txt]['count'] += 1
                stats[folder_name_txt]['total_size'] += file_size
            except Exception as e:
                print(f"Ошибка при перемещении файла '{filename}': {e}")

        elif filename.endswith(".json") and os.path.isfile(file_path):
            destination_path = os.path.join(folder_path_json, filename)
            try:
                file_size = os.path.getsize(file_path)
                shutil.move(file_path, destination_path)
                print(f"Файл '{filename}' перемещен в '{folder_name_json}'")
                stats[folder_name_json]['count'] += 1
                stats[folder_name_json]['total_size'] += file_size
            except Exception as e:
                print(f"Ошибка при перемещении файла '{filename}': {e}")

        elif filename.endswith(".csv") and os.path.isfile(file_path):
            destination_path = os.path.join(folder_path_csv, filename)
            try:
                file_size = os.path.getsize(file_path)
                shutil.move(file_path, destination_path)
                print(f"Файл '{filename}' перемещен в '{folder_name_csv}'")
                stats[folder_name_csv]['count'] += 1
                stats[folder_name_csv]['total_size'] += file_size
            except Exception as e:
                print(f"Ошибка при перемещении файла '{filename}': {e}")

    print("\n" + "=" * 50)
    print("СТАТИСТИКА ПЕРЕМЕЩЕНИЯ ФАЙЛОВ:")
    print("=" * 50)

    for folder_name, data in stats.items():
        if data['count'] > 0:
            size_gb = get_size_in_gb(data['total_size'])
            print(f"В папке '{folder_name}' перемещено {data['count']} файлов, "
                  f"их суммарный размер - {size_gb:.2f} гигабайт")
        else:
            print(f"В папке '{folder_name}' файлов не найдено")

    print("=" * 50)
    print("\nПЕРЕИМЕНОВАНИЕ ФАЙЛОВ:")
    print("=" * 50)

    for folder_name, folder_path in folders.items():
        if os.path.exists(folder_path) and any(os.path.isfile(os.path.join(folder_path, f))
                                               for f in os.listdir(folder_path)):
            rename_random_file(folder_path, folder_name)

    print("=" * 50)

find_files()
