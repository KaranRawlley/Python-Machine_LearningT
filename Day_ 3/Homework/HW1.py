usa = ['atlanta','new york','chicago','baltimore']
uk = ['london','bristol','cambridge']
india = ['mumbai','delhi','banglore']
d = [usa,uk,india]

def country():
    a = input('Enter a city name ')
    if a in usa:
         
        print(a.upper(),'is in USA')
    elif a in uk: 
        print(a.upper(),'is in UK')
   
    elif a in india: 
        print(a.upper(),'is in INDIA')
country()        
             
b = input('Enter the city of user 1 ')
c = input('Enter the city of user 2 ')

if b in usa and c in usa:
    print('You two live in the same country USA')
    
elif b in uk and c in uk:
    print('You two live in the same country UK')
    
elif b in india and c in india:
    print('You two live in the same country INDIA',)    
else: 
    print('You live in different country')        
    
     

            
        
        
               