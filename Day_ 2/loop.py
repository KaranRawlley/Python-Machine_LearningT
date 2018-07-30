name ='Rick'
inp = input('Guess the name, Enter')
pos=0
while inp!=name and pos<len(name):
    print("Wrong,Hint letter",end=' ')
    print(pos+1,"is", name[pos]+".",end="" )
    inp=input("Guess Again ")
    pos = pos+1
    
if pos==len(name) and name!=inp:
        print("bad",name)
        
else:
    print("\n Right")
    