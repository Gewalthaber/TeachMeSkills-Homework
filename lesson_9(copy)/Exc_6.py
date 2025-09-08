import re

def find_numbers_in_file(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        content = file.read()

    number_strings = re.findall(r'-?\d+\.?\d*', content)

    total = 0
    for num_str in number_strings:
        try:
            if '.' in num_str:
                total += float(num_str)
            else:
                total += int(num_str)
        except ValueError:
            continue

    return total

numbers_sum = find_numbers_in_file("numbers.txt")
print(f"Сумма всех чисел: {numbers_sum}")