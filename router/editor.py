from fastapi import APIRouter, Request  
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel

from .script_json import extract_multiple_table_info

router = APIRouter(
    prefix="/editor",
    tags=["editor"],
)

## api -------------------------------------------------
class Item(BaseModel):
    text: str
    
@router.post("/")
async def get_item(item: Item):
    text = item.text
    #print(text)
    structed_table = extract_multiple_table_info(text)
    # Return the text
    print(structed_table)
    return {"table": structed_table}