from . import routes
from src.controllers.user import *


@routes.route('/', methods=['GET'])
def indexRoute():
    return renderIndex()


@routes.route('/indexUser', methods=['GET'])
def indexUserRoute():
    return renderIndexUser()


@routes.route('/login', methods=['GET'])
def loginRoute():
    return renderLogin()


@routes.route('/logout', methods=['GET'])
def logoutRoute():
    return logout()


@routes.route('/authenticate', methods=['POST'])
def authenticateRoute():
    return authenticate()
