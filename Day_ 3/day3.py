# 
# 
# 
# def area():
#     flag = -1
#     while flag ==-1:
#         print('\n 1.Triangle \n 2.Circle \n 3.Square \n 4.Rectangle')
#         choice = input('\n Enter your choice ')
#         choice = int(choice)
#         if(choice==1):
#             b = input('base ')
#             h = input('height ')
#             b,h=float(b),float(h)
#             
#             print(0.5*b*h)
#         elif(choice==2):
#             r = input('radius ')
#             r=float(r)
#             print(3.14*r*r)            
#         elif(choice==3):
#             b = input('side ')
#             b=float(b)
#             print(b*b)     
#         elif(choice==4):
#             b = input('length ')
#             l = input('bjk ')
#             b=float(b)
#             l=float(l)
#             print(b*l) 
#         else:
#     
#             
#             print('Wrpng choice')
#                                    
#         ch=input('continue press 2')
#         ch = int(ch)
#         if ch!=2:
#             flag=1
#                
# area()

d=dict(one=1,four=4)

# print(d)
# 
# for i in d:
#     print(i,d[i])
# print('\n')    
# for i in sorted(d.keys()):
#     print(i,d[i])
# print('\n')    
# for i,h in sorted(d.items()):
#     print(i,h) 
# print('\n')    
# for i in sorted(d.values()):
#     print(i)
# print('\n')
# for i in d:
#     print(i)       
    
# d.pop('one')
# print(d)    

del d['four']
print(d)
    
        