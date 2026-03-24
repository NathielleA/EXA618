import urllib.request
from bs4 import BeautifulSoup

file = open("atividade5\seeds.txt", "r") # Abrindo arquivo com as URLs

# Criando um arquivo .txt para armazenar os resultados
output_file = open("atividade5\output.txt", "w")

# Percorrendo o arquivo linha por linha, acessando cada URL e extraindo o título e as imagens
for line in file:
    page = urllib.request.urlopen(line.strip())
    html = str(page.read().decode('utf-8'))

    soup = BeautifulSoup(html, 'html.parser')

    titulo = soup.title.string if soup.title else "Sem título"
    output_file.write("Titulo " + titulo + "\n")

    for img in soup.find_all('img'):
        imagem = img.attrs.get("src")
        if imagem:
            output_file.write("Imagem: " + imagem + "\n")

output_file.close()
file.close()