def HYPERgrasshopper(n):
    GH = [None] + ([0] * max(3, n))
    GH[1] = 1
    GH[2] = 1
    for i in range(3, n + 1):
        GH[i] = GH[i - 1] + GH[i - 2]
        if i % 3 == 0:
            GH[i] += GH[i // 3]
    return GH[n]
print('Количество способов достичь её:',HYPERgrasshopper(int(input('Введите конечную точку: '))))
