#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import cgi
import cgitb
import os
from datetime import datetime

cgitb.enable()

DATA_FILE = os.path.join(os.path.dirname(__file__), 'blog_posts.txt')

def read_posts():
    posts = []
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, 'r', encoding='utf-8') as f:
            for line in f:
                try:
                    autor, mensagem, data = line.strip().split('\t')
                    posts.append({'autor': autor, 'mensagem': mensagem, 'data': data})
                except ValueError:
                    continue
    return posts[::-1]  # Mais recentes primeiro

def save_post(autor, mensagem):
    data = datetime.now().strftime('%d/%m/%Y %H:%M:%S')
    with open(DATA_FILE, 'a', encoding='utf-8') as f:
        f.write(f"{autor}\t{mensagem}\t{data}\n")

def print_posts(posts):
    for post in posts:
        print(f"<div style='border:1px solid #ccc; margin-bottom:10px; padding:10px;'>")
        print(f"<strong>{post['autor']}</strong> em {post['data']}<br>")
        print(f"<pre style='white-space:pre-wrap;'>{cgi.escape(post['mensagem'])}</pre>")
        print("</div>")

print("Content-type: text/html; charset=utf-8\n")
print("<html><head><title>Blog CGI Simples</title></head><body>")
print("<h1>Blog CGI Simples</h1>")

form = cgi.FieldStorage()
if form.getvalue('autor') and form.getvalue('mensagem'):
    autor = form.getvalue('autor')
    mensagem = form.getvalue('mensagem')
    save_post(autor, mensagem)
    print("<p><b>Mensagem enviada com sucesso!</b></p>")

print("<form method='POST' action='/cgi-bin/blog.py'>")
print("Autor: <input type='text' name='autor' required><br>")
print("Mensagem:<br>")
print("<textarea name='mensagem' rows='4' cols='50' required></textarea><br>")
print("<input type='submit' value='Postar'>")
print("</form><hr>")

posts = read_posts()
print_posts(posts)

print("</body></html>")
