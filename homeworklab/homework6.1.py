def write_numbers_to_file(numbers, filename):
    with open(filename, 'w') as file:
        for number in numbers:
            file.write(str(number) + '\n')

def process_numbers_in_file(filename):
    try:
        with open(filename, 'r') as file:
            numbers = [float(line.strip()) for line in file.readlines()]
            total_sum = sum(numbers)
            max_value = max(numbers)
            min_value = min(numbers)

        with open(filename, 'a') as file:
            file.write(f"Сумма: {total_sum}\n")
            file.write(f"Максимум: {max_value}\n")
            file.write(f"Минимум: {min_value}\n")
    except FileNotFoundError:
        print("Файл не найден.")
    except Exception as e:
        print("Ошибка при чтении файла:", e)
    # Ввод чисел с клавиатуры


numbers_input = input("Введите числа через пробел: ").split()
numbers = [float(number) for number in numbers_input]

write_numbers_to_file(numbers, 'numbers.txt')

process_numbers_in_file('numbers.txt')
