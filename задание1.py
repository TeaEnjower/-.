class MyClass:
    def __init__(self, var1, var2):
        self.var1 = var1
        self.var2 = var2

    def display(self):
        print("Переменная 1:", self.var1)
        print("Переменная 2:", self.var2)

    def change_vars(self, new_var1, new_var2):
        self.var1 = new_var1
        self.var2 = new_var2

    def sum_vars(self):
        return self.var1 + self.var2

    def max_var(self):
        return max(self.var1, self.var2)


my_object = MyClass(5, 10)
my_object.display()

my_object.change_vars(3, 7)
my_object.display()

print("Сумма переменных:", my_object.sum_vars())
print("Наибольшее значение:", my_object.max_var())