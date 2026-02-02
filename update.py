import pymongo
if __name__ == "__main__":
    print("Welcome to pymongo")
    client=pymongo.MongoClient("mongodb://localhost:27017/")
    print(client)
    db=client['Moin'] #making database name,forming a database
    collection=db["sampleCollectionForMoin"] #cannot form a database until and unless a collection is build or formed/Analogy:Table in sql
    prev={"name":'faheem'}
    nextt={'$set':{"location":"Srinagar"}}
    collection.update_one(prev,nextt) #will update one key value will change faheem's location to srinagar
    collection.update_many(prev,nextt) #will update all key value named faheem will change all faheem's location to srinagar
    up=collection.update_many(prev,nextt) #will update all key value named faheem will change all faheem's location to srinagar
    print(up.modified_count) #will give total count of modified items