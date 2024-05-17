def isSecondSequenceASubsequence(first, second):
    l, k = 0, 0
    j = 0
    i = 0
    while i < len(first):
        if first[i] == second[j]:
            k = i
            l += 1
            i += 1
            if j < len(second) - 1:
                j += 1
            elif l < len(second):
                return False
        else:
            i += 1
        if l == len(second):
            return True
    return False

print('Является ли вторая последовательность подпоследовательностью первой? Ответ:', isSecondSequenceASubsequence(str(input('Введите первую последовательность: ')), str(input('Введите вторую последовательность: '))))
