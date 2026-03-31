import requests

from bs4 import BeautifulSoup

def main():
    livros = extrair_abreviaturas("https://www.bibliaonline.com.br/acf") # ACF é a versão padrão do site
    print(livros)

    url = "https://www.bibliaonline.com.br/"

    file = open("Projeto-Individual/crawler/DadosExtraidosBibliaOnline_NVI.csv", "a", encoding="utf-8")
    file.write("Livro|Capítulo|Versículo|Texto|Versão\n") # Escreve o cabeçalho do arquivo CSV

    for livro in livros:
        url_livro = url + "nvi/" + livro
        print(f"Extraindo versículos de {livro}...")
        extrair_versiculos(livro, url_livro, file)
    
    file.close()

def extrair_abreviaturas(url):

    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")

    # Extrair todas as abreviaturas dos livros, começando do terceiro pois os dois primeiros são abreviaturas dos versículos do dia
    abreviaturas = list()
    for a in soup.find_all("a", href=True)[3:70]: # Abrangendo os 66 livros
        href = a["href"]
        if href.startswith("/acf/"):
            partes = href.split("/")
            if len(partes) > 2 and partes[2]:
                abreviaturas.append(partes[2])

    # print("Abreviaturas encontradas:")
    # for abrev in abreviaturas:
    #     print(abrev)

    return abreviaturas

def extrair_versiculos(livro, url, file):

    capitulos = extrair_capitulos(url)

    for capitulo in capitulos:
        url_capitulo = url + "/" + capitulo
        
        response = requests.get(url_capitulo)
        soup = BeautifulSoup(response.text, "html.parser")

        # Encontrar todos os spans de número de versículo
        versiculos_num = soup.find_all("span", class_="v")
        print(f"Número de versículos encontrados: {len(versiculos_num)}")

        # Loop para extrair o número do versículo e o texto correspondente
        for v in versiculos_num:
            numero = v.get_text(strip=True) # Obter o número do versículo, removendo espaços em branco
            texto_span = v.find_next_sibling("span", class_="t") # Encontrar o próximo span com a classe "t" (texto do versículo)

            if texto_span:
                texto = texto_span.get_text(strip=True)
                print(numero, texto)
                file.write(f"{livro}|{capitulo}|{numero}|{texto}|NVI\n")

def extrair_capitulos(url):
    # Extraíndo número de capítulos de um livro
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")

    capitulos = soup.find_all("a", href=True)
    capitulos_num = [c for c in capitulos if c["href"].startswith("/nvi/") and c["href"].count("/") == 3] # Filtra apenas os links que correspondem aos capítulos
    capitulos_num = [c["href"].split("/")[3] for c in capitulos_num] # Extrai o número do capítulo do link

    return capitulos_num

if __name__ == "__main__":
    main()