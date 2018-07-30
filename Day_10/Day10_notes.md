## Regular Expression

A r.e is a spl text string for describing a search pattern

#package 'regex'

#module name  're'

eg . 

import  re

NameAge =   '''    
Janice is 22 and Theon is 33
Gabriel is 44 and Joye is 21
'''

ages    =   re.findall(r'\d{1,3}', NameAge)
names   =   re.findall(r'[A-Z][a-z]*',NameAge)

ageDict ={};
x=0;
for eachname    in  names:
    ageDict[eachname]=ages[x]
    x+=1
print(ageDict)    



## findall() returns string no of times of ouccrance 

 allinform = re.findall('inform','we need informto inform hinformim with the latest information')
 print(allinform)


## finditer() returns index of inform (start and end) 
  
Str =   'we need to inform him with the latest information'
for i in re.finditer('inform',Str):
    locTuple    =   i.span()
    
    print(locTuple)  


## Match letters with a particular pattern

Str = 'Sat,hat,mat,pat'
allStr=re.findall('[shmp]at', Str)    # can use range too [h-m]
for i in allStr:
    print(i)

## Replace a string

food = 'hat,rat,mat,pat'
regex = re.compile('[r]at')
food=regex.sub('food',food)

print(food)

#prog = re.compile(pattern)
#result = prog.match(string)


## match a single character

randStr='12345'
print('Matches:',len(re.findall('\d{5}',randStr)))

#result = re.match(pattern, string)


## 

# \d => decimal [0-9]
# \D => non digit char [^0-9]
# \s => any whitespaces [\t\n\r\f\v]
# \S => non whitespace char [^ \t\n\r\f\v]
# \w => alphanum char  [a-zA-z0-9]
# \W => non alpha num char [^ a-zA-z0-9]

## removing whitespaces

str = '''
hola amigos 
rick and morty 
bklyn 99
'''
print(str)
regex = re.compile('\n')
nstr = regex.sub('',str)
print(nstr)
	
## NAme validaTION
fn = 'Mayank Jha'
if(re.findall('\w*\s',fn)):
     print('Valid')
else:
    print('not valid')
             

## Email vaidation

mail =[ 'karan8798rawlley@gmail.com','Reysham @ com','Kv .com','123 @.com','sakshirawlley879@gmail.com']

for i in mail:
    if(re.findall('[\w._+%-]{1,20}\@[\w.-]{2,20}.[a-zA-Z]{2,3}',i)):
        print('valid ',i)
    else:
        print('not valid ',i)    
             