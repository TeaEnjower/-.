def ballOnStairs(init, n, step, show = False):
    if init >= n:
        return 0
    if n // 2 ** step < 1:
        return min(n // 16, n - init)
    routes = min(n // 2 ** step, n - init)
    for i in range(init + 1, min(init + n // 2 ** step, n) + 1):
        if show: print(init, '->', i)
        routes += ballOnStairs(i, n, step + 1, show)
    return routes

ballOnStairs(1, 4, 1, show = True)

print(ballOnStairs(1, int(input('Введите n: ')), 1, show = (True if input('Показывать все возможные ходы? (y/n) ') == 'y' else False)))