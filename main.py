from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from router import items, whiteboard

app = FastAPI()
app.include_router(items.router)
app.include_router(whiteboard.router)

app.mount("/static", StaticFiles(directory="static"))

templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
async def read_main(request: Request):
    return templates.TemplateResponse("main.html", {"request": request})
