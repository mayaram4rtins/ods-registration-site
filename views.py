from flask import render_template, request, flash, redirect, session, url_for
from main import app, db
from models import User, Projetos

@app.route('/')
def index():
    lista = Projetos.query.order_by(Projetos.id_proj)
    return render_template('Tela_de_apresentação.html', projeto=lista)

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
        return redirect(url_for('login', proxima=url_for('cadastroProjeto')))
    return render_template('Tela_de_CadastroProjeto.html')

@app.route('/cadastro-projeto')
def cadastroProjeto():
    id_proj = request.form['id_proj']
    nome = request.form['name']
    user = request.form['id_user']
    desc = request.form['descricao']
    telefone = request.form['telefone']
    data_cadastro = request.form['data_cadastro']
    status_projeto = request.form['status_projeto']
    tag = request.form['tag']

    proj = Projetos.query.filter_by(nome=nome).first()

    if proj:
        flash('Projeto já existente!')
        return redirect(url_for('menu'))

    novo_proj = Projetos(id_proj=id_proj, nome=nome, user=user, desc=desc, telefone=telefone, 
                         data_cadastro=data_cadastro, status_projeto=status_projeto, tag=tag)
    
    db.session.add(novo_proj)
    db.session.commit()

    return redirect(url_for('menu'))

@app.route('/novo-usuario')
def novoUsuario():
    return render_template('Tela-de-cadastro.html')

@app.route('/cadastro-usuario')
def cadastroUsuario():
    id_user = request.form['id_user']
    nome = request.form['name']
    email = request.form['email']
    senha = request.form['senha']
    telefone = request.form['telefone']

    usuario = User.query.filter_by(nome=nome).first()

    if usuario:
        flash('Usuário já existente!')
        return redirect(url_for('menu'))

    novo_user = Projetos(id_user=id_user, nome=nome, telefone=telefone, email=email, senha=senha)
    
    db.session.add(novo_user)
    db.session.commit()

    return redirect(url_for('menu'))

@app.route('/editar')
def editarProjeto():
    if 'user' not in session or session['user'] == None:
        return redirect(url_for('login', proxima=url_for('editarProjeto')))
    return render_template('Tela_de_CadastroProjeto.html')

@app.route('/autenticar', methods=['POST', ])
def autenticar():
    user = User.query.filter_by(username=request.form['usuario']).first()
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