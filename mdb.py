"""
1)Connect to db
2)Run CRUD 
"""
import mysql.connector as db
try:
    conn=db.connect(
    host="localhost",
    user="root",
    passwd="",
    database="mdb"
    )
except:
    print("Connection Error")


#cursor
cursor=conn.cursor(prepared=True)

#C- create
#cursor.execute("Create Table flight(id INT AUTO_INCREMENT Primary Key,origin TEXT NOT NULL,destination TEXT NOT NULL,duration TEXT NOT NULL)")
##Get database tables
cursor.execute("SHOW TABLES")
for table in cursor:
	print(table)


cursor.execute("INSERT INTO task(todo,date) VALUES(?,?)",("Cook meal","1/7/2021"))

#Read
id=4
cursor.execute('SELECT * FROM task WHERE id =  ? ',(id,))

##Get the row 
data = cursor.fetchone()[1]
print(data)

#U-Update
cursor.execute('Update task SET todo=? where id=?',("CIA Briefing on 9-11. What actually happened?",4))

#D-Delete
cursor.execute('DELETE FROM task WHERE id=?',(30,))
conn.commit()
print(cursor.lastrowid)

cursor.close()
conn.close()

