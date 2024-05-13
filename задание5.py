print ('if u want to stop - enter "0"')
a = int(input('Enter an integer number:'))
c1 =  0
d = 0                                      #even numbers
c2 = 0                                     #odd numbers

sum = 0
mul = 1                                    #multiplication
max = 0
min = a

while a != 0:
    c1 = c1+1 
    sum = sum + a
    mul = mul*a
    if max < a:
        max = a 
    if min > a:
        min = a
    if a%2 == 0:
        d = d+1 
    else:
        c2 = c2+1 
    a = int(input('Enter an integer number:'))
m = sum/c1 


print('')
print ('Number of sequence members:', c1)
print ('The sum of the entered numbers:', sum)
print ('The product of the entered numbers:', mul)
print ('The average value of the entered numbers:', m)
print ('The maximum of the entered numbers:', max)
print ('The minimum of the entered numbers:', min)
print ('Number of even numbers:', d)
print('Number of odd numbers:', c2)


del a, c1, d, c2