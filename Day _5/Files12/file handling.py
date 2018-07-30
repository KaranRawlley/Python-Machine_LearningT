def main():
    infile = open('lines.txt','r')
    outfile = open('new.txt','w')
    for line in infile:
        print(line,file=outfile,end ='')
    print('done')  
    outfile.close()
    file = open('new.txt','r')
    print(file.read())
     
main() 
#     

# def main():
#     buffersize=50000
#     infile = open('bigfile.txt','r')
#     outfile = open('new.txt','w')
#     buffer = infile.read(buffersize)
#     while len(buffer):
#         outfile.write(buffer)
#         print('.',end='')
#         buffer=infile.read(buffersize)
#         print()
#         
#     print('Done')
#     
# main()      

# def main():
#     buffersize=50000
#     infile = open('olives.jpg','rb')
#     outfile = open('new.jpg','wb')
#     buffer = infile.read(buffersize)
#     while len(buffer):
#         outfile.write(buffer)
#         print('.',end='')
#         buffer=infile.read(buffersize)
#         print()
#         
#     print('Done')
#     
# if __name__=='__main__':main()        