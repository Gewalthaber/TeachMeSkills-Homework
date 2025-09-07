import re
from collections import Counter


def analyze_text_file(input_file, ):

    try:
        with open(input_file, 'r', encoding='utf-8') as file:
            text = file.read()
    except FileNotFoundError:
        print(f"Файл {input_file} не найден")
        return
    except Exception as e:
        print(f"Ошибка чтения: {e}")
        return

    words = re.findall(r'\b\w+\b', text.lower())
    total_words = len(words)
    unique_words = len(set(words))

    counter = Counter(words)
    duplicates = {word: count for word, count in counter.items() if count > 1}

    print(f"Всего слов: {total_words}")
    print(f"Уникальных слов: {unique_words}")
    print(f"Повторяющихся слов: {len(duplicates)}")
    print("\nПовторяющиеся слова:")

    for word, count in sorted(duplicates.items(), key=lambda x: x[1], reverse=True):
        print(f"{word}: {count}")

analyze_text_file("input_file.txt")

