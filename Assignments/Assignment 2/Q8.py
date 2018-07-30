num = int(input('Enter a number '))
n = num
sum = 0

while n>0:
    c = int(n % 10)
    sum+=c
    n=int(n/10)
    
print('Sum of the digits of the number',num,'is',sum)     
    
    
    
    