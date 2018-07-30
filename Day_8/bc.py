import sqlite3 as sq
conn =sq.connect('bdg.db')
cursor = conn.cursor()


cursor.execute("""CREATE TABLE IF NOT EXISTS bdg(id INTEGER PRIMARY KEY AUTOINCREMENT,name text,age integer,aim text);""")

def inserT():
    name = input('Enter name ')
    
    age = int(input('Enter age '))
    
    
    
    cursor.execute("""INSERT INTO bdg VALUES(NULL,?,?,? );""",(name,age,'NA'))
   
    conn.commit()
#     conn.close()
    
    
def updateT():
    ch = input('What do you want to update?  ')
    if(ch=='name') :
        d = int(input('Enter id of the tuple you want to update name ' ))
        nname = input('Enter the new name ')
        
        cursor.execute('update bdg set name=? where id=?',(nname,d))
        
        
    elif(ch=='age') :
        d = int(input('Enter id of the tuple you want to update age ' ))
        nage = int(input('Enter the new age '))
        
        cursor.execute('update bdg set age=? where id=?',(nage,d))
        
    elif(ch=='aim') :
        d = input('Enter id of the tuple you want to update aim ' )
        naim = input('Enter the new aim ')
        
        cursor.execute('update bdg set aim=? where id=?',(naim,d))
        
    conn.commit()    
     
def deleteT():
    d = int(input('Enter the id  of the tuple you want to delete '))
    
    cursor.execute('delete from bdg where id=?',(d,))
    conn.commit()
def viewT() :
    
    cursor.execute('select * from bdg')
    
    print(cursor.fetchall())    
    
# def searchT():
deleteT()
viewT()
        
        
        
           
           
       
       
     

