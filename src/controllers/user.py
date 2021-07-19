from flask import render_template, request, redirect, session, flash
from flask.helpers import url_for
from src.database import db
from src.models import User
import bcrypt


def renderIndex():
    title: str = "Página Inicial"
    return render_template('index.html', title=title)


def renderIndexUser():
    title: str = "Página Inicial"
    return render_template('indexUser.html', title=title)


def renderLogin():
    title: str = "Login"
    return render_template('login.html', title=title)


def renderRegister():
    title: str = "Cadastro"
    return render_template('register.html', title=title)


def logout():
    session['email'] = None
    session['user_id'] = None
    flash('Usuário não logado')
    return redirect(url_for('routes.indexRoute'))


def authenticate():
    email: str = request.form['email']
    password: str = request.form['password']
    users = User.query.all()
    for user in users:
        if bcrypt.checkpw(password.encode('utf-8'), user.password.encode('utf-8')) and email == user.email:
            session['email'] = user.email
            session['user_id'] = user.id
            flash(session['email'] + ' logado com sucesso!')
            return redirect(url_for('routes.indexUserRoute'))
        else:
            flash('Senha ou E-mail incorretos')
            return redirect(url_for('routes.indexRoute'))


def createUser():
    name: str = request.form['name']
    email: str = request.form['email']
    password = bcrypt.hashpw(request.form['password'].encode('utf-8'), bcrypt.gensalt())
    try:
        user = User(
            name=name,
            email=email,
            password=password.decode('utf-8')
        )
        db.session.add(user)
        db.session.commit()
        flash('Cadastro realizado com sucesso')
        return redirect(url_for('routes.loginRoute'))
    except Exception as exception:
        return(str(exception))
