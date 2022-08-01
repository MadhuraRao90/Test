import mysql.connector as conn

mydb=conn.connect(host="localhost",user="root",password="Pradhyun@14042022")
cursor=mydb.cursor()
q="insert into kkrao1.kkraodetails values(101,'pradhyun','pradhyun@gmail.com',100,30)"
cursor.execute(q)
mydb.commit() # use commit whenver u make any chnages to db

q1="select * from kkrao1.kkraodetails"

cursor.execute(q1)
for i in cursor.fetchall():
    print(i)
