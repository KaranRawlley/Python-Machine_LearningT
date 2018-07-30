upperRange = int(input('Enter the Upper range '))
lowerRange = int(input('Enter the Lower range '))

di = int(input('Enter the number whose factors you want '))

for i in range(lowerRange,upperRange,1):
    if i%di==0:
        print(i)
    else:
        continue    