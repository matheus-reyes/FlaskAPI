from flask import render_template, request, redirect, session, flash
from flask.helpers import url_for


def renderIndex():
    title: str = "Página Inicial"
    return render_template('index.html', title=title)


def renderIndexUser():
    title: str = "Página Inicial"
    return render_template('indexUser.html', title=title)


def renderLogin():
    title: str = "Login"
    return render_template('login.html', title=title)


def logout():
    session['email'] = None
    flash('Usuário não logado')
    return redirect(url_for('routes.indexRoute'))


def authenticate():
    email: str = request.form['email']
    password: str = request.form['password']
    if password == password and email == email:
        session['email'] = request.form['email']
        flash(request.form['email'] + ' logado com sucesso!')
        return redirect(url_for('routes.indexUserRoute'))
    else:
        flash('Senha ou E-mail incorretos')
        return redirect(url_for('routes.indexRoute'))
