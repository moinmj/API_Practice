from fastapi import FastAPI, Path
app=FastAPI()
# GET 
# PUT 
# DELETE 
invent={1:{
        "Name": "MOIN",
        "Class":"ecec"
    }}
@app.get("/get_item/{item_id}")
def get_item(item_id: int = Path(description= "The path id is") ):
    return invent[item_id]