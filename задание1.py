x = input()
y = input()

if bool(x.isdigit()) and (y.isdigit()):                    # проверка типа введенных данных, с помощью логической переменной
    x = int(x)
    y = int(y)
    print ('Сумма введенных чисел:', x + y)
else:
    print ('"Сумма" веденных элементов:', x + y)            # конкатенация