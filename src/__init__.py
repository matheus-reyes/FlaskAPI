from flask import Flask
from .database import db, migrate
from .routes import *
from .models import *
import os

app = Flask(__name__)
app.secret_key = '!@#Chave_muito_segura_kkjkk!@#'
app.config.from_object(os.environ['APP_SETTINGS'])
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


db.init_app(app)
migrate.init_app(app, db)

app.register_blueprint(routes)
with app.app_context():
    db.create_all()
app.run(debug=True)
