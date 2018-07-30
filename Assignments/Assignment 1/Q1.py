# a = None
# b = None
# c = None
import time
flag = -1

while flag==-1:
    a = input("Enter the first operand : ")
    a = int(a)
    b = input("Enter the second operand : ")
    b = int(b)
    print("\n Choose operation from the following menu => ")
    print("\n 1.ADDITION \n 2.SUBTRACTION \n 3.MULTIPLICATION \n 4.DIVISION ")
    time.sleep(1.5)
    choice = input("\n Enter your choice : ")
    choice = int(choice)
    time.sleep(1.5)
    if choice == 1:
        c=a+b
        print('ADDITION ',a,'+',b,'=',c)
    elif choice == 2:
        c=a-b
        print('SUBTRACTION ',a,'-',b,'=',c)
    elif choice == 3:
        c=a*b
        print('MULTIPLICATION ',a,'*',b,'=',c)
    elif choice == 4:
        c=a/b
        print('DIVISION ',a,'/',b,'=',c)
    else:
        print("Wrong choice entered")
    time.sleep(1.5)    
    cont = input("if you want to end enter 5 (any other number to continue) : ")
    cont = int(cont)
    if cont == 5:
        flag = 1
        
                        
   
    
    
    
    