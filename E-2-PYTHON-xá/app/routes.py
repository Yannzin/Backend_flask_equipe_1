from flask import render_template, request, redirect, url_for
from app import app

# dicionário de veículos
veiculos = {
    1: {"placa": "ABC-1234", "modelo": "Fiat Uno", "cidade": "São Paulo"},
    2: {"placa": "XYZ-9876", "modelo": "Toyota Corolla", "cidade": "Rio de Janeiro"},
    3: {"placa": "QWE-5678", "modelo": "Honda Civic", "cidade": "Curitiba"}
}
proximo_id = 4  # controla o próximo ID para novos


# página inicial
@app.route("/")
def home():
    return redirect(url_for("listar_veiculos"))


# lista de veículos
@app.route("/veiculos")
def listar_veiculos():
    return render_template("veiculos.html", veiculos=veiculos)


# cadastrar veículo
@app.route("/veiculos/novo", methods=["GET", "POST"])
def cadastrar_veiculo():
    global proximo_id
    if request.method == "POST":
        modelo = request.form.get("modelo")
        placa = request.form.get("placa")
        cidade = request.form.get("cidade")

        # salvar no dicionário
        veiculos[proximo_id] = {
            "modelo": modelo,
            "placa": placa,
            "cidade": cidade
        }
        proximo_id += 1

        return redirect(url_for("listar_veiculos"))
    
    return render_template("cadastrar_veiculo.html")


# mostrar localização de 1 veículo
@app.route("/veiculos/<int:veiculo_id>")
def localizacao(veiculo_id):
    veiculo = veiculos.get(veiculo_id)
    if not veiculo:
        return "Veículo não encontrado", 404
    return render_template("localizacao.html", veiculo=veiculo)
