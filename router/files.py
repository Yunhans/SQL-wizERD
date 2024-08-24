from fastapi import APIRouter, status, HTTPException
from pydantic import BaseModel
import os
import base64


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
    
    file_id = new_file(file_name, user_id)
    
    return {"file_id": file_id}



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

@router.put("/update", status_code=status.HTTP_200_OK)
async def update_file_name_(request: FileUpdateRequest):
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
async def delete_file_(file_id):
    
    result = delete_file(file_id)
    
    return result



'''

--- UPLOAD IMAGE ---

    -params: file_id, imageDataUrl

'''

class ImageUploadRequest(BaseModel):
    file_id: str
    imageDataUrl: str

@router.post("/upload_image", status_code=status.HTTP_200_OK)
async def upload_image(request: ImageUploadRequest):
    file_id = request.file_id
    image_data_url = request.imageDataUrl
 
    if not image_data_url.startswith("data:image/png;base64,"):
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Invalid image data URL")
    
    image_data = image_data_url.split(",")[1]
    image_bytes = base64.b64decode(image_data)
    
    # image path
    image_path = f"./static/img/file_imgs/{file_id}.png"

    # ensure the directory exists
    os.makedirs(os.path.dirname(image_path), exist_ok=True)

    # store image into folder
    with open(image_path, "wb") as image_file:
        image_file.write(image_bytes)
        
    return {"img": f"{file_id}.png"}