class TwoVariables:
    def __init__(self, var1, var2):
        self.var1 = var1
        self.var2 = var2

    def display_variables(self):
        print(f"Variable 1: {self.var1}")
        print(f"Variable 2: {self.var2}")

    def modify_variables(self, new_var1, new_var2):
        self.var1 = new_var1
        self.var2 = new_var2

    def sum_variables(self):
        return self.var1 + self.var2

    def max_variable(self):
        return max(self.var1, self.var2)


# example of creating a class
variables_instance = TwoVariables(7, 15)

# display the value of a variable
variables_instance.display_variables()

# change the value of variable
variables_instance.modify_variables(10, 20)
variables_instance.display_variables()

# get sum
print("Sum of variables:", variables_instance.sum_variables())

# find max
print("Max variable value:", variables_instance.max_variable())
