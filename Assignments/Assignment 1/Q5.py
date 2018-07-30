#program to convert KM to miles
import time
flag = -1

while flag == -1:
    km = input('Enter the Km to convert to miles : ')
    km = float(km)
    m = km*0.62137
    m = float(m)
    print('\n',km,'Kilometers are',m,'Miles')
    time.sleep(1.5)
    choice = input('\nIf you wanna quit press 1 else any number to continue \n')
    choice = int(choice)
    if(choice==1):
        flag = 1