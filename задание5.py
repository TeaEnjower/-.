def getInput():
    return input('Enter smth:')


def testInput(x):
    if type (x) == int or type(x) == float:
        return ('True')
    else:
        return ('False')

def strToInt(x):
    return int(x)


def printInt(x):
    print(x)


smth = getInput()

if testInput(smth):
    printInt(strToInt(smth))

del smth

