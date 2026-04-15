import os
from datetime import datetime
from pymongo import MongoClient

MONGODB_URI = os.environ.get('MONGODB_URI')
MONGO_DB = 'blogdb'
MONGO_COLLECTION = 'posts'

def get_collection():
    if not MONGODB_URI:
        raise Exception("MONGODB_URI não definida")

    client = MongoClient(MONGODB_URI)
    db = client[MONGO_DB]
    return db[MONGO_COLLECTION]


def handler(request):
    try:
        collection = get_collection()

        if request.method == "GET":
            posts = []
            for doc in collection.find({}, {'_id': 0}).sort('data', -1):
                posts.append(doc)

            return {
                "statusCode": 200,
                "body": {"posts": posts}
            }

        elif request.method == "PUT":
            data = request.get_json()

            autor = data.get("autor", "")
            mensagem = data.get("mensagem", "")

            if autor and mensagem:
                post = {
                    'autor': autor,
                    'mensagem': mensagem,
                    'data': datetime.now().strftime('%d/%m/%Y %H:%M:%S')
                }
                collection.insert_one(post)

                return {
                    "statusCode": 200,
                    "body": {"status": "success"}
                }

            return {
                "statusCode": 400,
                "body": {"error": "Autor e mensagem obrigatórios"}
            }

        return {
            "statusCode": 405,
            "body": {"error": "Método não permitido"}
        }

    except Exception as e:
        return {
            "statusCode": 500,
            "body": {"error": str(e)}
        }


# export
app = handler