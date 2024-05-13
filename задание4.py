def Positive():
    print ('positive')


def Negative():
    print ('negative')


def test():
    x = int(input('Enter an integer number:'))
    if x > 0:
        Positive()
    else:
        Negative()

    del x



test()