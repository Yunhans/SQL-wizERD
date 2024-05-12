from fastapi import APIRouter, Request
from fastapi.templating import Jinja2Templates


router = APIRouter(
    tags=["tutorial"],
)

templates = Jinja2Templates(directory="templates")

@router.get("/tutorial")
async def tutorial(request: Request):
    return templates.TemplateResponse("tutorial.html", {"request": request})