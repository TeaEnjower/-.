def kar():
    spis = []
    x = input('Введите первое число: ')
    spis.append(x)
    y = input('Введите второе число: ')
    spis.append(y)
    if len(x) <= 10 and len(y) <= 10:
        return (int(x))*(int(y))
    else:
        a = len(x)
        if a % 2 == 0:
            mid = a / 2
            xs, ys = str(x), str(y)
            
            x_list, y_list = [i for i in xs], [i for i in ys]
            
            first_halfX, second_halfX = x_list[: a//2], x_list[a//2 :]
            first_halfY, second_halfY = y_list[: a//2], y_list[a//2 :]
            
            xq, xw = ''.join(first_halfX),''.join(second_halfX)
            x1, x2 = int(xq), int(xw)
            yq,yw = ''.join(first_halfY), ''.join(second_halfY)
            y1, y2 = int(yq), int(yw)
        elif a % 2 == 1:
            mid = (a + 1) / 2
            xs, ys = str(x), str(y)
            x_list, y_list = [i for i in xs], [i for i in ys]
            
            x_list.append(0)
            y_list.append(0)
            
            first_halfX, second_halfX = x_list[: a // 2], x_list[a // 2 :]
            first_halfY, second_halfY = y_list[: a // 2], y_list[a // 2 :]
            
            second_halfX.pop()
            second_halfY.pop()
            xq, xw = ''.join(first_halfX),''.join(second_halfX)
            x1, x2 = int(xq), int(xw)
            yq,yw = ''.join(first_halfY), ''.join(second_halfY)
            y1, y2 = int(yq), int(yw)
    mult = x2 * y2 + ((x1 + x2) * (y1 + y2) - y1 * x1 - y2 * x2) * 10 ** mid + y1 * x1 * 10 ** (2 * mid)
    spis.append(mult)
    print(spis)
    kar()