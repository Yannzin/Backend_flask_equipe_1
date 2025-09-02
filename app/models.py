from app import db
from flask_login import UserMixin
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash

class Veiculo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    placa = db.Column(db.String(10), unique=True, nullable=False)   
    modelo = db.Column(db.String(100), nullable=False)              
    cor = db.Column(db.String(50))
    

    localizacoes = db.relationship("Localizacao", backref="veiculo", lazy=True, order_by="Localizacao.timestamp")

    def to_dict(self):
        return {
            "id": self.id,
            "placa": self.placa,
            "modelo": self.modelo,
            "cor": self.cor
        }


class Localizacao(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    veiculo_id = db.Column(db.Integer, db.ForeignKey("veiculo.id"), nullable=False)
    latitude = db.Column(db.Float, nullable=False)
    longitude = db.Column(db.Float, nullable=False)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)  

    def to_dict(self):
        return {
            "id": self.id,
            "veiculo_id": self.veiculo_id,
            "latitude": self.latitude,
            "longitude": self.longitude,
            "timestamp": self.timestamp.strftime("%Y-%m-%d %H:%M:%S")
        }


class Usuario(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(128), nullable=False)

    def to_dict(self):
        return {
            "id": self.id,
            "nome": self.nome,
            "email": self.email
        }

    def set_password(self, senha):
        self.password_hash = generate_password_hash(senha)

    def check_password(self, senha):
        return check_password_hash(self.password_hash, senha)