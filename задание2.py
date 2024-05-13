from math import floor
from timeit import default_timer
import time
'''Реализуйте алгоритмы сужения области:
бинарный поиск (https://ru.wikipedia.org/wiki/%D0%94%D0%B2%D0%BE%D0%B8%D1%87%D0%BD%D1%8B%D0%B9_%D0%BF%D0%BE%D0%B8%D1%81%D0%BA)
метод золотого сечения (https://ru.wikipedia.org/wiki/%D0%9C%D0%B5%D1%82%D0%BE%D0%B4_%D0%B7%D0%BE%D0%BB%D0%BE%D1%82%D0%BE%D0%B3%D0%BE_%D1%81%D0%B5%D1%87%D0%B5%D0%BD%D0%B8%D1%8F)
интерполирующий поиск (https://ru.wikipedia.org/wiki/%D0%98%D0%BD%D1%82%D0%B5%D1%80%D0%BF%D0%BE%D0%BB%D1%8F%D1%86%D0%B8%D0%BE%D0%BD%D0%BD%D1%8B%D0%B9_%D0%BF%D0%BE%D0%B8%D1%81%D0%BA)'''
f = open("pi-10million.txt")
fs = f.readline(100)
LS = sorted([int(i) for i in range(1, 10000000)])
def Bin_search(numbers, num):
    left = 0
    right = len(numbers)
    while left < right:
        mid = (left + right) // 2
        if num == numbers[mid]:
            return mid
        elif num < numbers[mid]:
            right = mid
        else:
            left = mid


def goldenCutSearch(num, key):
    phi = 0.5*(1 + 5 ** 0.5)
    a = 0
    b = len(num) - 1
    while b - a >= 1:
        x1 = int(b - (b - a)//phi)
        x2 = int(a + (b - a)//phi)
        A = num[a : x2 + 1]
        B = num[x1 : b + 1]
        if key in A:
            b = x2
        elif key in B:
            a = x1
        else:
            print('goldenCutSearch: not found')
            return
    return a

def interpolating_search(arr, x):
    """
    Интерполяционный поиск элемента в отсортированном массиве.

    :param arr: Отсортированный массив.
    :param x: Искомое число.
    :return: Индекс искомого числа в массиве, или None, если число не найдено.
    """
    l = 0
    u = len(arr) - 1

    while l <= u:
        i = l + ((u - l) * (x - arr[l]) // (arr[u] - arr[l]))

        if x == arr[i]:
            return i
        elif x < arr[i]:
            u = i - 1
        else:
            l = i + 1

t = default_timer()
print(Bin_search(LS, 9999999))
print('{:.10f}'.format(default_timer() - t))

t = default_timer()
print(goldenCutSearch(LS, 9999999))
print('{:.10f}'.format(default_timer() - t))

t = default_timer()
print(interpolating_search(LS, 9999999))
print('{:.10f}'.format(default_timer() - t))