import urllib.request
from bs4 import BeautifulSoup

with open("atividade5/seeds.txt", "r") as file, open("atividade5/output.html", "w", encoding="utf-8") as output_file:
    # Escreve o cabeçalho do HTML
    output_file.write("""<!DOCTYPE html>\n<html lang='pt-br'>\n<head>\n<meta charset='UTF-8'>\n<title>Atividade 5 - Parse HTML (Nathielle)</title>\n</head>\n<body>\n""")
    output_file.write("<h1>Títulos e Imagens Extraídas: </h1>\n")

    for line in file:
        url = line.strip()
        try:
            page = urllib.request.urlopen(url)
            html = page.read().decode('utf-8')
            soup = BeautifulSoup(html, 'html.parser')

            titulo = soup.head.title.string.strip() if soup.head and soup.head.title else "Sem título"

            imagens = []
            for img in soup.find_all('img'):
                imagem = img.attrs.get("src")
                if imagem:
                    if not imagem.startswith("http"):
                        imagem = url.rstrip('/') + "/" + imagem.lstrip('/')

                    output_file.write(f"<h2>{titulo}</h2>\n")
                    output_file.write(f"<img src=\"{imagem}\" alt=\"Imagem\" style='max-width:400px;'><br>\n")                

        except Exception as e:
            output_file.write(f"<p>Erro ao acessar {url}: {e}</p>\n")

    # Fecha o HTML
    output_file.write("</body>\n</html>")