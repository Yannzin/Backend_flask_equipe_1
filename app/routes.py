from flask import render_template, request, jsonify
from app import app


##Aula 2
@app.route("/")
def index():
    pessoas = [
        {"id": 1, "nome": "Ryan"},
        {"id": 1, "nome": "Ana"},
        {"id": 1, "nome": "Anderson"}

    ]
    ##Exercicio 1 (Passar um título dinâmico)
    titulo = request.args.get("titulo", "Página inicial")

    return render_template("index.html",title="Página Inicial", pessoas = pessoas)


