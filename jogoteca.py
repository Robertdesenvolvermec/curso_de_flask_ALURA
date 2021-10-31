from flask import Flask, request, redirect
from flask.templating import render_template

app = Flask(__name__)

class Jogo():
    def __init__(self, nome, categoria, console):
        self.nome = nome
        self.categoria = categoria
        self.console = console

jogo1 = Jogo('Call of Duth', 'Ação', 'PS2')
jogo2 = Jogo('Resident Evil','Terror','PS2')
jogo3 = Jogo('GTA','Ação','PS2')
lista = [jogo1, jogo2, jogo3]

@app.route('/')
def index():
    return render_template('lista.html', cabecario='JOGO BRABO', titulo='JOGO BRABO', jogos=lista)

@app.route('/novo')
def novo():
    return render_template('novo.html', cabecario='JOGO BRABO', titulo='NOVO JOGO')

@app.route('/criar', methods=['POST',])
def criar():
    nome = request.form['nome']
    categoria = request.form['categoria']
    console = request.form['console']
    jogo = Jogo(nome, categoria, console)
    lista.append(jogo)
    return redirect('/')

app.run(debug=True, use_reloader=True)