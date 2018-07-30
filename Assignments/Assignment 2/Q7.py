a = int(input('Enter the first digit '))
b = int(input('Enter the Second digit '))
c = int(input('Enter the Third digit '))
l = [a,b,c]

for i in range(3):
    for j in range(3):
        for k in range(3):
            if i!=j!=k:
                print(l[i],l[j],l[k])
