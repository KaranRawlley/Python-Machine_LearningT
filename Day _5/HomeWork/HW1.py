class remote:
    def __init__(self):
        self.channels=['Hungama','Pogo','Sonic','Cartoon Network','Toonami','Disney Channel','Nick','Nick jr',]
        self.index = -1
        
    def __iter__(self):
        return self
    def __next__(self):
        self.index+=1
        if self.index == len(self.channels) :
            self.index=0
        return self.channels[self.index]
    
r = remote()
itr = iter(r)
for i in range(10):
    print(next(itr))    
           