#!/usr/bin/env python3
import os
from urllib.parse import parse_qs

qs = os.environ["QUERY_STRING"]
list = parse_qs(qs, encoding="latin-1")
var = list["nome"][0]


print("Content-type: text/html;charset=utf-8")
print()
print("<html><head><title>Exemplo GET</title></head><body>")
print("QUERY_STRING = '" + qs + "'<br>")
print("var = '" + var + "'<br>")
print("</body></html>")