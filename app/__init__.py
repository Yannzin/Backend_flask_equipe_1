import os
from flask import Flask, json
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from dotenv import load_dotenv

# 1️⃣ Carrega o .env primeiro
env_file = '.env.prod' if os.getenv('FLASK_ENV') == 'production' else '.env.dev'
load_dotenv(env_file)

# 2️⃣ Flask app
app = Flask(__name__, template_folder="templates", static_folder="static")

# 3️⃣ Configurações gerais
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY', 'dev-secret-key')
app.config['DEBUG'] = os.getenv('DEBUG', 'False') == 'True'
app.config['ENV'] = os.getenv('FLASK_ENV', 'development')

# 4️⃣ Configuração do banco de dados
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv(
    'DATABASE_URL',
    f"sqlite:///{os.path.join(basedir, 'app.db')}"  # fallback para SQLite
)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# 5️⃣ Inicializa DB e Migrate
db = SQLAlchemy(app)
migrate = Migrate(app, db)

# 6️⃣ Corrige JSONEncoder se necessário
if not hasattr(json, 'JSONEncoder'):
    from json import JSONEncoder
    json.JSONEncoder = JSONEncoder

# 7️⃣ Importa rotas e models
from app import routes, models
