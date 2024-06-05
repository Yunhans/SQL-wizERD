from fastapi import APIRouter, Request  
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel


from .script_json import transform_sql_to_dict

router = APIRouter(
    prefix="/editor",
    tags=["editor"],
)

# define global variables
table_data = None


## api -------------------------------------------------
class Item(BaseModel):
    text: str
    
@router.post("/api/table_transform")
async def get_item(item: Item):
    global table_data
    text = item.text
    #print(text)
    structed_table = transform_sql_to_dict(text)
    table_data = structed_table  # Update the global variable
    return {"table": structed_table}
    

    

@router.get("/api/get_transformed_sql")
async def get_trandform_sql():

    return {"table": table_data}

# http://127.0.0.1:8000/editor/api/get_transformed_sql