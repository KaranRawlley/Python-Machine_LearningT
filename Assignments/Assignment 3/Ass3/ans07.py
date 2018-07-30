a=input('Enter a string to arrange it in alphabetical order: ')
for i in range(len(a)-1):
    for j in range(len(a)-i-1):
        if a[j]>a[j+1]:
            temp=a[j]
            a = a[:j] + a[j+1] + a[j + 1:]
            a = a[:j+1] + temp + a[j + 2:]
            
print(a)