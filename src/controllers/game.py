from flask import render_template, redirect
from flask.helpers import url_for


def renderNewGame():
    title: str = "Criar Jogo"
    return render_template('newGame.html', title=title)


def createGame():
    # name: str = request.form['name']
    # category: str = request.form['category']
    # console: str = request.form['console']
    # criar o jogo
    return redirect(url_for('routes.indexRoute'))
