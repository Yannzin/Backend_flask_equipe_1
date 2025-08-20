from flask import render_template, request, jsonify
from app import app


# Aula 1 — Introdução e primeira rota
@app.route("/")
def index():
    return render_template("index.html", title="Página Inicial")




@app.route("/olamundo")
def ola_mundo():
    ##return render_template("olamundo.html", title="Ola Mundo")
    return "Olá, mundo — esta é a rota /hello"

