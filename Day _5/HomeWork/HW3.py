#Open the file
fobj = open("hw3.txt",'r')
outfile = open('new.txt','w')
text = fobj.read().strip().split()
l = ['geetansh','om','gurpreet','akshay','rick']
flag=True
#Conditions
while True:
    for i in l:
        
        if i in text: #string in present in the text file
            continue
           
        else: #string is absent in the text file
            print(i,file=outfile,end ='\n')
            print('hello')
            continue
    break   
            
fobj.close()
outfile.close()