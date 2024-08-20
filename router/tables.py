from fastapi import APIRouter, Request, status
from pydantic import BaseModel
from typing import List, Optional, Union


from crud.table import new_table, get_all_tables, get_table, update_table_info, update_table_position, delete_table
from utils.extract_table_detail import extract_details, extract_detail, reverse_info
from utils.json_script import generate_sql_script


router = APIRouter(
    prefix="/api/table",
    tags=["file"],
)


'''

--- create new table (erd) ---
        
        -params: file_id, table_name, script

'''

class TableCreateRequest(BaseModel):
    file_id: str
    name: str
    attribute: Optional[List] = []
    foreign_keys: Optional[List] = []
    location:dict



@router.post("/create", status_code=status.HTTP_200_OK)
async def create_new_table(request: TableCreateRequest):
    file_id = request.file_id
    table_name = request.name
    attributes = request.attribute
    foreign_keys = request.foreign_keys
    x = request.location['x']
    y = request.location['y']
    
    script = str(reverse_info(table_name, attributes, foreign_keys))
    result = new_table(table_name, script, x, y, file_id)
    
    return result



'''

--- get all the tables ---

    (script --> erd)
    -params: file_id 

'''

@router.get("/get/{file_id}", status_code=status.HTTP_200_OK)
async def get_all_table(file_id):
    table_list = get_all_tables(file_id)
    table_list_extract = extract_details(table_list)
    
    return table_list_extract



'''

--- get all the tables ---

    (erd --> script)
    -params: file_id

'''

@router.get("/get/toscript/{file_id}", status_code=status.HTTP_200_OK)
async def get_all_table_to_script(file_id):
    
    table_list = get_all_tables(file_id)
    script = generate_sql_script(table_list)
    
    return script
    


'''

--- get specific table ---

    -params: file_id

'''

@router.get("/get/specific/{table_id}", status_code=status.HTTP_200_OK)
async def get_specific_table(table_id):
    table_list = get_table(table_id)
    table_list_extract = extract_detail(table_list)
    
    return table_list_extract

'''

--- update table info (erd)---

    -params: table_id, table_name, script

'''

class TableUpdateInfoRequest(BaseModel):
    id: str
    name: str
    attribute: Optional[List] = []
    foreign_keys: Optional[List] = [] 


@router.put("/update/info", status_code=status.HTTP_200_OK)
async def update_table_info_(request: TableUpdateInfoRequest):

    table_id = request.id
    table_name = request.name
    attributes = request.attribute
    foreign_keys = request.foreign_keys
    
    script = str(reverse_info(table_name, attributes, foreign_keys))
    
    result = update_table_info(table_id, table_name, script)
    
    return result



'''

--- update table position (erd)---

    -params: table_id, x, y

'''

class TablePosition(BaseModel):
    x: float
    y: float

class TableUpdatePositionRequest(BaseModel):
    id: str
    position: TablePosition

class TableUpdatePositionsRequest(BaseModel):
    updates: List[TableUpdatePositionRequest]



@router.put("/update/position", status_code=status.HTTP_200_OK)
async def update_table_position_(request: TableUpdatePositionsRequest):
    for update in request.updates:
        table_id = update.id
        x = update.position.x
        y = update.position.y
        result = update_table_position(table_id, x, y)
    
    return result



'''

--- delete table (erd)

    -params: table_id

'''

@router.delete("/delete/{table_id}", status_code=status.HTTP_200_OK)
async def delete_table_(table_id):
    result = delete_table(table_id)
    
    return result
    