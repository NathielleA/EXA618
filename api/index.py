import os
from fastapi import FastAPI, Request
from pymongo import MongoClient
from datetime import datetime

app = FastAPI()

MONGODB_URI = os.environ.get("MONGODB_URI")

client = MongoClient(MONGODB_URI)
db = client["blogdb"]
collection = db["posts"]


@app.get("/blog")
def get_posts():
    posts = list(collection.find({}, {"_id": 0}))
    return {"posts": posts}

@app.post("/blog")
async def handle_blog(request: Request):
    data = await request.json()

    action = data.get("action")

    if action == "put":
        return create_post(data)

    elif action == "get":
        return get_posts()
    
    if "action" not in data:
        return {"error": "action obrigatória"}

    return {"error": "Ação inválida"}

def create_post(data):
    autor = data.get("autor")
    mensagem = data.get("mensagem")

    if not autor or not mensagem:
        return {"error": "Campos obrigatórios"}

    collection.insert_one({
        "autor": autor,
        "mensagem": mensagem,
        "data": datetime.now().strftime('%d/%m/%Y %H:%M:%S')
    })

    return {"status": "ok"}

@app.get("/")
def home():
    return {"msg": "home funcionando"}