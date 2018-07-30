def a():
    x=input('Enter first number: ')
    x=int(x)
    y=input('Enter second number: ')
    y=int(y)
    print('{} + {} = {}'.format(x,y,x+y))
def s():
    x=input('Enter first number: ')
    x=int(x)
    y=input('Enter second number: ')
    y=int(y)
    print('{} - {} = {}'.format(x,y,x-y))
def m():
    x=input('Enter first number: ')
    x=int(x)
    y=input('Enter second number: ')
    y=int(y)
    print('{} * {} = {}'.format(x,y,x*y))
def d():
    x=input('Enter first number: ')
    x=int(x)
    y=input('Enter second number: ')
    y=int(y)
    print('{} / {} = {}'.format(x,y,x/y))
c='y'
while c is 'y' or c is 'Y':
    print('Select operation.\n1.Add\n2.Subtract\n3.Multiply\n4.Divide')
    c=input('Enter choice(1/2/3/4): ')
    if c is '1':
        a()
    elif c is '2':
        s()
    elif c is '3':
        m()
    elif c is '4':
        d()    
    c=input('Want to do another operation?(y/n)')    