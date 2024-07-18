from fastapi import APIRouter


from crud.table import get_all_tables



router = APIRouter(
    prefix="/api/table",
    tags=["file"],
)


'''

--- get all the tables ---

    -params: file_id 

'''

@router.get("/get/{file_id}")
async def get_all_table(file_id):
    table_list = get_all_tables(file_id)
    return table_list