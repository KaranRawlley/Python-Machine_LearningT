f=0
s=1
n=input('Enter the series length ');
n=int(n)
i=0
print('0')
print('1')
for i in range(n):
    sum=f+s
    print(sum)
    f=s
    s=sum