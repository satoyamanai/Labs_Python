import os

def find_file_on_desktop(filename):
    desktop_path = os.path.join(os.path.expanduser('~'), 'Desktop')
    for root, dirs, files in os.walk(desktop_path):
        if filename in files:
            return os.path.abspath(os.path.join(root, filename))
    return None

# 输入要查找的文件名
filename_to_find = "occupation.txt"

# 查找文件
file_path = find_file_on_desktop(filename_to_find)

# 输出结果
if file_path:
    print(f"文件 '{filename_to_find}' 在桌面上找到，路径如下:")
    print(file_path)
else:
    print(f"文件 '{filename_to_find}' 未在桌面上找到.")
