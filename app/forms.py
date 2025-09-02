from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, FloatField, IntegerField, PasswordField
from wtforms.validators import DataRequired, Email, NumberRange, Length

class NomeForm(FlaskForm):
    nome = StringField("Nome", validators=[DataRequired()])
    email = StringField("E-mail", validators=[DataRequired(), Email(message="Credenciais inválidas")])
    senha = PasswordField("Senha", validators=[DataRequired(), Length(min=6)])
    submit = SubmitField("Enviar")

class CarroForm(FlaskForm):
    placa = StringField("Placa", validators=[DataRequired(), Length(min=7, max=8)])
    modelo = StringField("Modelo", validators=[DataRequired(), Length(min=2, max=100)])
    cor = StringField("Cor", validators=[DataRequired(), Length(min=2, max=50)])
    submit = SubmitField("Salvar")


class LoginForm(FlaskForm):
    email = StringField("E-mail", validators=[DataRequired(), Email()])
    senha = PasswordField("Senha", validators=[DataRequired()])
    submit = SubmitField("Entrar")