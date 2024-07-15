from fastapi import APIRouter


from crud.file import get_all_files



router = APIRouter(
    prefix="/api/file",
    tags=["file"],
)


'''

--- get all the files ---

    -params: user_id 

'''

@router.get("/get/{user_id}")
async def get_all_file(user_id):
    file_list = get_all_files(user_id)
    return {"files": file_list}