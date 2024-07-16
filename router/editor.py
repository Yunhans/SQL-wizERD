from fastapi import APIRouter, Request  
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel

from utils.sql_grammar import sql_parse_middle
from utils.script_json import middle_parse_json


'''

--- script interface trigger ---

'''



router = APIRouter(
    prefix="/editor",
    tags=["editor"],
)


## api -------------------------------------------------
class Item(BaseModel):
    file_id: str
    text: str
    
@router.post("/api/table_transform")
async def sql_parse_json(item: Item):

    file_id = item.file_id
    raw_sql = item.text
    #print(raw_sql)
    middle_format = sql_parse_middle(raw_sql)
    table_data = middle_parse_json(file_id, middle_format)

    return table_data
    

    

# @router.get("/api/get_transformed_sql")
# async def get_trandform_sql():

#     return table_data

# http://127.0.0.1:8000/editor/api/get_transformed_sql