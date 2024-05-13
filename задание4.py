# with Cycle "for"

s = int(input('Enter an integer number:'))

for i in range(2, s+1):
    if s%i == 0:
        print(i)
        break

        
del s, i