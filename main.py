from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from router.users import add_middleware

from router import files, tables, users, magic_wiki, editor, whiteboard

app = FastAPI()

app.include_router(users.router)
app.include_router(files.router)
app.include_router(tables.router)
app.include_router(magic_wiki.router)
app.include_router(editor.router)
app.include_router(whiteboard.router)

# add middleware
add_middleware(app)

app.mount("/static", StaticFiles(directory="static"))

templates = Jinja2Templates(directory="templates")
