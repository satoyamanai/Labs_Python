def transform_string(s):
    upper_count = sum(1 for char in s if char.isupper())
    lower_count = sum(1 for char in s if char.islower())

    if upper_count > lower_count:
        return s.upper()
    elif lower_count > upper_count:
        return s.lower()
    else:
        return s


input_string = input("Введите строку: ")

transformed_string = transform_string(input_string)
print("Преобразованная строка:", transformed_string)