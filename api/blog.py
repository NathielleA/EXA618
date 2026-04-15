import os
import json
from datetime import datetime
from pymongo import MongoClient

MONGODB_URI = os.environ.get('MONGODB_URI')

def get_collection():
    if not MONGODB_URI:
        raise Exception("MONGODB_URI não definida")

    client = MongoClient(MONGODB_URI)
    db = client['blogdb']
    return db['posts']


def handler(request):
    try:
        collection = get_collection()

        if request.method == "GET":
            posts = list(collection.find({}, {'_id': 0}))
            return {
                "statusCode": 200,
                "body": json.dumps({"posts": posts})
            }

        elif request.method == "PUT":
            data = json.loads(request.body)

            autor = data.get("autor")
            mensagem = data.get("mensagem")

            if not autor or not mensagem:
                return {
                    "statusCode": 400,
                    "body": json.dumps({"error": "Campos obrigatórios"})
                }

            collection.insert_one({
                "autor": autor,
                "mensagem": mensagem,
                "data": datetime.now().strftime('%d/%m/%Y %H:%M:%S')
            })

            return {
                "statusCode": 200,
                "body": json.dumps({"status": "ok"})
            }

        return {
            "statusCode": 405,
            "body": json.dumps({"error": "Método não permitido"})
        }

    except Exception as e:
        return {
            "statusCode": 500,
            "body": json.dumps({"error": str(e)})
        }

