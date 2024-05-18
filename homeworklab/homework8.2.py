class Polynomial:
    def __init__(self, degree, coefficients):
        self.degree = degree
        self.coefficients = coefficients

    def calculate_value(self, x):
        value = 0
        for i in range(self.degree + 1):
            value += self.coefficients[i] * (x ** i)
        return value

    def add_polynomial(self, other_polynomial):
        new_degree = max(self.degree, other_polynomial.degree)
        new_coefficients = [0] * (new_degree + 1)

        for i in range(self.degree + 1):
            new_coefficients[i] += self.coefficients[i]

        for i in range(other_polynomial.degree + 1):
            new_coefficients[i] += other_polynomial.coefficients[i]

        return Polynomial(new_degree, new_coefficients)

    def subtract_polynomial(self, other_polynomial):
        new_degree = max(self.degree, other_polynomial.degree)
        new_coefficients = [0] * (new_degree + 1)

        for i in range(self.degree + 1):
            new_coefficients[i] += self.coefficients[i]

        for i in range(other_polynomial.degree + 1):
            new_coefficients[i] -= other_polynomial.coefficients[i]

        return Polynomial(new_degree, new_coefficients)

    def multiply_polynomial(self, other_polynomial):
        new_degree = self.degree + other_polynomial.degree
        new_coefficients = [0] * (new_degree + 1)

        for i in range(self.degree + 1):
            for j in range(other_polynomial.degree + 1):
                new_coefficients[i + j] += self.coefficients[i] * other_polynomial.coefficients[j]

        return Polynomial(new_degree, new_coefficients)

    def display_polynomial(self):
        print("Polynomial:")
        for i in range(self.degree + 1):
            print(f"{self.coefficients[i]}x^{i}", end=" ")
        print("\n")


# 例子
poly1 = Polynomial(2, [1, 2, 3])  # 多项式1，阶数为2，系数为1, 2, 3
poly2 = Polynomial(1, [2, 1])  # 多项式2，阶数为1，系数为2, 1

# 显示多项式1，2
poly1.display_polynomial()
poly2.display_polynomial()

# 多项式1在x=2处的值
x_value = 2
print(f"Value of Polynomial 1 at x={x_value}: {poly1.calculate_value(x_value)}")

# 计算和
sum_poly = poly1.add_polynomial(poly2)
sum_poly.display_polynomial()

# 计算差值
diff_poly = poly1.subtract_polynomial(poly2)
diff_poly.display_polynomial()

# 计算乘积
product_poly = poly1.multiply_polynomial(poly2)
product_poly.display_polynomial()