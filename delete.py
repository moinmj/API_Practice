import pymongo
if __name__ == "__main__":
    print("Welcome to pymongo")
    client=pymongo.MongoClient("mongodb://localhost:27017/")
    print(client)
    db=client['Moin'] #making database name,forming a database
    collection=db["sampleCollectionForMoin"] #cannot form a database until and unless a collection is build or formed/Analogy:Table in sql
    record={"name":'faheem'}
    collection.delete_one(record) #deletes one item that is given in argument
    collection.delete_many(record) #deletes all item that is given in the argument 
    up=collection.delete_many(record) 
    print(up.deleted_count) #will give total count of deleted items