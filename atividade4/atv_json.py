import time
from xml.dom.minidom import parse
import json

Mapa = parse("atividade3/map.osm")

# Criar um arquivo GeoJSON para armazenar os dados extraídos
geojson = dict()
geojson["type"] = "FeatureCollection"
geojson["features"] = []

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
            nome = nome
        else:
            nome = "Nao disponivel"

        # Criar um dicionário para a feature GeoJSON
        geojson["features"].append({
                "type": "Feature",
                "geometry": {
                    "type": "Point",
                    "coordinates": [float(lon), float(lat)]
                },
                "properties": {
                    "tipo": tipo,
                    "nome": nome
                }            
        })
print(geojson)

# Salvar o arquivo GeoJSON com os dados extraídos
with open("atividade4/map.geojson", "w") as f:
    json.dump(geojson, f, indent=4, ensure_ascii=False)


