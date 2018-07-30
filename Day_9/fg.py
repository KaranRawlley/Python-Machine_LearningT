# lambda function
# from distutils.command.check import check
from _functools import reduce

# double = lambda x:x*2
# print(double(5))

#use of lambda() with filter()

# li = [5,7,33,22,97,54,62,77,23,73,61]
# 
# flist = list(filter(lambda x:(x%2!=0),li))
# 
# print(flist)


# alter without filter
# mylist = [1,2,3,4,5]
# 
# def alter(values,check):
#     return [val for val in values if check(val)]
# 
# list = alter(mylist,lambda x: x!=5)
# print(list)   

#using filter

# flist = list(filter(lambda x:(x!=5),mylist))
# print(flist)
# 
# l ='INDIA123DELHI'
# 
# # flist = list(filter(lambda x:(x!='1' or x!='2' or x!='3'),l))
# # print(flist)
# 
# print(l)
# 
# nl = list(filter(lambda x:x not in [ str(i) for i in range(10)],l))
# 
# nnl =''.join(nl)
# print(nnl)
#     
# 
# line = input('Enter string ')
# letter = input('Enter letter to remove ')
# print(list(line))
# 
# nline = list(filter(lambda x : x != letter,line))
# # print(nline)
# 
# print(''.join(nline))


# #lambda with map()
# 
# listl = [5,7,22,97,54,62,77,23,73,61]
# 
# fl = list(map(lambda x:x*2,listl))
# print(fl)
#    

# listl = [5,8,10,20,50,100]
# 
# sum = reduce((lambda x,y:x+y),listl)
# print(sum)
#     
    
    










         

    