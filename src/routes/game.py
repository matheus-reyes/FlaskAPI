from . import routes
from src.controllers.game import *


@routes.route('/newGame', methods=['GET'])
def newGameRoute():
    return renderNewGame()


@routes.route('/createGame', methods=['POST'])
def createGameRoute():
    return createGame()


@routes.route('/listGame', methods=['GET'])
def listGameRoute():
    return renderListGames()
