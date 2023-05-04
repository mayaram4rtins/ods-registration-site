from flask import Flask, render_template, request, flash, redirect, session, url_for
import json

class User():
    def __init__(self, nome, usuario, email, senha, telefone):
        self.nome = nome
        self.usuario = usuario
        self.email = email
        self.senha = senha
        self.telefone = telefone

usuario1 = User('Mayara', 'maymarti', 'mayara@mayara.com.br', 'senha2', '123456789')
usuario2 = User('Fabricio', 'fabbrito', 'fabricio@fabricio.com.br', 'senha3', '987654321')

usuarios = {usuario1.usuario : usuario1,
            usuario2.usuario : usuario2}

app = Flask(__name__, template_folder='templates')
app.secret_key = 'palavrasecreta'

@app.route('/')
def index():
    return render_template('Tela_de_login.html')

@app.route('/login')
def login():
    proxima = request.args.get('proxima')
    return render_template('Tela_de_login.html', proxima=proxima)

@app.route('/novo-projeto')
def cadastroProjeto():
    if 'user' not in session or session['user'] == None:
        return redirect(url_for('login', proxima=url_for('menu')))
    return render_template('.html')

@app.route('/autenticar', methods=['POST', ])
def autenticar():
    if request.form['name'] in usuarios:
        user = usuarios[request.form['usuario']]
        if request.form['password'] == user.senha:
            session['user'] = user.usuario
            flash(user.usuario + ' logou com sucesso!')
            proxima_pagina = request.form['proxima']
            return redirect(proxima_pagina)
        else:
            flash(user.usuario + " não logado! Verifique suas credenciais.")
            return redirect(url_for('login'))

@app.route('/logout')
def logout():
    session['user'] = None
    flash('Logout efetuado com sucesso!')
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)