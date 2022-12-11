import pymongo
client = pymongo.MongoClient("mongodb+srv://ineuron:11223344@nehal.8sxbiat.mongodb.net/?retryWrites=true&w=majority")
db = client.test
print(db)

d={
    "name" : "suhanshu",
    "email" : "nehaldipti00@gmail.com",
    "surname" : "dipti"
}
db1 = client['mongotest']
coll = db1['test']
coll.insert_one(d)