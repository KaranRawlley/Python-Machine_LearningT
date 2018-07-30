first=0
second=1
n=input('Enter upto how many terms you want to print the series: ')
n=int(n)
def fib(n,first,second):
    if n is 0:
        return
    else:
        print(first,'\t',end='')
        sum=first+second
        first=second
        second=sum
        fib(n-1,first,second)
fib(n,0,1)