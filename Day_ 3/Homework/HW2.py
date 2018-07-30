n =int(input('Enter the number of family members (min 5) '))

l =[]

for i in range(n):
    a = input('Enter name of the member ')
    b = int(input('Enter the age of the member '))
    d = dict(name=a,age=b)
    l.append(d)
    
ch =2
while ch==2:
    print('Search by \n1.NAME or 2.AGE ')
    choice = int(input('Enter your choice'))
    if choice == 1:
        s=input('Enter the name you wanna search ')
        for i in range(n):
            if s==l[i]['name']:
                print(l[i])
    if choice == 2:
        s=int(input('Enter the age of the member you wanna search '))
        for i in range(n):
            if s==l[i]['age']:
                print(l[i])              
    x=int(input('If want to search again press 2(if not press any number)'))   
    ch=x       
                 

            
          
          
              