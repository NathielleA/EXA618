from xml.dom.minidom import parse

Mapa = parse("atividade3/map.osm")

for node in Mapa.getElementsByTagName("node"):
    for tag in node.getElementsByTagName("tag"):
        if tag.getAttribute("k") == "amenity":
            print("Local: ", tag.getAttribute("v"))
            print("Latitude: ", node.getAttribute("lat"), "Longitude: ", node.getAttribute("lon"))