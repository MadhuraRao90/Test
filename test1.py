# import a sql library
import mysql.connector as conn

# establish a connectivity- between pycharm and mysql
mydb=conn.connect(host="localhost",user="root",password="Pradhyun@14042022")
# here host = localhost as we are using a local machine
# user - by default we all get it as root
# password - watever password i had given while setting up mysql workbench
# if db is available in cloud - host -- admin will give u url - so will have to specify that

cursor=mydb.cursor()
#cursor.execute("create database kkrao1")
#cursor.execute("create table kkrao1.kkraodetails(employe_id int(10),employe_name varchar(80),emp_mailid varchar(40),employe_salary int(6),employe_attendance int(3))")
#cursor.execute("show databases") # this is to execute a query
#
s="select * from kkrao1.kkraodetails"
q=cursor.execute (s)
print(q) # if there is nothing to fetch then this will give errors

# these are exact 4 lines of code that you have to execute in order to run any query

#whwever u are creating a table u need to create tables and columns. database is like a folder


# create a database and inside that create a table



# put up the data inside the table
