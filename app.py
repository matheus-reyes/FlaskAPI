from flask import Flask, render_template, request, redirect, session, flash
from flask.helpers import url_for

app = Flask(__name__)
app.secret_key = '!@#Chave_muito_segura_kkjkk!@#'


@app.route('/')
def renderIndex():
    title: str = "Página Inicial"
    return render_template('index.html', title=title)


@app.route('/indexUser')
def renderIndexUser():
    title: str = "Página Inicial"
    return render_template('indexUser.html', title=title)


@app.route('/newGame')
def renderNewGame():
    title: str = "Criar Jogo"
    return render_template('newGame.html', title=title)


@app.route('/createGame', methods=['POST'])
def createGame():
    # name: str = request.form['name']
    # category: str = request.form['category']
    # console: str = request.form['console']
    # criar o jogo
    return redirect(url_for('renderIndex'))


@app.route('/login')
def renderLogin():
    title: str = "Login"
    return render_template('login.html', title=title)


@app.route('/authenticate', methods=['POST'])
def authenticate():
    email: str = request.form['email']
    password: str = request.form['password']
    if password == password and email == email:
        session['email'] = request.form['email']
        flash(request.form['email'] + ' logado com sucesso!')
        return redirect(url_for('renderIndexUser'))
    else:
        flash('Senha ou E-mail incorretos')
        return redirect(url_for('renderIndex'))


@app.route('/logout')
def logout():
    session['email'] = None
    flash('Usuário não logado')
    return redirect(url_for('renderIndex'))


app.run(debug=True)
