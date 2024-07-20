from fastapi import APIRouter, Request
from fastapi.templating import Jinja2Templates


router = APIRouter(
    tags=["whiteboard"],
)

templates = Jinja2Templates(directory="templates")

@router.get("/whiteboard/{file_id}")
async def whiteboard(request: Request, file_id):
    
    user = request.session.get('user')
    user_id = request.session.get('user_id')
    
    return templates.TemplateResponse("whiteboard.html", {
        "request": request, 
        "file_id": file_id,
        "user": user,
        "user_id": user_id
        })