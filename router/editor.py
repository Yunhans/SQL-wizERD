from fastapi import APIRouter, Request  
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel

from utils.sql_grammar import sql_parse_middle
from utils.script_json import middle_parse_json
from utils.json_script import generate_sql_script


'''

--- script interface trigger ---

'''



router = APIRouter(
    prefix="/editor",
    tags=["editor"],
)


## api -------------------------------------------------


# script to erd

class Script(BaseModel):
    file_id: str
    text: str
    
@router.post("/api/script_to_erd")
async def sql_parse_json(item: Script):

    file_id = item.file_id
    raw_sql = item.text
    #print(raw_sql)
    middle_format = sql_parse_middle(raw_sql)
    table_data = middle_parse_json(file_id, middle_format)

    return table_data
    

    

# erd to script

class Erd(BaseModel):
    file_id: str
    table_data: dict
    
@router.post("/api/erd_to_script")
async def json_parse_sql(item: Erd):

    file_id = item.file_id
    table_data = item.table_data
    sql_script = generate_sql_script(table_data)

    return sql_script