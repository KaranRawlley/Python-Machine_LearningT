#celsius to fahrenheit converter
import time

flag = -1

while flag==-1:
    c = input('\n Enter the Temperature in Celsius ')
    c = float(c)
    f = (c*1.8)+32
    f = float(f)
    print(c,'C is ',f,'F')
    time.sleep(4)
    choice = input('If you wanna quit press 2(to continue press any other number) ')
    choice = int(choice)
    if choice == 2:
        flag = 1
     