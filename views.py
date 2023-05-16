from flask import render_template, request, flash, redirect, session, url_for
from main import app
from models import User, Projetos

@app.route('/')
def index():
    lista = Projetos.query.order_by(Projetos.id)
    return render_template('Tela_de_apresentação.html', projetos=lista)

@app.route('/login')
def login():
    proxima = request.args.get('proxima')
    return render_template('Tela_de_login.html', proxima=proxima)

@app.route('/menu')
def menu():
    return render_template('Tela_de_Menu.html')

    @app.route('/novo-projeto')
    def novoProjeto():
        if 'user' not in session or session['user'] == None:
            return redirect(url_for('login', proxima=url_for('novoProjeto')))
        return render_template('Tela_de_CadastroProjeto.html')

'''
@app.route('/cadastro-projeto')
def cadastroProjeto():
    id_proj = request_form['id_proj']
    nome = request_form['name']
    user = request_form['id_user']
    desc = request_form['descricao']
    ods = request_form['ods']
    telefone = request_form['telefone']
    data_cadastro = request_form['data_cadastro']
    status_projeto = request_form['status_projeto']
    tag = request_form['tag']

    proj = Projetos.query.filter_by(nome=name).first()

    if proj:
        flash('Jogo já existente!')
        return redirect(url_for('index'))

    novo_proj = Projetos(id_proj=id_proj, nome=nome, user=user, desc=desc, ods=ods, telefone=telefone, 
                         data_cadastro=data_cadastro, status_projeto=status_projeto, tag=tag)
    
    db.session.add(novo_proj)
    db.session.commit()

    return redirect(url_for('index'))
'''

@app.route('/editar')
def editarProjeto():
    if 'user' not in session or session['user'] == None:
        return redirect(url_for('login', proxima=url_for('editarProjeto')))
    return render_template('Tela_de_CadastroProjeto.html')

@app.route('/autenticar', methods=['POST', ])
def autenticar():
    user = User.query.filter_by(nickname=request.form['usuario']).first()
    if user:
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