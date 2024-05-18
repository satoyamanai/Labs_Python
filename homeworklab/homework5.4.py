def reverse_dictionary(dict_items):
    reversed_dict = {}
    for number, string in dict_items:
        reversed_dict[string] = number
    return reversed_dict
original_dict = {
    1: "one",
    2: "two",
    3: "three",
    4: "four"
}

dict_items = original_dict.items()

reversed_dict = reverse_dictionary(dict_items)

print("Обратный словарь:")
print(reversed_dict)