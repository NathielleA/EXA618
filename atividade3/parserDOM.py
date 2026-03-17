import time
from xml.dom.minidom import parse

inicio = time.time()
Mapa = parse("atividade3/map.osm")

for node in Mapa.getElementsByTagName("node"):
    lat = node.getAttribute("lat")
    lon = node.getAttribute("lon")
    tipo = None
    nome = None
    for tag in node.getElementsByTagName("tag"):
        if tag.getAttribute("k") == "amenity":
            tipo = tag.getAttribute("v")
        if tag.getAttribute("k") == "name":
            nome = tag.getAttribute("v")
    if tipo:
        if nome:
            print("Latitude:", lat, "Longitude:", lon, "| Tipo do Local:", tipo, "| Nome do Local:", nome)
        else:
            print("Latitude:", lat, "Longitude:", lon, "| Tipo do Local:", tipo, "| Nome do Local: Não disponível")
fim = time.time()
print(f"Tempo de execução do parser DOM: {fim - inicio:.4f} segundos")