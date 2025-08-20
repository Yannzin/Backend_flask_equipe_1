from flask import render_template, request, jsonify
from app import app



@app.route("/")
def index():
    return render_template("index.html", title="Página Inicial")


## Aula1/Ex1
@app.route("/olamundo")
def ola_mundo():
    ##return render_template("olamundo.html", title="Ola Mundo")
    return "Olá, mundo — esta é a rota"

##Aula1/Ex2
@app.route("/hello/<nome>")
def hello(nome):
    return f"Olá, {nome}!"
