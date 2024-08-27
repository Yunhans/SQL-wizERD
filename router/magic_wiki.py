from fastapi import APIRouter, Request
from fastapi.templating import Jinja2Templates


router = APIRouter(
    tags=["magic-wiki"],
)

templates = Jinja2Templates(directory="templates")

@router.get("/magic-wiki")
async def tutorial(request: Request):
    return templates.TemplateResponse("magicbook.html", {"request": request})