from fastapi import APIRouter, Request  
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel

from crud.table import get_tables_script
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
    result = middle_parse_json(file_id, middle_format)

    return result
    

    

# erd to script
    
@router.get("/api/erd_to_script/{file_id}")
async def json_parse_sql(file_id):
    table_script = get_tables_script(file_id)
    sql_script = generate_sql_script(table_script)

    return sql_script