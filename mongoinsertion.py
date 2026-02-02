import pymongo

if __name__ == "__main__":
    print("Welcome to pymongo")
    client=pymongo.MongoClient("mongodb://localhost:27017/")
    print(client)
    db=client['Moin'] #making database name,forming a database
    collection=db["sampleCollectionForMoin"] #cannot form a database until and unless a collection is build or formed/Analogy:Table in sql
    dictionary = {"name":"Moin", "marks":50} #data that will go in database, data is stored in key value pair called collection
    collection.insert_one(dictionary) #method to insert data in dictionary 
    dictionary2 = {"name":"Salman", "marks":55}
    collection.insert_one(dictionary2)
    insert_these=[
        {"_id":1,"name":"Moin", "location":"srinagar","marks":20},
        {"_id":2,"name":"salman", "location":"budgam","marks":45},
        {"_id":3,"name":"toib", "location":"pulwama","marks":65},
        {"_id":4,"name":"faheem", "location":"handwara","marks":45} #Formed a list of dictionary or data
    ]
    collection.insert_many(insert_these) #This function will insert all the data at once instead of adding one by one 
    
