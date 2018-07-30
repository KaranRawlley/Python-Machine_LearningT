garde = None
def grading(d):
    sum = 0
    
    for i in range(5):
        sum += d[i]
        
    avg = sum/5
    print(sum)
    print(avg)
    if avg<50:
        grade = 'E'
    elif 50<=avg<60:
        grade = 'D'
    elif 60<=avg<70:
        grade = 'C'
    elif 70<=avg<80:
        grade = 'B'            
    if 80<=avg<90:
        grade = 'A'
    if 90<=avg<=100:
        grade = 'A+' 
    print(grade)

flag = -1
l = []
count = 1
while flag ==-1:
    print('CASE',count)
    for i in range(5):
        print('Enter marks of',i+1,'subject : ')
        d = float(input())  
        l.append(d)
        
    grading(l)
    
    
    choice = int(input('If you wanna continue press 2 (if not press any other number) '))
    if choice==2:
        flag = -1
        count+=1
        l.clear()
    else:
        flag=5    
      
    
               