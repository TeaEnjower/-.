# Так можно добавлять картинки

from IPython.display import Image # вызов из библиотеки определённой функции
Image("операции.png")              # вызов функции и передача ей в качестве аргумента пути к файлу 

# (в данном случае фаил находится в той же папке)


try:
    print('Выберите операцию:')
    print('1) сложение')
    print('2) умножение')
    print('3) вычитание')
    print('4) деление (только целочисленное): ', end = '')
    task = int(input())
    a, b = input('Введите два числа в произвольных ' +
                 'системах счисления через пробел: ').split()
    a_base, b_base = map(int, input('Введите системы счисления ' +
                                    'чисел через пробел: ').split())
    a_10 = int(convert_base_R(a, from_base = a_base))
    b_10 = int(convert_base_R(b, from_base = b_base))
    if b_10 == 0 and task == 4:
        raise ZeroDivisionError
    c_base = int(input('Введите систему счисления результата: '))
    if task == 1:
        print('Результат:', convert_base_R(a_10 + b_10, to_base = c_base))
    elif task == 2:
        print('Результат:', convert_base_R(a_10 * b_10, to_base = c_base))
    elif task == 3:
        print('Результат:', convert_base_R(a_10 - b_10, to_base = c_base))
    elif task == 4:
        print('Результат:', convert_base_R(a_10 // b_10, to_base = c_base))
except ValueError:
    print('Ошибка введенных данных.')
    ERRMSG()
except ZeroDivisionError:
    print('Ошибка деления на ноль.')
    ERRMSG()
except IndexError:
    print('Ошибка индекса.')
    ERRMSG()