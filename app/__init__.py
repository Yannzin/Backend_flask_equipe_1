from flask import Flask, json
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from flask_jwt_extended import JWTManager
from dotenv import load_dotenv
import os

# Carregar .env correto dependendo do ambiente
env_file = '.env.prod' if os.getenv('FLASK_ENV') == 'production' else '.env.dev'
load_dotenv(env_file)

app = Flask(__name__, template_folder="templates", static_folder="static")

# Chaves de segurança
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY', 'dev-secret-key')
app.config['JWT_SECRET_KEY'] = os.getenv("JWT_SECRET_KEY", "jwt-secret-dev")
jwt = JWTManager(app)

# Configuração do banco de dados
basedir = os.path.abspath(os.path.dirname(__file__))

# Pega a URL do PostgreSQL do .env ou usa SQLite como fallback


app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://postgres:root@localhost/localiza"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
migrate = Migrate(app, db)

# Ajuste do JSON Encoder
if not hasattr(json, 'JSONEncoder'):
    from json import JSONEncoder
    json.JSONEncoder = JSONEncoder

# Configuração do Login Manager
login_manager = LoginManager()
login_manager.login_view = "index"
login_manager.init_app(app)

from app.models import Usuario

@login_manager.user_loader
def load_user(user_id):
    return Usuario.query.get(int(user_id))

from app import routes
