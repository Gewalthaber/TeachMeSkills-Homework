import re

def replace_fio_in_text(text):
    pattern = r'\b[А-ЯЁ][а-яё]*(?:[- ][А-ЯЁ][а-яё]*)*\s+[А-ЯЁ][а-яё]*\s+[А-ЯЁ][а-яё]*\b'
    return re.sub(pattern, 'N', text)

def process_file(input_file, output_file):
    try:
        with open(input_file, 'r', encoding='utf-8') as f:
            text = f.read()

        result = replace_fio_in_text(text)

        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(result)

        print(f"Файл успешно обработан. Результат сохранен в {output_file}")
        return result

    except FileNotFoundError:
        print(f"Ошибка: файл {input_file} не найден")
        return None
    except Exception as e:
        print(f"Произошла ошибка: {e}")
        return None

def replace_fio_in_text_improved(text):
    patterns = [
        r'\b[А-ЯЁ][а-яё]*-[А-ЯЁ][а-яё]* [А-ЯЁ][а-яё]* [А-ЯЁ][а-яё]*\b',
        r'\b[А-ЯЁ][а-яё]* [А-ЯЁ][а-яё]* [А-ЯЁ][а-яё]*\b',
        r'\b[А-ЯЁ][а-яё]* [А-ЯЁ][а-яё]* [А-ЯЁ][а-яё]* [А-ЯЁ][а-яё]*\b'
    ]

    for pattern in patterns:
        text = re.sub(pattern, 'N', text)
    return text

if __name__ == "__main__":
    input_text = """Подсудимая Эверт-Колокольцева Елизавета Александровна
в судебном заседании вину инкриминируемого
правонарушения признала в полном объёме и суду показала,
что 14 сентября 1876 года, будучи в состоянии алкогольного
опьянения от безысходности, в связи с состоянием здоровья
позвонила со своего стационарного телефона в полицию,
сообщив о том, что у неё в квартире якобы заложена бомба.
После чего приехали сотрудники полиции, скорая
и пожарные, которым она сообщила, что бомба — это она."""

    print("Исходный текст:")
    print(input_text)
    print("\n" + "=" * 50)

    result = replace_fio_in_text_improved(input_text)

    print("Обработанный текст:")
    print(result)