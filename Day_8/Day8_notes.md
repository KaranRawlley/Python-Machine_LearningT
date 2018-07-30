       

       DataBase

SQL python

=> import Db module
=> connect to the Db
=> Aquire cursor . with connection.cursor()
=> execute SQl statement. with execute(),executemany()
=> fetch the results . with fetchhone(), fetchmany() or fetchall()
=> commit changes . connection.commit()
=> close the connection use close.connection() or the with keyword


Eg

import sqlite3 as sq
conn =sq.connect('cources.db')
cursor = conn.cursor()
cursor.execute("""CREATE TABLE courses(number INTERGER PRIMARY KEY,name text,ects real);""")
cursor.execute("""INSERT INTO courses VALUES('o282o',"Python Programming",5 );""")
conn.commit()

## Python SQL fetching data

cursor.execute('select * from courses')
cursor.fetchone()# return one row at a time 

#fetching all data from table using loop
for row in cursor :
    print(row)

#fetching all rows in one go using fetchall()
print(cursor.fetchall()) #creates a list of all the tuples

#fetching all with limit

cursor.execute('select * from courses order by number limit 2')
print(cursor.fetchall())

#python search data
cursor.execute('select*from courses where number=? or name=? or ects=?',('value1','value2','value3'))
print(cursor.fetchall())


# parameterized search data into a python var

param = {'ects':10.0}
cursor.execute('select number from courses where ects=?',(param['ects'],))  
print(cursor.fetchall())


# UPDATing  from Db 

cursor.execute('update courses set name=?,ects=? where number=?',('name','acts','number'))

cursor.execute('update courses set name=?,ects=? where number=?',('Rick','98','o282i'))

cursor.execute('select*from courses where number=? or name=? or ects=?',('o282i','value2','kj'))
 
print(cursor.fetchall())



# Deleting from SQLite

cursor.execute('delete from courses where number=?',('o2829',))
cursor.execute('select*from courses ')
  

id name age aim 
create insert update search delete view