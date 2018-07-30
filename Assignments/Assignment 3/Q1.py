
def lcm(x,y):
    if x>y:
        grt = x
    else:
        grt = y 
    while True:
        if (grt%x==0) and (grt%y==0):
            lcm=grt
            break
    return lcm

print(lcm(3,2))    
           