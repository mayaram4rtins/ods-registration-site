from flask import Flask, render_template, request, flash, redirect, session
import json

app = Flask(__name__, template_folder='templates')
app.secret_key = 'palavrasecreta'

@app.route('/')
def index():
    return render_template('Tela_de_login.html')

@app.route('/login')
def login():
    return render_template('Tela_de_login.html')

@app.route('/autenticar', methods=['POST',])
def autenticar():
    if 'senha' == request.form['password']:
        session['usuario_logado'] = request.form['name']
        flash(request.form['name'] + ' logou com sucesso!')
        return redirect('/')
    else:
        flash(request.form['name'] + " não logado! Verifique suas credenciais.")
        return redirect('/login')

if __name__ == '__main__':
    app.run(debug=True)