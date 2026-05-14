from flask import Flask, request, make_response, render_template

app = Flask(__name__)

@app.route('/')
def home():
    nome = request.cookies.get('nome')
    if not nome:
        nome = 'visitante'
    return render_template('home.html', nome=nome)

@app.route('/nome/<nome>')
def salvar_nome(nome):
    resposta = make_response(
        render_template('home.html', nome=nome)
    )
    resposta.set_cookie('nome', nome, max_age=60*60)
    return resposta

if __name__ == '__main__':
    app.run(debug=True)