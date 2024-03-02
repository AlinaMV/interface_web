from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

app = FastAPI()
templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.get("/items/{item_id}", response_class=HTMLResponse)
async def read_item(request: Request, item_id: int, q: str = None):
    return templates.TemplateResponse("index.html", {"request": request, "item_id": item_id, "q": q})
