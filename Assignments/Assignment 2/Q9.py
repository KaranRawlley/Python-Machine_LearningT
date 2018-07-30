num = int(input('Enter a number '))
n = num
count = 0

while n>0:
    n=int(n/10)
    count+=1
    
print('Number of digits in',num,'is',count)     
    
    
    
    