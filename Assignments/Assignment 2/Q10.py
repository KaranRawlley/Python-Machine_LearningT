n = int(input('Enter the number '))
num = n
reverse = 0
while num>0:
    x = num%10
    reverse = (reverse*10) + x
    num = num//10

if n==reverse:
    print('Entered number is a palindrome ')
    print(n,'<=>',reverse)    
else:
    print('Entered number is not a palindrome ')
    print(n,'<=>',reverse)    
    