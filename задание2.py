import nympy as np
def maxCommonSequence(first, second):
    commonSequences = []
    i = 0
    while i < len(first) - 1:
        j = 0
        while j < len(second) - 1:
            if first[i] == second[j]:
                if first[i + 1] == second[j + 1]:
                    commonSequences.append(first[i])
                    commonSequences[-1] += first[i + 1]
                    i1 = i + 2
                    j1 = j + 2
                    while (i1 < len(first)) and (j1 < len(second)):
                        if first[i1] == second[j1]:
                            commonSequences[-1] += first[i1]
                        else:
                            break
                        i1 += 1
                        j1 += 1
            j += 1
        i += 1
    if len(commonSequences) == 0:
        return ''
    else:
        mx = 0
        for i in range(1, len(commonSequences)):
            if len(commonSequences[mx]) < len(commonSequences[i]):
                mx = i
        return commonSequences[mx]


def maxCommonSequence_Dynamically(first, second):
    first.insert(0, '1')
    second.insert(0, '2')
    E = np.zeros((len(first) + 1, len(second) + 1))
    H = np.zeros((len(first) + 1, len(second) + 1))
    for j in range(1, len(second) + 1):
        for i in range(1, len(first) + 1):
            if first[i - 1] == second[j - 1]:
                E[i][j] = 1 + E[i - 1][j - 1]
                H[i][j] = -1
            else:
                if E[i - 1][j] >= E[i][j - 1]:
                    E[i][j] = E[i - 1][j]
                    H[i][j] = 2  # l
                else:
                    E[i][j] = E[i][j - 1]
                    H[i][j] = 1  # u

    i = len(first)
    j = len(second)
    commonSequences = []
    commonSequence = ''
    while H[i][j] != 0:
        if H[i][j] == -1:
            commonSequence += first[i - 1]
            i -= 1
            j -= 1
        elif H[i][j] == 1:
            if commonSequence != '':
                commonSequence
                commonSequences.append(commonSequence)
                commonSequence = ''
            j -= 1
        elif H[i][j] == 2:
            if commonSequence != '':
                commonSequences.append(commonSequence)
                commonSequence = ''
            i -= 1
    if len(commonSequences) == 0:
        return
    else:
        mx = 0
        for i in range(1, len(commonSequences)):
            if len(commonSequences[mx]) < len(commonSequences[i]):
                mx = i
        CS = list(commonSequences[mx])
        CS.reverse()
        CS = ''.join(CS)
        return CS


print(maxCommonSequence(list(str(input('Введите первую последовательность: '))),
                        list(str(input('Введите вторую последовательность: ')))))

print(maxCommonSequence_Dynamically(list(str(input('Введите первую последовательность: '))),
                                    list(str(input('Введите вторую последовательность: ')))))
