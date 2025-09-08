import re


def main():
    filename = input("Введите название текстового файла: ")

    try:
        with open('stop_words.txt', 'r', encoding='utf-8') as stop_file:
            stop_words = stop_file.read().split()

        with open(filename, 'r', encoding='utf-8') as file:
            text = file.read()

        for word in stop_words:
            pattern = re.compile(re.escape(word), re.IGNORECASE)

            def replace_with_stars(match):
                matched_text = match.group(0)
                return '*' * len(matched_text)

            text = pattern.sub(replace_with_stars, text)
        print(text)

    except FileNotFoundError:
        print("Ошибка: файл не найден")
    except Exception as e:
        print(f"Произошла ошибка: {e}")


if __name__ == "__main__":
    main()