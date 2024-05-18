import os
print(os.getcwd())

def read_matrix_element(filename, index):
    desktop_path = os.path.join(os.path.expanduser('~'), 'Desktop')
    file_path = os.path.join(desktop_path, filename)

    with open(file_path, 'r') as file:
        line = file.readlines()[index]
        element = int(line.split()[index])
    return element

element_matrix1 = read_matrix_element("matrix1.txt", 0)  # 选择第一个元素
element_matrix2 = read_matrix_element("matrix2.txt", 0)  # 选择第一个元素

product_element = element_matrix1 * element_matrix2

print(f"{element_matrix1} 0 0")
print(f"0 {element_matrix2} 0")
print(f"0 0 {product_element}")