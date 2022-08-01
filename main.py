import pymongo
# connecting mongo db and pycharm

client = pymongo.MongoClient("mongodb+srv://madhura:Maddy2809@cluster0.jx1ws.mongodb.net/?retryWrites=true&w=majority")
db = client.test
print(db)
# till here we are connecting with mongodb
d={
    "name":"madhura",
    "email":"madhura@yahoo.com",
    "surname":"rao"

}
d={
    'name':'pradhyun',
    'emailid':'pradhyunbekal@gmail.com',
    'surname':'Bekal'

}

db1=client['mongotest']
coll=db1['test']
coll.insert_one(d)