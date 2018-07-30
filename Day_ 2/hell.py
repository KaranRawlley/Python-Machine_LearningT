#no>43 print large
# >35 <=43 medium
# >25 <=35 small
# <=25 not eligible
# The value is small/medium/large 

import random 

a=random.randint(0,45)
print(a)

if a>43:
    print('The value is large')
    
elif 35<a<=43:
    print('The value is medium')

elif 25<a<=35:
    print('The value is small') 
    
else:
    print("The value is Not Eligible")           


