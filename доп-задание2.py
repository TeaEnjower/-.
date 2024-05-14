def cut_table(table):
    ind_row, ind_col = 0, 0
    max_sum = -10**20
    max_num = -10**20
    for ind, row in enumerate(table):
        if row.count(0) > max_num:
            max_num, ind_row = row.count(0), ind
    table_rev = [list(i) for i in zip(*table)]
    for ind, col in enumerate(table_rev):
        if sum(col) > max_sum:
            max_sum, ind_col = sum(col), ind
    return f'Максимально нулей в строчке: {ind_row+1}, Максимальная сумма в столбце: {ind_col+1}'


def do_table(n, *args):
    t = [[0]*n for _ in range(n)]
    i, j = 0, 0

    for k in args:
        t[i][j] = k
        if i <= j + 1 and i + j < n - 1:
            j += 1
        elif i < j and i + j >= n - 1:
            i += 1
        elif i >= j and i + j > n - 1:
            j -= 1
        elif i > j + 1 and i + j <= n - 1:
            i -= 1
    return t


t = do_table(3, 1, 4, 5, 6, 7, 4, 2, 3, 5)
print(*t, sep='\n')
print()
print(cut_table(t))