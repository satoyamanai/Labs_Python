def sum_of_digits():
    while True:
        user_input = input("Введите целые числа (для завершения введите 'done'): ")
        clean_input = ''.join(filter(str.isdigit, user_input))
        if clean_input:
            numbers = list(map(int, clean_input))
            total_sum = sum(numbers)
            print("Сумма введенных цифр:", total_sum)
            break
        else:
            print("Некорректный ввод. Пожалуйста, введите цифры.")

sum_of_digits()