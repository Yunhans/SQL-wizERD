from fastapi import APIRouter
from pydantic import BaseModel


from crud.file import new_file, get_all_files




router = APIRouter(
    prefix="/api/file",
    tags=["file"],
)


'''
--- CREATE ---

    -create new file
    -params: user_id, file_name

'''

class FileCreateRequest(BaseModel):
    user_id: str
    file_name: str


@router.post("/create")
async def create_new_file(request: FileCreateRequest):  
    user_id = request.user_id
    file_name = request.file_name
    
    message = new_file(file_name, user_id)
    return message



'''
--- READ ---

    -get all the files
    -params: user_id 

'''

@router.get("/get/{user_id}")
async def get_all_file(user_id):
    file_list = get_all_files(user_id)
    
    return {"files": file_list}