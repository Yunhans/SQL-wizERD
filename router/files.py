from fastapi import APIRouter, status
from pydantic import BaseModel


from crud.file import new_file, get_all_files, update_file_name, delete_file




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


@router.post("/create", status_code=status.HTTP_200_OK)
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

@router.get("/get/{user_id}", status_code=status.HTTP_200_OK)
async def get_all_file(user_id):
   
    file_list = get_all_files(user_id)
    
    return {"files": file_list}



'''

--- UPDATE ---

    -update file name
    -params: file_id, file_name

'''

class FileUpdateRequest(BaseModel):
    file_id: str
    file_name: str

@router.put("/update/{file_id}", status_code=status.HTTP_200_OK)
async def update_file_name(request: FileUpdateRequest):
    file_id = request.file_id
    file_name = request.file_name
    
    result = update_file_name(file_id, file_name)
    
    return result



'''

--- DELETE ---

    -delete file
    -params: file_id
'''

@router.delete("/delete/{file_id}", status_code=status.HTTP_200_OK)
async def delete_file(file_id):
    
    result = delete_file(file_id)
    
    return result