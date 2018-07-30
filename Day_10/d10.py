import  re
import regex

# NameAge =   '''    
# Janice is 22 and Theon is 33
# Gabriel is 44 and Joye is 21
# '''
# 
# ages    =   re.findall(r'\d{1,3}', NameAge)
# names   =   re.findall(r'[A-Z][a-z]*',NameAge)
# 
# ageDict ={};
# x=0;
# for eachname    in  names:
#     ageDict[eachname]=ages[x]
#     x+=1
# print(ageDict)    
# 

# allinform = re.findall('inform','we need informto inform hinformim with the latest information')
# print(allinform)

# Str =   'we need to inform him with the latest information'
# for i in re.finditer('inform',Str):
#     locTuple    =   i.span()
#     
#     print(locTuple)   


# Str = 'Sat,hat,mat,pat'
# allStr=re.findall('[h-m]at', Str)
# for i in allStr:
#     print(i)

# food = 'hat,rat,mat,pat'
# regex = re.compile('[r]at')
# food=regex.sub('food',food)
# print(regex)
# print(food)


# randStr='12345'
# print('Matches:',len(re.findall('\d{2}',randStr)))

# str = '''
# hola amigos 
# rick and morty 
# bklyn 99
# '''
# print(str)
# regex = re.compile('\n')
# nstr = regex.sub('',str)
# print(nstr)

# str = 'here is \\bpit'
# print(str)
# print(re.search(r'\\bpit',str))
# num2 =['444-122-1234','123-122-7899','111-123-23','67-7890-2019']
# print(num2)
# for i in num2:
#     
#     pn = re.findall('\w{3}\-\w{3}\-\w{4}',i)
#     if(pn!=[]):
#         print(pn,' Valid')
#         


# fn = 'Mayank Jha'
# if(re.findall('\w*\s\w*',fn)):
#      print('Valid')
# else:
#     print('not valid')
mail =[ 'karan8798rawlley@gmail.com','Reysham @ com','Kv .com','123 @.com','sakshirawlley879@gmail.com']

for i in mail:
    if(re.findall('[\w._+%-]{1,20}\@[\w]{2,20}.[a-zA-Z]{2,3}$',i)):
        print('valid ',i)
    else:
        print('not valid ',i)    
             
             
        







