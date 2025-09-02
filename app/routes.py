from flask_login import login_user, logout_user, login_required, current_user
from flask import render_template, request, jsonify, redirect, url_for, flash
from app import app, db
from app.forms import NomeForm, LoginForm
from app.models import Veiculo, Localizacao, Usuario
import random 
from datetime import datetime




#index/login
@app.route("/", methods=["GET", "POST"])
def index():
    if current_user.is_authenticated:
        return redirect(url_for("listar_veiculos"))

    if request.method == "POST":
        email = request.form["email"]
        senha = request.form["senha"]
        usuario = Usuario.query.filter_by(email=email).first()

        if usuario and usuario.check_password(senha):
            login_user(usuario)
            flash("Login realizado com sucesso!", "success")


            return redirect(url_for("index"))
        else:
            flash("Credenciais inválidas", "danger")

    return render_template("index.html", title="Login")





                                            #cadastro de usuario
@app.route("/form", methods=["GET", "POST"])
def form():
    if current_user.is_authenticated:
        return redirect(url_for("index"))
    
    form = NomeForm()
    mensagem = None

    if form.validate_on_submit():
        nome = form.nome.data
        email = form.email.data
        senha = form.senha.data

        # Verifica se já existe usuário com este email
        existente = Usuario.query.filter_by(email=email).first()
        if existente:
            mensagem = "E-mail já cadastrado."
        else:
            usuario = Usuario(nome=nome, email=email)
            usuario.set_password(senha)
            db.session.add(usuario)
            db.session.commit()
            mensagem = f"Usuário {nome} cadastrado com sucesso!"

    elif form.is_submitted() and not form.validate():  
        mensagem = "Credenciais inválidas"

    return render_template("form.html", title="Cadastro Usuário", form=form, mensagem=mensagem)



#Sair da aplicação
@app.route("/logout")
@login_required
def logout():
    logout_user()
    flash("Você saiu da conta.", "info")
    return redirect(url_for("index"))


#perfil
@app.route("/perfil")
@login_required
def perfil():
    return render_template("perfil.html", title="Perfil", usuario=current_user)






#CRUDDEVEÍCULOS

@app.route("/veiculos")
@login_required
def listar_veiculos():
    veiculos = Veiculo.query.all()
    return render_template("veiculos.html", title="Lista de Veículos", veiculos=veiculos)



LAT_MIN, LAT_MAX = -3.85, -3.70
LON_MIN, LON_MAX = -38.60, -38.50


@app.route("/veiculo/novo", methods=["GET", "POST"])
@login_required
def novo_veiculo():
    if request.method == "POST":
        placa = request.form["placa"]
        modelo = request.form["modelo"]
        cor = request.form.get("cor")

        existente = Veiculo.query.filter_by(placa=placa).first()
        if existente:
            flash(f"Placa já está cadastrada!", "danger")
            return redirect(url_for("novo_veiculo"))

        veiculo = Veiculo(placa=placa, modelo=modelo, cor=cor)
        db.session.add(veiculo)
        db.session.commit()


        # Cria localização inicial aleatória
        latitude = round(random.uniform(LAT_MIN, LAT_MAX), 6)
        longitude = round(random.uniform(LON_MIN, LON_MAX), 6)
        localizacao = Localizacao(
            veiculo_id=veiculo.id, 
            latitude=latitude,
            longitude=longitude
        )
        db.session.add(localizacao)
        db.session.commit()



        flash("Veículo cadastrado com sucesso!", "success")
        return redirect(url_for("listar_veiculos"))
    return render_template("veiculo_form.html", title="Novo Veículo")




@app.route("/veiculo/<int:id>/editar", methods=["GET", "POST"])
@login_required
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
@login_required
def excluir_veiculo(id):
    veiculo = Veiculo.query.get_or_404(id)

    Localizacao.query.filter_by(veiculo_id=veiculo.id).delete()

    db.session.delete(veiculo)
    db.session.commit()
    flash("Veículo excluído com sucesso!", "success")
    return redirect(url_for("listar_veiculos"))





                                    #lista de localizações do carro
@app.route("/localizacoes/<int:veiculo_id>")
@login_required
def listar_localizacoes(veiculo_id):
    veiculo = Veiculo.query.get_or_404(veiculo_id)
    localizacoes = veiculo.localizacoes
    return render_template("localizacoes.html",
                           title=f"Localizações do Veículo {veiculo.placa}",
                           veiculo=veiculo,
                           localizacoes=localizacoes)







                                    #carregar as localizações dos carros
@app.route("/api/localizacoes")
@login_required
def api_localizacoes():
    localizacoes = [loc.to_dict() for loc in Localizacao.query.all()]

    return jsonify(localizacoes)



                                    #carregar o mapa
@app.route("/mapa")
@login_required
def mapa():
    return render_template("mapa.html", title="Mapa de Veículos")





                                    #carregar o formato json dos carros cadastrados
@app.route("/api/veiculos", methods=["GET", "POST"])
@login_required
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