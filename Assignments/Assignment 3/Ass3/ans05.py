def fac(n):
    if n is 0:
        return 1
    else:
        return n*fac(n-1)
n=input('Enter the number whose factorial is to be found: ')
n=int(n)
print(fac(n))