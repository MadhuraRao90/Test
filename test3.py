import mysql.connector as conn

mydb=conn.connect(host="localhost",user="root",password="Pradhyun@14042022")
cursor=mydb.cursor()

q="select employe_id ,emp_mailid from kkrao1.kkraodetails"

cursor.execute(q)
# print(cursor.fetchall()) we can directly print fetchall it will give lists

lst=[]
for i in cursor.fetchall():
    lst.append(i)
print(lst)



# to use a specific database pass the command - use kkrao1
# then it will start using that database n all the tables inside that will be referred
