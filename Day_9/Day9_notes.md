
##  lambda function

#While normal functions are defined using the def keyword , python gives an anonymous func defined using the lambda keyord

Syntax of lambda

lambda arguments : expression

# eg . lambda function

double = lambda x:x*2
print(double(5))



 ##lambda() with filter(),map(),reduce()

#lambda can be used with built in functions - filter(), map(), reduce()


#use of lambda() with filter()

li = [5,7,33,22,97,54,62,77,23,73,61]

flist = list(filter(lambda x:(x%2!=0),li))

print(flist)   


# alter without filter
mylist = [1,2,3,4,5]

def alter(values,check):
    return [val for val in values if check(val)]

list = alter(mylist,lambda x: x!=5)
print(list)   
         

#using filter

flist = list(filter(lambda x:(x!=5),mylist))
print(flist)         

## String functions

# capitalize() => capitilizes first letter of string
# upper()  => converts lowercase letters in a string into uppercase
# swapcase() => invert case for all letters in string
# strip() => return or remove white space in the start & end of the string 
# str.replace(old,new[max]) => old have been replaced with new
# isalnum() => returns true if string has at least 1 character and all characters are alpha numeric and false o/w
# isdigit() => returns true if string only have digits
# isnumeric()
# str.join(sequence)



## lambda() with map()

map()  => takes a list as argument. The func is called with a lambda function and a list and an new list is returned 
          which contains all the lambda modified elements

#lambda with map()

listl = [5,7,22,97,54,62,77,23,73,61]

fl = list(map(lambda x:x*2,listl))
print(fl)


## lambda with reduce()

 
 __eq__(self) # exactly equal
 