import sqlite3 as sq
conn =sq.connect('cources.db')
cursor = conn.cursor()
cursor.execute("""CREATE TABLE IF NOT EXISTS courses(number INTERGER PRIMARY KEY,name text,ects real);""")
# cursor.execute("""INSERT INTO courses VALUES('o2847',"Python Programming",5 );""")
# conn.commit()


# parameterized input with a python var
# courses = ('0987','Nonlinear',10)
# 
# cursor.execute("insert into courses values(?,?,?);",courses)

# parameterized insertion of multiple rows with executemany:

# courses = [('0985','Nonlinear',10),('0785','Nonlinear',10)]
#  
# cursor.executemany("insert into courses values(?,?,?);",courses)

#Python SQL fetching data

# cursor.execute('select * from courses')
# print(cursor.fetchone())# return one row at a time 

#fetching all data from table using loop
# for row in cursor :
#     print(row)

#fetching all rows in one go using fetchall()
# print(cursor.fetchall())


#fetchin all with limit

# cursor.execute('select * from courses order by number limit 2')
# print(cursor.fetchall())
#python search data
# cursor.execute('select*from courses where number=? or name=? or ects=?',('o2829','value2','k'))
# 
# print(cursor.fetchall())


# parameterized search data into a python var

# param = {'ects':10.0}
print(cursor.fetchall())

# cursor.execute('select number from courses where ects=?',(param['ects'],))  
# print(cursor.fetchall())

# UPDATing  from Db 


# cursor.execute('update courses set name=?,ects=? where number=?',('Rick','98','o282i'))
# 
# cursor.execute('select*from courses where number=? or name=? or ects=?',('o282i','value2','kj'))
#  
# print(cursor.fetchall())


# Deleting from SQLite

cursor.execute('delete from courses where number=?',('o2829',))
cursor.execute('select*from courses ')
  
print(cursor.fetchall())






conn.close()