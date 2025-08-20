from flask import render_template, request, jsonify, flash, redirect, url_for
from app import app
from app.forms import NomeForm

# Aula 1 — Introdução e primeira rota
@app.route("/")
def index():
    return render_template("index.html", title="Página Inicial")

    


@app.route("/sobre")
def sobre():
    return render_template("about.html", title="Sobre o Projeto")

# Aula 2 — Formulários
@app.route("/form", methods=["GET", "POST"])
def form():
    form = NomeForm()
    mensagem = None

    if form.validate_on_submit():
        nome = form.nome.data
        email = form.email.data


## Aula 2 Exercicio 2
        flash(f"Formulário enviado com sucesso! Nome: {nome}, Email: {email}", "success")
        return redirect(url_for("index"))

    elif form.is_submitted() and not form.validate():
        mensagem = "Formulário inválido! Verifique os campos e tente novamente."
        flash(mensagem, "error")

    return render_template("form.html", title="Formulário", form=form, mensagem=mensagem)

# Aula 3 — API REST
@app.route("/api/dados")
def api_dados():
    dados = [
        {"id": 1, "nome": "Ana Vitória"},
        {"id": 2, "nome": "Ryan Feitosa"},
        {"id": 3, "nome": "Anderson Freitas"}
    ]
    return jsonify(dados)
