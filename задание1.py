a = int(input("Enter a number: "))

if a//1000 != 0 or a//100 != 0 or a == 0:       # the number is divided entirely by 1000 or 100 and is not equal to zeros or the number is zero     
    d = a%100                                   # the remainder of the division, d - the first part of the number
    c0 = a//100                                 # the integer part of the number a when divided by 100
    c1 = c0//10                                 # the integer part of the number a when divided by 10
    c2 = c0%10 * 10                             
    c = c1 + c2                                 # c - the second part of the number
    if d == c:
        print(1)
    else:
        print(0)
        
else:
    print(0)

    
del a, d, c0, c1, c2, c