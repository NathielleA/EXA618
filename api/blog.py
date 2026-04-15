import os
from datetime import datetime
from pymongo import MongoClient

# Configuração MongoDB Atlas
MONGODB_URI = os.environ.get('MONGODB_URI')
MONGO_DB = 'blogdb'
MONGO_COLLECTION = 'posts'

client = MongoClient(MONGODB_URI)
db = client[MONGO_DB]
collection = db[MONGO_COLLECTION]

# Função da API para rodar no Vercel
def handler(request, response):
    try:
        if request.method == "GET":
            posts = read_posts()
            return response.json({"posts": posts})
        elif request.method == "PUT":
            data = request.json()
            autor = data.get("autor", "")
            mensagem = data.get("mensagem", "")
            if autor and mensagem:
                save_post(autor, mensagem)
                return response.json({"status": "success", "message": "Mensagem salva com sucesso!"})
            else:
                return response.json({"status": "error", "message": "Autor e mensagem são obrigatórios."}, status=400)
        else:
            return response.json({"status": "error", "message": "Método não permitido."}, status=405)
    except Exception as e:
        return response.json({"status": "error", "message": f"Exception: {str(e)}"}, status=500)
    

def read_posts():
    posts = []
    for doc in collection.find({}, {'_id': 0}).sort('data', -1):
        posts.append(doc)
    return posts


def save_post(autor, mensagem):
    data = datetime.now().strftime('%d/%m/%Y %H:%M:%S')
    post = {
        'autor': autor,
        'mensagem': mensagem,
        'data': data
    }
    collection.insert_one(post)

# Exportação explícita para Vercel
app = handler
