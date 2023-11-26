from fastapi import FastAPI , Path , Query , HTTPException , status
from typing import Optional
from pydantic import BaseModel

abc = FastAPI()

class Item(BaseModel):
    name : str
    price : float
    brand : Optional[str] = None

class Updateitem(BaseModel):
    name : Optional[str] = None
    price :Optional[float] = None
    brand : Optional[str] = None

items = {}

@abc.get("/get_item/{item_id}")
def get_item(item_id : int = Path(None, description="Enter the proper id", gt=0)):
     return items[item_id]


@abc.get("/get_name/")
def get_item(name : Optional[str] = None):
     for item_id in items:
         if items[item_id]["name"] == name:
            return items[item_id]
     raise HTTPException(status_code=404, detail="Name not found")

@abc.post("/create_item/{item_id}")
def create_item(item_id :int, item :Item):
    if item_id in items:
        return {"Error":"Already existing"}
    items[item_id] = {"name":item.name,"price":item.price,"brand":item.brand}
    return items[item_id]

@abc.put("/update_item/{item_id}")
def update_item(item_id : int, item:Updateitem):
    if item_id not in items:
        return {"Error":"Item does not exist"}

    if item.name != None:
        items[item_id]["name"] = item.name

    if item.price != None:
        items[item_id]["price"] = item.price

    if item.brand != None:
        items[item_id]["brand"] = item.brand
    
    return items[item_id]
    
@abc.delete("/delete_item")
def delete_item(item_id : int = Query(...,description="Enter the item to be deleted")):
    if item_id not in items:
        return {"Data":"Not exists"}
    
    del items[item_id]
    return {"Data":"Succesfully deleted"}