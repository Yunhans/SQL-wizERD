from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from router.users import add_middleware

from router import items, users, tutorial, editor

app = FastAPI()
app.include_router(items.router)
app.include_router(users.router)
app.include_router(tutorial.router)
app.include_router(editor.router)

# add middleware
add_middleware(app)

app.mount("/static", StaticFiles(directory="static"))

templates = Jinja2Templates(directory="templates")

# @app.get("/white", response_class=HTMLResponse)
# async def read_main(request: Request):
#     return templates.TemplateResponse("main.html", {"request": request})
