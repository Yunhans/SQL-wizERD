from fastapi import APIRouter, Request  
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel

from .sql_grammar import sql_parse_middle
from .script_json import middle_parse_json

router = APIRouter(
    prefix="/editor",
    tags=["editor"],
)



## api -------------------------------------------------
class Item(BaseModel):
    text: str
    
@router.post("/api/table_transform")
async def sql_parse_json(item: Item):
    
    raw_sql = item.text
    # print(raw_sql)
    middle_format = sql_parse_middle(raw_sql)
    table_data = middle_parse_json(middle_format)

    return table_data
    

    

# @router.get("/api/get_transformed_sql")
# async def get_trandform_sql():

#     return table_data

# http://127.0.0.1:8000/editor/api/get_transformed_sql