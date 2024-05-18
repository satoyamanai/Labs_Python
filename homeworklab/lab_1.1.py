x = 2
print("Шаг 1:")
print("x =", x, ", тип:", type(x))

x += 3
print("\nШаг 2:")
print("x =", x, ", тип:", type(x))

x = (x + 1) / 2
print("\nШаг 3:")
print("x =", x, ", тип:", type(x))

x = x + 1 / 2
print("\nШаг 4:")
print("x =", x, ", тип:", type(x))

x = x < 5
print("\nШаг 5:")
print("x =", x, ", тип:", type(x))

x = str(x)
print("\nШаг 6:")
print("x =", x, ", тип:", type(x))
