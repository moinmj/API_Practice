from fastapi import FastAPI , Path , Query ,HTTPException, status
from pydantic import BaseModel
from typing import Optional
app=FastAPI()
# /hello
# /get-item
# local() function

@app.get("/")
def home():
    return{"Data": "Test"}
@app.get("/about")
def about():
    return{"name":"Moin"}
class Item(BaseModel):
    name:str
    price:float
    brand:str
inventory={}
class UpdateItem(BaseModel):
    name:Optional[str] = None
    price:Optional[float] = None
    brand:Optional[str] = None
inventory={}
# inventory={1:{"name": "Moin",
#               "Rollno": 33,
#               "position": "first"}}
@app.get("/get_item/{item_id}")
def get_item(item_id: int = Path(description="The path id is")):
    return inventory[item_id]
@app.get("/get-by-name/{item_id}")
def get_item(*,item_id:int,name:str,test: int):
    for item_id in inventory:
        # if inventory[item_id].name == name:
        if inventory[item_id]["name"] == name:
            return inventory[item_id]
    # return {"Data": "Not found"}
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Item name not found ")
@app.post("/create-item/{item_id}")
def create_item(item_id:int,item: Item):
    if item_id in inventory:
        return{"Error":"Item_id already exists"}
    inventory[item_id] = item
    # inventory[item_id] = {"name": item.name,
    #                       "brand" :item.brand,
    #                       "price": item.price}
    return inventory[item_id]
@app.put("/update_item/{item_id}")
def update_item(item_id: int, item: UpdateItem):
    if item_id not in inventory:
        return{"Error":"Item_id doesn't exists"}
    if item.name != None:
        inventory[item_id].name = item.name
    if item.price != None:
        inventory[item_id].price = item.price
    if item.brand != None:
        inventory[item_id].brand = item.brand
    return inventory[item_id]
@app.delete("/delete-item")
def delete_item(item_id:int = Query (description="The Id that is to be deleted")):
    if item_id not in inventory:
        return {"Error":"ID does not exist."}
    del inventory[item_id]
    return{"Success":"Item deleted"}