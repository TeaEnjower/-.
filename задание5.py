# решение с помощью рекурсии

def move(n, x, y):
    if n == 1:
        print('нужно переложить диск' ,n, 'со стержня номер -', x, 'на стержень номер -', y)
    else:
        move(n - 1, x, 6 - x - y)
        print('нужно переложить диск' ,n, 'со стержня номер -', x, 'на стержень номер - ' ,y)
        move(n - 1, 6 - x - y, y)


a = int(input('Введите количество дисков: '))
x = int(input('Введите с какого стержня перекладываются диски: '))
y = int(input('Введите на какой стержень перекладываются диски: '))
move(a, x, y)