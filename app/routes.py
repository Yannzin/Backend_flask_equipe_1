from flask import render_template, request, jsonify, redirect, url_for, flash
from app import app, db
from app.forms import NomeForm
from app.models import Veiculo, Localizacao, Usuario
from datetime import datetime

#Inicio
@app.route("/")
def index():
    return render_template("index.html", title="Página Inicial")

@app.route("/sobre")
def sobre():
    return render_template("about.html", title="Sobre o Projeto")

#Formulário
@app.route("/form", methods=["GET", "POST"])
def form():
    form = NomeForm()
    mensagem = None
    if form.validate_on_submit():
        nome = form.nome.data
        mensagem = f"Olá, {nome}! Formulário recebido com sucesso."
    return render_template("form.html", title="Formulário", form=form, mensagem=mensagem)


#CRUDDEVEÍCULOS

@app.route("/veiculos")
def listar_veiculos():
    veiculos = Veiculo.query.all()
    return render_template("veiculos.html", title="Lista de Veículos", veiculos=veiculos)

@app.route("/veiculo/novo", methods=["GET", "POST"])
def novo_veiculo():
    if request.method == "POST":
        placa = request.form["placa"]
        modelo = request.form["modelo"]
        cor = request.form.get("cor")
        veiculo = Veiculo(placa=placa, modelo=modelo, cor=cor)
        db.session.add(veiculo)
        db.session.commit()
        flash("Veículo cadastrado com sucesso!", "success")
        return redirect(url_for("listar_veiculos"))
    return render_template("veiculo_form.html", title="Novo Veículo")

@app.route("/veiculo/<int:id>/editar", methods=["GET", "POST"])
def editar_veiculo(id):
    veiculo = Veiculo.query.get_or_404(id)
    if request.method == "POST":
        veiculo.placa = request.form["placa"]
        veiculo.modelo = request.form["modelo"]
        veiculo.cor = request.form.get("cor")
        db.session.commit()
        flash("Veículo atualizado com sucesso!", "success")
        return redirect(url_for("listar_veiculos"))
    return render_template("veiculo_form.html", title="Editar Veículo", veiculo=veiculo)

@app.route("/veiculo/<int:id>/excluir", methods=["POST"])
def excluir_veiculo(id):
    veiculo = Veiculo.query.get_or_404(id)
    db.session.delete(veiculo)
    db.session.commit()
    flash("Veículo excluído com sucesso!", "success")
    return redirect(url_for("listar_veiculos"))


@app.route("/localizacoes/<int:veiculo_id>")
def listar_localizacoes(veiculo_id):
    veiculo = Veiculo.query.get_or_404(veiculo_id)
    return render_template("localizacoes.html", title="Localizações", veiculo=veiculo, localizacoes=veiculo.localizacoes)


@app.route("/api/veiculos", methods=["GET", "POST"])
def api_veiculos():
    if request.method == "POST":
        data = request.get_json()
        veiculo = Veiculo(
            placa=data["placa"],
            modelo=data["modelo"],
            cor=data.get("cor")
        )
        db.session.add(veiculo)
        db.session.commit()
        return jsonify(veiculo.to_dict()), 201

    veiculos = Veiculo.query.all()
    return jsonify([v.to_dict() for v in veiculos])

@app.route("/api/veiculos/<int:id>", methods=["GET", "PUT", "DELETE"])
def api_veiculo(id):
    veiculo = Veiculo.query.get_or_404(id)

    if request.method == "PUT":
        data = request.get_json()
        veiculo.placa = data["placa"]
        veiculo.modelo = data["modelo"]
        veiculo.cor = data.get("cor", veiculo.cor)
        db.session.commit()
        return jsonify(veiculo.to_dict())

    if request.method == "DELETE":
        db.session.delete(veiculo)
        db.session.commit()
        return "", 204

    return jsonify(veiculo.to_dict())


