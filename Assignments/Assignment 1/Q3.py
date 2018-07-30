a = input('Enter a number ')
a = int(a)
b = input('Enter another number ')
b = int(b)
print('unswapped values ',a,' ',b)
c = a
a = b
b = c
print('Swapped values',a,' ',b)

#part 2 w/o third var

d = input('\n\nEnter a number ')
d = int(d)
e = input('Enter a number ')
e = int(e)
print(' unswapped values ',d,' ',e )
d = d+e
e = d-e
d = d-e

print('\n\nSwapped values',d,' ',e )



