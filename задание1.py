f = open("pi-10million.txt")
fs = f.readline()
def six_num(numbers, find):
    for i in range(10000000-5):
        if fs[i] == find and fs[i+1] == find and fs[i+2] == find and fs[i+3] == find and fs[i+4] == find and fs[i+5] == find:
            return (i, i+5)

def six_first(numbers):
    for i in range(1, 10000000-5):
        if fs[i] == '1' and fs[i+1] == '4' and fs[i+2] == '1' and fs[i+3] == '5' and fs[i+4] == '9' and fs[i+5] == '2':
            return (i, i+5)

def Telephone(numbers):
    for i in range(0, 10000000-5):
        if fs[i] == '8' and fs[i+1] == '9' and fs[i+2] == '9' and fs[i+3] == '3' and fs[i+4] == '9' and fs[i+5] == '2' and fs[i+6] == '7':
            return (i, i+5)
print(six_num(fs, '9'))
print(six_num(fs, '8'))
print(six_num(fs, '0'))
print(six_first(fs))
print(Telephone(fs))