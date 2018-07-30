x=input('Enter a number in decimal form: ')
x=int(x)
str=''
while x>0:
    if x%2 is 0:
        str+='0'
        x//=2
    else:
        str+='1'
        x//=2
str=str[::-1]
print('Binary form: ',str)
str=str[::-1]
if len(str)%3 is 1:
    str+='00'
elif len(str)%3 is 2:
    str+='0'
str=str[::-1]
l=[]
l2=[]
for i in range(len(str)):
    l.append(str[i])
check=None
for i in range(0,len(l),3):
    check=l[i]+l[i+1]+l[i+2]
    l2.append(check)
oct=0
for i in range(len(l2)):
    if l2[i]=='000':
        oct=oct*10+0
    elif l2[i]=='001':
        oct=oct*10+1
    elif l2[i]=='010':
        oct=oct*10+2
    elif l2[i]=='011':
        oct=oct*10+3
    elif l2[i]=='100':
        oct=oct*10+4
    elif l2[i]=='101':
        oct=oct*10+5
    elif l2[i]=='110':
        oct=oct*10+6
    elif l2[i]=='111':
        oct=oct*10+7
        
print('Octal form: ',oct)





str=str[::-1]
if len(str)%4 is 1:
    str+='000'
elif len(str)%4 is 2:
    str+='00'
elif len(str)%4 is 3:
    str+='0'
str=str[::-1]
l=[]
l2=[]
for i in range(len(str)):
    l.append(str[i])
check=None
for i in range(0,len(l),4):
    check=l[i]+l[i+1]+l[i+2]+l[i+3]
    l2.append(check)
oct=''
for i in range(len(l2)):
    if l2[i]=='0000':
        oct+='0'
    elif l2[i]=='0001':
        oct+='1'
        print('added 1')
    elif l2[i]=='0010':
        oct=oct+'2'
    elif l2[i]=='0011':
        oct=oct+'3'
    elif l2[i]=='0100':
        oct+='4'
    elif l2[i]=='0101':
        oct+='5'
    elif l2[i]=='0110':
        oct+='6'
    elif l2[i]=='0111':
        oct=oct+'7'
    elif l2[i]=='0111':
        oct=oct+'7'
    elif l2[i]=='1000':
        oct=oct+'8'
    elif l2[i]=='1001':
        oct=oct+'9'
    elif l2[i]=='1010':
        oct=oct+'A'
    elif l2[i]=='1011':
        oct=oct+'B'
    elif l2[i]=='1100':
        oct=oct+'C'
    elif l2[i]=='1101':
        oct=oct+'D'
    elif l2[i]=='1110':
        oct=oct+'E'
    elif l2[i]=='1111':
        oct=oct+'F'
print('Hexadecimal form: ',oct)