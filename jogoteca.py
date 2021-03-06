from flask import Flask, request, redirect, session, flash, url_for
from flask.templating import render_template
from models import Jogo, Usuario
from dao import JogoDao
from flask_mysqldb import MySQL

app = Flask(__name__)
app.secret_key = 'Alura'

app.config['MYSQL_HOST'] = "127.0.0.1"
app.config['MYSQL_USER'] = "Robert"
app.config['MYSQL_PASSWORD'] = "Robert1105"
app.config['MYSQL_DATABASE'] = "jogoteca"
app.config['MYSQL_PORT'] = "3306"
db = MySQL(app)

jogo_dao = JogoDao(db)

usuario_1 = Usuario('Luan','Luan Marques', '1234')
usuario_2 = Usuario('Nico','Nico Steppat', '7a1')
usuario_3 = Usuario('Flavio','Flávio', 'javascript')
usuario_3 = Usuario('Robert','Robert', '1234')

usuarios = {
    usuario_1.id: usuario_1,
    usuario_2.id: usuario_2,
    usuario_3.id: usuario_3,
}

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
        return redirect(url_for('login', proxima=url_for('novo')))
    else:
        return render_template('novo.html', cabecario='JOGO BRABO', titulo='NOVO JOGO')

@app.route('/criar', methods=['POST'])
def criar():
    nome = request.form['nome']
    categoria = request.form['categoria']
    console = request.form['console']
    jogo = Jogo(nome, categoria, console)
    jogo_dao.salvar(jogo)
    return redirect(url_for('index'))

@app.route('/login')
def login():
    proxima = request.args.get('proxima')
    return render_template('login.html', proxima=proxima)

@app.route('/autenticar', methods=['POST'])
def autenticar():

    if(request.form['usuario'] in usuarios):
        usuario = usuarios[request.form['usuario']]
        if(usuario.senha == request.form['senha']):
            session['usuario_logado'] = request.form['usuario']
            flash(request.form['usuario'] + ' logou com sucesso!')
            proxima_pagina = request.form['proxima']
            return redirect(proxima_pagina)
    else:
        flash(' Senha/usuário não identificado, tente novamente.')
        return redirect(url_for('login'))

@app.route('/logout')
def logout():
    session['usuario_logado'] = None
    flash('Usuário deslogado!')
    return redirect(url_for('index'))

app.run(debug=True)