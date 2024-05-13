def a(x):                                                            # three-digit and positive, with 0 at the end
    return x > 0 and len(str(x)) == 3 and str(x)[2] == '0'


def b(x):                                                            # odd, divisible by 3 or by 5
    return x % 2 == 1 and (x % 3 == 0 or x % 5 == 0)


def c(x):                                                            # belongs to the segment of the numerical line [2, 6]  
    return x in range(200, 601)                                      # I think, in this case, the specified segment was meant, because three-digit numbers are considered


def d(x):                                                            # three-digit and all its digits are the same
    try:
        return len(str(x)) == 3 and (str(x)[0] == str(x)[1] == str(x)[2])
    except:
        return False
    

x = int(input('Enter a number: '))

print ('')
print ('1.', a(x))
print ('2.',b(x))
print ('3.',c(x))
print ('4.',d(x), '\n')

del x