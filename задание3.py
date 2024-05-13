n = int(input('Enter the number of cows:'))

if n%100 > 10 and n%100 < 20:
    print ('На лугу пасётся', n, 'коров')
elif n%10 == 0 or n%10 > 4:
     print ('На лугу пасётся', n, 'коров')
elif n%10 == 1:
     print ('На лугу пасётся', n, 'корова')
else:
     print ('На лугу пасётся', n, 'коровы')
        
del n