print('******Area of Triangle******')
print('\n Enter the length of 3 sides of a TRIANGLE (one at a time) : \n')
a = input('Enter first side : ')
a = float(a)
b = input('Enter second side : ')
b = float(b)
c = input('Enter third side : ')
c = float(c)

s = (a+b+c)/2
s= float(s)
area = (s*(s-a)*(s-b)*(s-c)) ** 0.5
area = float(area)

print('Area of Triangle with sides ',a,'',b, '', c , ' is : '  ,area)