string = input()
length = len(string)
a = 0                                          # строчные элементы
A = 0                                          # заглавные элементы

for i in range(length):
    
    if string[i].islower():                    #возвращает True, если все алфавиты в строке являются строчными
        a += 1
    else:
        A += 1
print(A, a)

if A > a:
    print(string.upper())
elif A < a:
    print(string.lower())
else:
    print(string)