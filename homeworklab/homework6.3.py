import os
print(os.getcwd())
def read_seating_data(filename):
    try:
        desktop_path = os.path.join(os.path.expanduser('~'), 'Desktop')
        file_path = os.path.join(desktop_path, filename)

        with open(file_path, 'r') as file:
            rows = [line.strip() for line in file.readlines()]
            return rows
    except FileNotFoundError:
        print("Файл не найден.")
        return []
    except Exception as e:
        print("Ошибка при чтении файла:", e)
        return []

def show_seating_info(seating_data):
    total_places = 0
    free_places_all = 0

    for i, row in enumerate(seating_data, start=1):
        total_places += len(row)
        free_places = row.count('0')
        free_places_all += free_places
        print(f'На ряду номер {i}: {free_places} свободных мест')

    print(f'Общее количество мест в зале: {total_places}')
    print(f'Общее количество свободных мест в зале: {free_places_all}')

    try:
        row_num = int(input("Введите номер ряда: ")) - 1
        seat_num = int(input("Введите номер места: ")) - 1

        if seating_data[row_num][seat_num] == '0':
            print('Данное место свободно')
        elif seating_data[row_num][seat_num] == '1':
            print('Данное место занято')
        else:
            print('Некорректные данные о месте')
    except IndexError:
        print("Введен некорректный номер ряда или места")
    except ValueError:
        print("Некорректный формат ввода. Введите целые числа.")

# Чтение данных о занятости мест из файла
seating_data = read_seating_data('Kino.txt')

# Отображение информации о занятости мест
show_seating_info(seating_data)