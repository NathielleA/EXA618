#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import sys
from datetime import datetime
from urllib.parse import parse_qs

DATA_FILE = os.path.join(os.path.dirname(__file__), 'blog_posts.csv')

# Função da API para rodar no Vercel
def handler(request, response):

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
    
def read_posts():
    posts = []
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, 'r', encoding='utf-8') as f:
            for line in f:
                try:
                    autor, mensagem, data = line.strip().split(',')
                    posts.append({'autor': autor, 'mensagem': mensagem, 'data': data})
                except ValueError:
                    continue
    return posts[::-1]  # Mais recentes primeiro

def save_post(autor, mensagem):
    data = datetime.now().strftime('%d/%m/%Y %H:%M:%S')
    with open(DATA_FILE, 'a', encoding='utf-8') as f:
        f.write(f"{autor},{mensagem},{data}\n")
