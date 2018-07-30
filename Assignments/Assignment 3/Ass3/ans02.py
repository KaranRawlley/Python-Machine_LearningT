def gcd1(la,lb):
    mul=1
    for i in la:
        if i in lb:
            mul*=i
    return mul
    
def gcd(a,b):
    c=a
    d=b
    print(c,d)
    la=[]
    i=2
    while a>1 and i<=a:
        if a%i is 0:
            la.append(i)
            a=a//i
        else:
            i+=1
    print(la)
    lb=[]
    i=2
    while b>1 and i<=b:
        if b%i is 0:
            lb.append(i)
            b=b//i
        else:
            i+=1
    print(lb)
    if len(la)<len(lb):
        print('GCD is ',gcd1(la,lb))
    else:
        print('GCD is ',gcd1(lb,la))
    
x=int(input('Input first number'))
y=int(input('Input second number'))
gcd(x,y)