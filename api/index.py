from fastapi import FastAPI, Request

app = FastAPI()

@app.get("/api/blog")
def get_posts():
    return {
        "posts": [
            {"autor": "Teste", "mensagem": "Funcionando 🚀"}
        ]
    }

@app.put("/api/blog")
async def create_post(request: Request):
    data = await request.json()

    autor = data.get("autor")
    mensagem = data.get("mensagem")

    if not autor or not mensagem:
        return {"error": "Campos obrigatórios"}

    return {
        "status": "ok",
        "autor": autor,
        "mensagem": mensagem
    }