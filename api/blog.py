import os
import json
from datetime import datetime
# from pymongo import MongoClient

# MONGODB_URI = os.environ.get('MONGODB_URI')

# def get_collection():
#     if not MONGODB_URI:
#         raise Exception("MONGODB_URI não definida")

#     client = MongoClient(MONGODB_URI)
#     db = client['blogdb']
#     return db['posts']


def handler(request):
    return {
        "statusCode": 200,
        "body": "API funcionando"
    }