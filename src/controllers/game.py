from flask import render_template, redirect, request, session, flash, jsonify
from flask.helpers import url_for
from src.database import db
from src.models import Game


def renderNewGame():
    title: str = "Criar Jogo"
    return render_template('newGame.html', title=title)


def createGame():
    name: str = request.form['name']
    category: str = request.form['category']
    console: str = request.form['console']
    user_id: int = session['user_id']

    try:
        game = Game(
            name=name,
            category=category,
            console=console,
            user_id=user_id
        )
        db.session.add(game)
        db.session.commit()
        flash('Jogo de ID {} adicionado'.format(game.id))
        return redirect(url_for('routes.indexUserRoute'))
    except Exception as exception:
        return(str(exception))


def renderListGames():
    games = getAllGames(session['user_id'])
    return render_template('listGames.html', games=games)


def getAllGames(user_id):
    return Game.query.filter_by(user_id=user_id)


def getGameById(id_):
    try:
        game = Game.query.filter_by(id=id_).first()
        return jsonify(game.serialize())
    except Exception as exception:
        return(str(exception))
