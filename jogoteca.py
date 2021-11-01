from flask import Flask, request, redirect, session, flash
from flask.templating import render_template

app = Flask(__name__)
app.secret_key = 'Alura'

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
    if ('usuario_logado' not in session or session['usuario_logado'] == None):
        return redirect('/login')
    else:
        return render_template('novo.html', cabecario='JOGO BRABO', titulo='NOVO JOGO')

@app.route('/criar', methods=['POST',])
def criar():
    nome = request.form['nome']
    categoria = request.form['categoria']
    console = request.form['console']
    jogo = Jogo(nome, categoria, console)
    lista.append(jogo)
    return redirect('/')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/autenticar', methods=['POST'])
def autenticar():
    if('mestra' == request.form['senha']):
        session['usuario_logado'] = request.form['usuario']
        flash(request.form['usuario'] + ' logou com sucesso!')
        return redirect('/')
    else:
        flash(' Senha/usuário não identificado, tente novamente.')
        return redirect('/login')

@app.route('/logout')
def logout():
    session['usuario_logado'] = None
    flash('Usuário deslogado!')
    return redirect('/')

app.run(debug=True)