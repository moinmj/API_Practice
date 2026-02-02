import pymongo
if __name__ == "__main__":
    print("Welcome to pymongo")
    client=pymongo.MongoClient("mongodb://localhost:27017/")
    print(client)
    db=client['Moin'] #making database name,forming a database
    collection=db["sampleCollectionForMoin"] #cannot form a database until and unless a collection is build or formed/Analogy:Table in sql
    one = collection.find_one() #any One document will be pulled
    one = collection.find_one({'name':"faheem"}) #document will be pulled with name faheem only.
    allDocs = collection.find({"name":"Moin"}) #will pull all the documents containing name Moin
    for item in allDocs:
        print(item)
    allDocs = collection.find({"name":"Moin"},{"name":1,"_id":0}) #This will only show name all values are by default 1 and when we put a particular value to 1 all the other values goes 0 apart from id, id you have to implicitly put 1 or 0 to show or not show
    for item in allDocs:
        print(item)
    allDocs = collection.find({"name":"Moin","marks":{"$lte":90}},{"name":1,"_id":0}) #$lte this will give me all the moin whose marks are greater than 90 only 
    # print(collection.count_documents())

