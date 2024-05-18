numbers = [1, 2, 3, 4, 5]
sum_numbers = sum(numbers)
count = len(numbers)

while True:
    new_number = int(input("Введите число (для завершения введите 0): "))
    if new_number == 0:
        break
    numbers.append(new_number)
    sum_numbers += new_number
    count += 1
    average = sum_numbers / count
    print("Среднее значение этих", count, "чисел равно {:.5f}".format(average))
