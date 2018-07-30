# class Vehicle:
#     def gen_usage(self):
#         print('Transportation')
# 
# class car(Vehicle):
#     def __init__(self):
#         print('car')
#         self.wheel=4
#         self.roof=True
#         
#     def usage(self):
#         self.gen_usage() 
#         print('commute work')   
#           
# class mc(Vehicle):
#     def __init__(self):
#         print('Bike')
#         self.wheel=2
#         self.roof=False
#         
#     def usages(self):
#         self.gen_usage() 
#         print('commute work')   
# c = Vehicle()
# c.gen_usage()
# 
# d = car()
# d.usage()
# 
# 
# m=mc()
# m.usages()
# 
# print(isinstance(c,Vehicle))
# print(isinstance(m,Vehicle))
# print(isinstance(c,car))
# print(isinstance(d,car))
# print(isinstance(m,mc))
# 
# print(issubclass(car,mc))

#                 Multiple Inheritance
# class father:
#     def loves(self):
#         print('gardener')
#         
# class mother:
#     def loves(self):
#         print('cook')
# class child(mother,father):
#     def loves(self):
#         mother.loves(self)
#         father.loves(self)
#         print('loves')
#         
# f=father()
# m=mother()
# c=child()
# c.loves()

# class Human:
#     data = None
#     def __init__(self,n,g,o,w):
#         self.name=n
#         self.gender=g
#         self.occ=o
#         self.work=w
#         
#     def prints(self):
#          print('Name :',self.name,'\nGender :',self.gender,'\nOccupation :',self.occ,'\nSpeaks :',self.data,'\nDo work :',self.work)
#    
#  
# tc=Human('Tom Cruise','Male','Actor','Shoot movie')
# tc.data='I am Ethan Hunt of Mission Impossible'
# tc.prints()
# ms=Human('Maria Sharapova','Female','Tennis player','play tennis')  
# ms.data='I won 5 grand slams'
# ms.prints()                              
class person:
    def __init__(self,n,ln):
        self.name=n
        self.last=ln
        
    def __str__(self):
        return self.name+' '+ self.last
    
       
class emp(person):
    def __init__(self,f,l,sn):
        super().__init__(f,l)
        self.stn=sn
        
x=person('Rick','Sanchez')
y=emp('Morty','hola',34)
print(x)  
print(y)     





