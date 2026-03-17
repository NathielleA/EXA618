
import time
import xml.sax

class OSMHandler(xml.sax.ContentHandler):
    def startElement(self, name, attributes):
        if name == "node":
            self.lat = attributes.get("lat", "")
            self.lon = attributes.get("lon", "")
            self.tipo = None
            self.nome = None
            self.in_node = True
        elif name == "tag" and getattr(self, "in_node", False):
            if attributes.get("k") == "amenity":
                self.tipo = attributes.get("v")
            if attributes.get("k") == "name":
                self.nome = attributes.get("v")

    def endElement(self, name):
        if name == "node" and getattr(self, "in_node", False):
            if self.tipo:
                if self.nome:
                    print(f"Latitude: {self.lat} Longitude: {self.lon} | Tipo do Local: {self.tipo} | Nome do Local: {self.nome}")
                else:
                    print(f"Latitude: {self.lat} Longitude: {self.lon} | Tipo do Local: {self.tipo} | Nome do Local: Não disponível")
            self.in_node = False


inicio = time.time()
parser = xml.sax.make_parser()
parser.setContentHandler(OSMHandler())
parser.parse("atividade3/map.osm")
fim = time.time()
print(f"Tempo de execução do parser SAX: {fim - inicio:.4f} segundos")